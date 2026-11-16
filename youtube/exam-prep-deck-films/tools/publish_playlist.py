#!/usr/bin/env python3
"""publish_playlist.py - upload the 13 Key Terms films to @NikBearBrown, UNLISTED, in the playlist
"Computational Skepticism, Exam Prep", in deck order. Written 2026-11-12 at Bear's word ("put them up on YouTube
under a playlist"; playlist name and unlisted confirmed in chat).

    python3 publish_playlist.py --source DIR --dry-run     # checks everything, uploads nothing
    python3 publish_playlist.py --source DIR               # uploads (skips any film already in the ledger)

--source is the folder the masters were copied back into from the cluster (one sub-folder per slug). Each file must
match the reel's own master by sha256 or nothing is uploaded. Writes <slug>.srt and <slug>-youtube.md in each reel
folder first (captions from the narration on measured beat windows; description with chapters from the deck's slide
titles). Records each upload in the channel's publish ledger and in books/youtube/PUBLISH-LOG.md. Idempotent.
"""
import argparse, hashlib, json, re, shutil, sys, textwrap
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from films import ALL, BOOKS, film  # noqa: E402

CREDS = BOOKS / "youtube/credentials/nikbearbrown"
TOKEN, LEDGER = CREDS / "youtube_token.json", CREDS / "youtube_publish_ledger.json"
LOG = BOOKS / "youtube/PUBLISH-LOG.md"
CHANNEL_ID = "UCg0cw2ouRhQ8dr114yGp0mA"
PLAYLIST = "Computational Skepticism, Exam Prep"
PRIVACY = "unlisted"
SCOPES = ["https://www.googleapis.com/auth/youtube.upload", "https://www.googleapis.com/auth/youtube",
          "https://www.googleapis.com/auth/youtube.force-ssl"]


def sha(p):
    with open(p, "rb") as f:
        return hashlib.file_digest(f, "sha256").hexdigest()


