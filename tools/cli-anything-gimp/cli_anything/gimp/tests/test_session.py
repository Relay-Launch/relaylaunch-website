"""Tests for session management."""

import os
import pytest

from cli_anything.gimp.core.session import Session


class TestSession:
    def test_snapshot_and_undo(self):
        s = Session()
        s.project = {"value": 1}
        s.snapshot("set to 1")
        s.project = {"value": 2}
        result = s.undo()
        assert result["ok"]
        assert s.project["value"] == 1

    def test_redo(self):
        s = Session()
        s.project = {"value": 1}
        s.snapshot("set to 1")
        s.project = {"value": 2}
        s.snapshot("set to 2")
        s.undo()
        result = s.redo()
        assert result["ok"]
        assert s.project["value"] == 2

    def test_undo_empty(self):
        s = Session()
        result = s.undo()
        assert not result["ok"]

    def test_redo_empty(self):
        s = Session()
        result = s.redo()
        assert not result["ok"]

    def test_max_undo(self):
        s = Session()
        s.project = {"value": 0}
        for i in range(60):
            s.snapshot(f"step {i}")
            s.project = {"value": i + 1}
        assert len(s.undo_stack) == Session.MAX_UNDO

    def test_snapshot_clears_redo(self):
        s = Session()
        s.project = {"value": 1}
        s.snapshot("v1")
        s.project = {"value": 2}
        s.snapshot("v2")
        s.undo()
        assert len(s.redo_stack) == 1
        s.snapshot("v3")
        assert len(s.redo_stack) == 0

    def test_save_and_load(self, tmp_path):
        s = Session()
        s.project = {"name": "test", "value": 42}
        s.project_path = str(tmp_path / "session.json")
        result = s.save_session()
        assert result["ok"]
        assert os.path.isfile(s.project_path)

        s2 = Session()
        result = s2.load_session(s.project_path)
        assert result["ok"]
        assert s2.project["value"] == 42

    def test_list_history(self):
        s = Session()
        s.project = {"value": 1}
        s.snapshot("action 1")
        s.snapshot("action 2")
        history = s.list_history()
        assert len(history) == 2
        assert history[0]["description"] == "action 1"
