#!/usr/bin/env python3
"""Tests for collect/speakers_judge.py: a company is a speaker lead only if its own MCP page is sourced and it publishes a public route.
Made-up companies; no network."""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import copy, json, unittest

import speakers_judge as sj

with open(lp.config("keywords.json")) as _f:
    KW = json.load(_f)
RULE = KW["speakers_rule"]
U = "https://example.test/"


def sig(kind, n=1):
    return {"kind": kind, "url": f"{U}{kind}/{n}", "shows": "made up"}


def lead(**kw):
    rec = {"id": "speakers-madeup", "company": "Made Up Co", "verdict": "keep", "why": "", "mcp": {"name": "Made Up MCP", "primary_source": U + "mcp", "status": "GA"},
           "signals": [sig("mcp_docs"), sig("devrel_team"), sig("mcp_talk", 1), sig("mcp_talk", 2), sig("community_channel")], "people_found": 2,
           "contact_route": {"kind": "devrel-page", "url": U + "devrel"}}
    rec.update(kw)
    return sj.lead_view(rec), rec


def judge(**kw):
    v, rec = lead(**kw)
    return sj.judge_speaker(v, rec, KW)


class Judge(unittest.TestCase):
    def test_the_rule_is_off_and_the_weights_add_up_to_a_hundred(self):
        self.assertEqual(RULE["posting"], "off")
        w = RULE["weights"]
        full = w["mcp_docs"] + w["devrel_team"] + w["mcp_talk"] + w["mcp_talk_extra_max"] + w["named_people"] + w["community_channel"] + w["contact_route"]
        self.assertEqual(full, 100)
        self.assertLess(w["contact_route_weak"], w["contact_route"])

    def test_a_full_set_of_sourced_signals_is_posted_with_the_parts_of_its_score(self):
        r = judge()
        self.assertEqual(r["decision"], "post")
        self.assertEqual(r["score"], 30 + 15 + 25 + 10 + 5 + 10)
        self.assertEqual(r["parts"]["mcp_talk"], 25)
        self.assertIn("links not re-checked", r["reason"])
        self.assertEqual(r["route"]["url"], U + "devrel")

    def test_extra_talks_stop_counting_at_the_cap(self):
        r = judge(signals=[sig("mcp_docs")] + [sig("mcp_talk", i) for i in range(9)])
        self.assertEqual(r["parts"]["mcp_talk"], RULE["weights"]["mcp_talk"] + RULE["weights"]["mcp_talk_extra_max"])

    def test_no_sourced_page_for_the_companys_own_mcp_means_nothing_else_is_counted(self):
        r = judge(signals=[sig("devrel_team"), sig("mcp_talk")])
        self.assertEqual(r["decision"], "not-mcp")

    def test_a_signal_without_an_https_link_counts_for_nothing(self):
        r = judge(signals=[{"kind": "mcp_docs", "url": "http://example.test/mcp"}, {"kind": "mcp_docs", "url": ""}, {"kind": "mcp_docs"}])
        self.assertEqual(r["decision"], "not-mcp")

    def test_a_company_with_no_public_route_is_held_back_however_high_its_score(self):
        r = judge(contact_route={})
        self.assertEqual(r["decision"], "unstated")
        self.assertIn("no public contact route", r["reason"])
        self.assertEqual(judge(contact_route={"kind": "private-email", "url": U + "x"})["decision"], "unstated")     # a kind that is not on the list is not a route

    def test_a_thin_company_is_held_back_below_the_minimum_score(self):
        r = judge(signals=[sig("mcp_docs")], people_found=0)
        self.assertEqual((r["decision"], r["score"]), ("unstated", 40))
        self.assertIn("below 60", r["reason"])

    def test_the_minimum_is_a_setting_not_a_constant(self):
        kw = copy.deepcopy(KW)
        kw["speakers_rule"]["min_score"] = 40
        v, rec = lead(signals=[sig("mcp_docs")], people_found=0)
        self.assertEqual(sj.judge_speaker(v, rec, kw)["decision"], "post")

    def test_a_dropped_company_is_rejected_with_the_researchs_reason(self):
        r = judge(verdict="drop", why="only a third-party server exists")
        self.assertEqual(r["decision"], "rejected")
        self.assertIn("third-party", r["reason"])

    def test_when_links_were_rechecked_only_those_that_answered_2xx_count(self):
        checks = {U + "mcp_docs/1": {"status": "200"}, U + "devrel": {"status": "200"}, U + "devrel_team/1": {"status": "404"}, U + "mcp_talk/1": {"status": "robots"}}
        r = judge(checks=checks)
        self.assertEqual(sorted(r["parts"]), ["contact_route", "mcp_docs", "named_people"])
        self.assertNotIn("links not re-checked", r["reason"])
        self.assertEqual(judge(checks={U + "mcp_docs/1": {"status": "403"}, U + "devrel": {"status": "200"}})["decision"], "not-mcp")
        self.assertEqual(judge(checks={U + "mcp_docs/1": {"status": "200"}})["decision"], "unstated")                     # route not re-checked: no route

    def test_a_community_forum_is_a_route_but_a_weaker_one_than_a_devrel_page(self):
        strong, weak = judge(), judge(contact_route={"kind": "community-page", "url": U + "forum"})
        self.assertEqual((strong["parts"]["contact_route"], weak["parts"]["contact_route"]), (10, 5))
        self.assertEqual(weak["decision"], "post")
        self.assertEqual(judge(contact_route={"kind": "partnerships-form", "url": U + "p"})["parts"]["contact_route"], 10)

    def test_a_page_that_turned_the_script_away_counts_only_if_the_researcher_opened_it_and_a_404_never_counts(self):
        opened = {"kind": "mcp_docs", "url": U + "mcp_docs/1", "opened": True}
        unopened = {"kind": "mcp_docs", "url": U + "mcp_docs/1"}
        route = {U + "devrel": {"status": "200"}}
        for status, sig_, expect in (("403", opened, "post"), ("robots", opened, "post"), ("403", unopened, "not-mcp"), ("404", opened, "not-mcp"), ("410", opened, "not-mcp"), ("429", opened, "post")):
            r = judge(signals=[sig_, sig("devrel_team"), sig("mcp_talk")], checks={U + "mcp_docs/1": {"status": status}, **route, U + "devrel_team/1": {"status": "200"}, U + "mcp_talk/1": {"status": "200"}})
            self.assertEqual(r["decision"], expect, (status, sig_))

    def test_a_company_with_an_open_question_is_held_back_not_scored(self):
        r = judge(verdict="to-do", todo="decide whether a foundation project fits")
        self.assertEqual(r["decision"], "unstated")
        self.assertIn("waiting for a decision", r["reason"])
        self.assertIn("foundation", r["reason"])

    def test_people_are_a_count_never_a_name(self):
        v, rec = lead()
        self.assertNotIn("name", json.dumps({k: rec[k] for k in ("people_found",)}))
        self.assertEqual(sj.lead_view(rec)["location_text"], "")


if __name__ == "__main__":
    unittest.main()
