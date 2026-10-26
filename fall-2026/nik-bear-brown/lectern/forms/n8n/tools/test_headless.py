#!/usr/bin/env python3
"""Run the five Lectern workflows in a disposable n8n profile and compare what they produce with the expected outputs
that the PYTHON Lectern produced (tools/make_fixtures.py). Never touches the normal ~/.n8n profile, never needs a
credential, never calls the network, never sends anything.

  python3 tools/test_headless.py            # all five
  python3 tools/test_headless.py --only 02
"""
import argparse, copy, datetime, json, os, pathlib, re, shutil, subprocess, sys, tempfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
FOLDERS = {"01": "01-collect", "02": "02-filter", "03": "03-delta", "04": "04-post-to-discord", "05": "05-daily"}
LAST = {"01": "Normalise", "02": "Assemble run", "03": "Diff", "04": "Result", "05": "Daily summary"}


def parse_execution(text):
    dec = json.JSONDecoder()
    for m in re.finditer(r"^\s*\{", text, re.M):
        try:
            v, _ = dec.raw_decode(text[m.start():].lstrip())
            if isinstance(v, dict) and isinstance(v.get("data", {}).get("resultData"), dict):
                return v
        except (ValueError, AttributeError):
            pass
    raise RuntimeError("n8n returned no execution record:\n" + text[-1500:])


def items(execution, node):
    runs = execution["data"]["resultData"].get("runData", {}).get(node)
    if not runs:
        return None
    return [i["json"] for i in (runs[-1].get("data", {}).get("main", [[]])[0] or [])]


class Runner:
    def __init__(self, tmp):
        self.exe = shutil.which("n8n") or sys.exit("n8n is not installed")
        self.env = {k: v for k, v in os.environ.items() if not k.startswith(("N8N_", "DB_", "QUEUE_", "EXECUTIONS_"))}
        self.env.update({"N8N_USER_FOLDER": tmp, "N8N_DIAGNOSTICS_ENABLED": "false", "N8N_VERSION_NOTIFICATIONS_ENABLED": "false", "N8N_TEMPLATES_ENABLED": "false",
                         "N8N_PERSONALIZATION_ENABLED": "false", "N8N_RUNNERS_ENABLED": "false", "N8N_COMMUNITY_PACKAGES_ENABLED": "false", "DB_SQLITE_POOL_SIZE": "1",
                         "N8N_BLOCK_FILE_ACCESS_TO_N8N_FILES": "false"})
        self.version = subprocess.check_output([self.exe, "--version"], text=True, env=self.env).strip()

    def import_all(self, workflows, tmp):
        bundle = pathlib.Path(tmp) / "import.json"
        bundle.write_text(json.dumps(workflows))
        r = subprocess.run([self.exe, "import:workflow", "--input=" + str(bundle)], env=self.env, text=True, capture_output=True, timeout=180)
        if r.returncode:
            raise RuntimeError("import failed: " + r.stderr[-1500:] + r.stdout[-1500:])

    def execute(self, wid):
        r = subprocess.run([self.exe, "execute", "--id=" + wid, "--rawOutput"], env=self.env, text=True, capture_output=True, timeout=240)
        return parse_execution(r.stdout + "\n" + r.stderr)


def err(ex):
    e = ex["data"]["resultData"].get("error")
    return (e.get("message") or str(e)) if e else None


