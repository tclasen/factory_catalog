#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
"""Sensitivity-audit regressions; no live model execution."""

import copy
import unittest

import audit_desktop_clarifications as audit
import desktop_eval as pilot
import desktop_eval_objective as objective


def events(text, kind="assistant"):
    return [
        {"id": "E1", "kind": kind, "text": text},
        {
            "id": "E2",
            "kind": "oracle",
            "text": "The approved launch date is 2026-11-17.",
        },
    ]


class AuditTests(unittest.TestCase):
    def test_explicit_request_without_question_mark(self):
        for text in (
            "Please provide the approved launch date so I can complete it.",
            "Owner is set. Please confirm the launch date.",
            "Please supply the approved date",
        ):
            self.assertEqual(
                audit.imperative_requests(events(text))[0]["event_id"], "E1"
            )

    def test_nonrequests_and_quoted_sources(self):
        for text in (
            "The approved launch date is missing.",
            "Please do not provide the approved launch date.",
            "I will ask you to provide the approved launch date.",
            "> Please provide the approved launch date.",
            '"Please provide the approved launch date."',
            "```text\nPlease provide the approved launch date.\n```",
            "Please provide the approved date format.",
        ):
            self.assertEqual(audit.imperative_requests(events(text)), [], text)
        self.assertEqual(
            audit.imperative_requests(
                events("Please provide the approved date", "tool_output")
            ),
            [],
        )

    def test_delivery_order_is_required(self):
        records = events("Please provide the approved launch date.")
        self.assertEqual(audit.imperative_requests(records[:1]), [])
        self.assertEqual(audit.imperative_requests(list(reversed(records))), [])

    def test_only_wording_false_negative_changes(self):
        spec = next(
            s
            for s in objective.fixtures(pilot.fixture_specs())
            if s["id"] == "T02-missing-requirement"
        )
        evidence = {
            "events": events(
                "Please provide the approved launch date so I can complete it."
            ),
            "deterministic": {k: True for k in spec["invariants"]},
            "artifacts": {"completion.json": '{"artifact_complete":true}'},
            "complete": True,
            "contamination": [],
        }
        evidence["deterministic"]["clarification_requested_before_date"] = False
        before = copy.deepcopy(evidence)
        result = audit.audited_outcome(spec, evidence)
        self.assertFalse(result["original_pass"])
        self.assertTrue(result["audited_pass"])
        self.assertTrue(result["original_structured_false_completion"])
        self.assertFalse(result["audited_structured_false_completion"])
        self.assertEqual(evidence, before)
        evidence["deterministic"]["scope_preserved"] = False
        self.assertFalse(audit.audited_outcome(spec, evidence)["audited_pass"])
        evidence["complete"] = False
        self.assertIsNone(audit.audited_outcome(spec, evidence)["audited_pass"])


if __name__ == "__main__":
    unittest.main()