def ts(sec):
    ms = int(round(sec * 1000)); h, rem = divmod(ms // 1000, 3600); m, s = divmod(rem, 60)
    return f"{h:02}:{m:02}:{s:02},{ms % 1000:03}"


def chap(sec):
    sec = int(sec); h, rem = divmod(sec, 3600); m, s = divmod(rem, 60)
    return f"{h}:{m:02}:{s:02}" if h else f"{m}:{s:02}"


def write_srt(sheet, out):
    """One cue per sentence group (at most two lines of 42 characters), timed by word share inside the beat."""
    cues, t = [], 0.0
    for b in sheet["beats"]:
        dur = float(b["actual_duration_s"]); text = b["narration_text"].strip()
        lead = float(b.get("lead_silence_s") or 0)
        sents = re.split(r"(?<=[.!?])\s+", text)
        chunks = []
        for s_ in sents:
            lines = textwrap.wrap(s_, 42)
            for i in range(0, len(lines), 2):
                chunks.append(" ".join(lines[i:i + 2]))
        words = [max(1, len(c.split())) for c in chunks]
        span = max(0.5, dur - lead - 0.3); acc = 0
        for c, w in zip(chunks, words):
            a = t + lead + span * acc / sum(words); acc += w
            z = t + lead + span * acc / sum(words)
            cues.append((a, z - 0.05, "\n".join(textwrap.wrap(c, 42))))
        t += dur
    out.write_text("\n\n".join(f"{i}\n{ts(a)} --> {ts(z)}\n{c}" for i, (a, z, c) in enumerate(cues, 1)) + "\n", encoding="utf-8")
    return len(cues), t


def description(F, sheet, deck):
    md = sheet["metadata"]; nar = json.loads((F["extract"] / "narration.json").read_text())
    titles = {s["index"]: s["title"] for s in deck["slides"]}
    chapters, t, seen = [], 0.0, set()
    for b in sheet["beats"]:
        bid = b["beat_id"]
        label = None
        if bid == "BOPEN": label = "Introduction"
        elif bid == "BDEFS": label = "Labels on every slide"
        elif b.get("deck") and b["deck"]["slide"] not in seen:
            seen.add(b["deck"]["slide"]); label = titles[b["deck"]["slide"]]
        elif bid == "BVDT": label = "Recap"
        elif bid == "BHTF": label = "Your turn"
        if label: chapters.append(f"{chap(t)} {label}")
        t += b["actual_duration_s"]
    body = [
        f"{md['title']}. {nar['opening_summary'].strip()}",
        "",
        f"Part of the playlist {PLAYLIST}: one film per chapter of INFO 7375, Computational Skepticism for AI. Each film walks "
        "through the chapter's terminology deck one animation at a time; every term is stated plainly and then given a concrete "
        "example. The exam is built from case studies, so learn the exact term and how to tell it from its look-alike.",
        "",
        "Chapters",
        *chapters,
        "",
        "Your turn: paste this into Claude to practise.",
        nar["your_turn"]["command"].strip(),
        "",
        "Course and slides by Professor Nik Bear Brown. Narration: Liam, in for Bear (a synthetic voice, Kokoro). "
        "Numbers on the slides are computed, simulated or illustrative, as each slide's corner label says.",
        "",
        "#ComputationalSkepticism #AI #ExamPrep",
    ]
    text = "\n".join(body).replace("<", "").replace(">", "")
    return text[:4900]


def service():
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build
    c = Credentials.from_authorized_user_file(str(TOKEN), SCOPES)
    if not c.valid:
        c.refresh(Request()); TOKEN.write_text(c.to_json())
    return build("youtube", "v3", credentials=c)


def find_playlist(yt):
    tok, found = None, []
    while True:
        r = yt.playlists().list(part="snippet,status", mine=True, maxResults=50, pageToken=tok).execute()
        found += [i for i in r["items"] if i["snippet"]["title"] == PLAYLIST]
        tok = r.get("nextPageToken")
        if not tok:
            return found


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--source", required=True); ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args(); src = Path(a.source)
    ledger = json.loads(LEDGER.read_text()); plan, probs = [], []
    for nn in ALL:
        F = film(nn); slug = F["slug"]; reel = F["reel"]
        sheet = json.loads((reel / "beat_sheet.json").read_text()); deck = json.loads((F["extract"] / "deck.json").read_text())
        master = reel / "exports/landscape" / f"{slug}.mp4"; up = src / slug / f"{slug}.mp4"
        if not up.exists(): probs.append(f"{slug}: no copy from the cluster"); continue
        if sha(up) != sha(master): probs.append(f"{slug}: cluster copy differs from the master")
        n, total = write_srt(sheet, reel / f"{slug}.srt")
        d = description(F, sheet, deck); (reel / f"{slug}-youtube.md").write_text(d + "\n", encoding="utf-8")
        if slug in ledger and not str(ledger[slug]).startswith("_"):
            print(f"{nn} {slug}: already uploaded as {ledger[slug]} (skipped)"); plan.append((nn, F, up, d, ledger[slug])); continue
        plan.append((nn, F, up, d, None))
        print(f"{nn} {sheet['metadata']['title']!r}  {up.stat().st_size / 1e6:.0f} MB  {total / 60:.1f} min  {n} caption cues  {PRIVACY}")
    if probs:
        sys.exit("BLOCKED: " + "; ".join(probs))
    yt = service()
    ch = yt.channels().list(part="id", mine=True).execute()["items"][0]["id"]
    if ch != CHANNEL_ID:
        sys.exit(f"token is for channel {ch}, not @NikBearBrown")
    found = find_playlist(yt)
    if len(found) > 1:
        sys.exit("more than one playlist with this name")
    print("channel @NikBearBrown ok;", f"playlist found: {found[0]['id']} ({found[0]['status']['privacyStatus']})" if found else f"playlist will be created ({PRIVACY})")
    if a.dry_run:
        print(f"[dry-run] {sum(1 for p in plan if not p[4])} to upload; captions and descriptions written; nothing uploaded."); return
    from googleapiclient.http import MediaFileUpload
    if found:
        pid = found[0]["id"]
    else:
        pid = yt.playlists().insert(part="snippet,status", body={"snippet": {"title": PLAYLIST, "description":
              "Key terms for INFO 7375, Computational Skepticism for AI: one film per chapter, every term stated and then given "
              "an example. Narrated by Liam, in for Professor Bear."}, "status": {"privacyStatus": PRIVACY}}).execute()["id"]
        print("created playlist", pid)
    shutil.copy2(LEDGER, LEDGER.with_name(LEDGER.name + ".bak-2026-11-12-exam-prep"))
    in_pl = set()
    tok = None
    from googleapiclient.errors import HttpError
    while True:
        try:
            r = yt.playlistItems().list(part="snippet", playlistId=pid, maxResults=50, pageToken=tok).execute()
        except HttpError as e:  # a playlist created seconds ago can 404 on read: treat it as empty
            if e.resp.status == 404: break
            raise
        in_pl |= {i["snippet"]["resourceId"]["videoId"] for i in r["items"]}; tok = r.get("nextPageToken")
        if not tok: break
    log = []
    for pos, (nn, F, up, d, vid) in enumerate(plan):
        slug = F["slug"]; title = json.loads((F["reel"] / "beat_sheet.json").read_text())["metadata"]["title"]
        if not vid:
            body = {"snippet": {"title": title, "description": d, "categoryId": "27", "defaultLanguage": "en", "defaultAudioLanguage": "en",
                                "tags": ["Computational Skepticism", "INFO 7375", "AI", "exam prep", F["topic"], "key terms"]},
                    "status": {"privacyStatus": PRIVACY, "selfDeclaredMadeForKids": False, "containsSyntheticMedia": True}}
            req = yt.videos().insert(part="snippet,status", body=body,
                                     media_body=MediaFileUpload(str(up), chunksize=-1, resumable=True, mimetype="video/mp4"))
            resp = None
            while resp is None:
                _, resp = req.next_chunk()
            vid = resp["id"]; print(f"{nn} {slug} -> https://youtu.be/{vid} ({PRIVACY})", flush=True)
            L = json.loads(LEDGER.read_text()); L[slug] = vid; L.setdefault("_uploaded_sha256s", []).append(sha(up))
            LEDGER.write_text(json.dumps(L, indent=2))
            try:
                yt.captions().insert(part="snippet", body={"snippet": {"videoId": vid, "language": "en", "name": "English", "isDraft": False}},
                                     media_body=MediaFileUpload(str(F["reel"] / f"{slug}.srt"), mimetype="application/x-subrip")).execute()
                print("   captions ok")
            except Exception as e:  # noqa: BLE001
                print(f"   CAPTIONS FAILED (video is up; re-run later to retry): {e}")
            log.append(f"| {datetime.now():%Y-%m-%d} | {title} | https://youtu.be/{vid} | {PRIVACY} | {PLAYLIST} |")
        if vid not in in_pl:
            yt.playlistItems().insert(part="snippet", body={"snippet": {"playlistId": pid, "position": pos,
                                      "resourceId": {"kind": "youtube#video", "videoId": vid}}}).execute()
            in_pl.add(vid); print(f"   in playlist at position {pos + 1}")
    if log:
        with LOG.open("a") as f:
            f.write(f"\n\n## {datetime.now():%Y-%m-%d} Computational Skepticism, Exam Prep (13 Key Terms films, unlisted)\n\n"
                    "| Date | Title | URL | Privacy | Playlist |\n|---|---|---|---|---|\n" + "\n".join(log) + "\n")
    print(f"playlist: https://www.youtube.com/playlist?list={pid}")


if __name__ == "__main__":
    main()