def check(name, ok, detail=""):
    print(f"   {'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail and not ok else ""))
    return ok


def canon(x):
    return json.loads(json.dumps(x, sort_keys=True))


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--only"); a = ap.parse_args()
    which = [a.only] if a.only else list(FOLDERS)
    results = []
    with tempfile.TemporaryDirectory(prefix="lectern-n8n-") as tmp:
        os.chmod(tmp, 0o700)
        state_path, posted_path = os.path.join(tmp, "published-state.json"), os.path.join(tmp, "posted.json")
        wfs = {}
        for k, f in FOLDERS.items():
            wf = json.loads((ROOT / f / "workflow.json").read_text())
            if k == "05":
                s = json.dumps(wf).replace("__STATE_PATH__", state_path).replace("__POSTED_PATH__", posted_path)
                wf = json.loads(s)
            wfs[k] = wf
        run = Runner(tmp)
        print(f"n8n {run.version}; disposable profile; no network, no credentials, nothing sent")
        run.import_all(list(wfs.values()), tmp)

        for k in which:
            print(f"{FOLDERS[k]}")
            ex = run.execute(wfs[k]["id"])
            exp = json.loads((ROOT / FOLDERS[k] / "expected.json").read_text()) if k != "05" else None
            ok = check("ran without an error", err(ex) is None, err(ex) or "")
            out = items(ex, LAST[k]) if ok else None
            ok = check(f"'{LAST[k]}' produced one item", bool(out) and len(out) == 1, "no output") and ok
            if not (ok and out):
                results.append((k, False)); continue
            o = out[0]
            if k == "01":
                ok = check("views identical to the Python normalise()", canon(o["views"]) == canon(exp["views"]), "views differ") and ok
                ok = check("source status rows identical", canon(o["sources"]) == canon(exp["status"]), "status differs") and ok
            elif k == "02":
                ok = check("every record identical to the Python (fields, keep decision, matched words, reject reason)", canon(o["records"]) == canon(exp["records"]), "records differ") and ok
                ok = check("counts identical (kept, rejected by reason, duplicates)", canon(o["counts"]) == canon(exp["counts"]), f"{o['counts']} vs {exp['counts']}") and ok
            elif k == "03":
                summ = lambda rows: sorted(({"key": f"{r['source']}:{r['source_id']}", "why": r.get("why"), "fields": sorted(c["field"] for c in r.get("changes", []))} for r in rows), key=lambda x: x["key"])
                for part in ("new", "changed", "gone"):
                    ok = check(f"{part}: same postings, same reasons as the Python diff()", canon(summ(o[part])) == canon(exp[part]), f"{summ(o[part])} vs {exp[part]}") and ok
                ok = check("first-time companies identical", o["first_time_companies"] == exp["first_time_companies"]) and ok
                ok = check("a source that was down never closes its postings", any(g["why"].startswith("unknown: source unavailable") for g in o["gone"])) and ok
            elif k == "04":
                ok = check("same rows in the same order as the Python build_messages()", o["rows"] == exp["rows"], f"{o['rows']} vs {exp['rows']}") and ok
                ok = check("message text byte-identical (with the heading added by the node)", all(m == e for m, e in zip(o["messages"], exp["messages"])) and len(o["messages"]) == len(exp["messages"])) and ok
                ok = check("nothing was sent (send is false)", o["sent_count"] == 0 and o["posted_ids"] == []) and ok
            elif k == "05":
                ok = check("first run: baseline is 'no earlier run'; every kept posting is new", "no earlier run" in o["baseline"] and o["new"] == o["kept"] == json.loads((ROOT / "02-filter" / "expected.json").read_text())["counts"]["kept"], str(o)) and ok
                ok = check("state file written", os.path.exists(state_path)) and ok
                ex2 = run.execute(wfs[k]["id"])
                ok = check("same day again: refuses, because the state is not older than the run (as the Python does)", "not older than this run" in (err(ex2) or ""), str(err(ex2))) and ok
                nxt = copy.deepcopy(wfs[k])
                for n in nxt["nodes"]:
                    if n["name"] == "Settings":
                        n["parameters"]["jsCode"] = n["parameters"]["jsCode"].replace("date: ''", "date: '2026-10-20'")
                run.import_all([nxt], tmp)
                ex3 = run.execute(nxt["id"])
                o3 = (items(ex3, LAST[k]) or [{}])[0]
                ok = check("next day, same postings: nothing new, nothing changed, nothing gone, nothing to post", err(ex3) is None and o3.get("new") == 0 and o3.get("changed") == 0 and o3.get("gone") == 0 and o3.get("messages") == 0, str(o3) + str(err(ex3))) and ok
                ok = check("the state advanced to the later date", json.loads(open(state_path).read()).get("as_of") == "2026-10-20") and ok
            results.append((k, ok))
    allok = all(ok for _, ok in results)
    print("ALL PASSED" if allok else "FAILURES: " + ", ".join(k for k, ok in results if not ok))
    (ROOT / "test-results").mkdir(exist_ok=True)
    (ROOT / "test-results" / "headless-report.json").write_text(json.dumps({"runtime": run.version, "tested_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "results": {FOLDERS[k]: ok for k, ok in results}, "mode": "synthetic fixtures, no network, no credentials, nothing sent", "all_passed": allok}, indent=1) + "\n")
    return 0 if allok else 1


if __name__ == "__main__":
    raise SystemExit(main())
