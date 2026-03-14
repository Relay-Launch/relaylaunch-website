"""Session management with undo/redo state tracking."""

import copy
import json
import os
from datetime import datetime, timezone


class Session:
    """Manages project state with undo/redo history."""

    MAX_UNDO = 50

    def __init__(self):
        self.project = None
        self.project_path = None
        self.undo_stack = []
        self.redo_stack = []
        self.created_at = datetime.now(timezone.utc).isoformat()

    def snapshot(self, description=""):
        """Save current state to undo stack."""
        if self.project is None:
            return
        if len(self.undo_stack) >= self.MAX_UNDO:
            self.undo_stack.pop(0)
        self.undo_stack.append({
            "state": copy.deepcopy(self.project),
            "description": description,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        })
        self.redo_stack.clear()

    def undo(self):
        """Restore previous state."""
        if not self.undo_stack:
            return {"ok": False, "error": "Nothing to undo"}
        entry = self.undo_stack.pop()
        self.redo_stack.append({
            "state": copy.deepcopy(self.project),
            "description": f"undo: {entry['description']}",
            "timestamp": datetime.now(timezone.utc).isoformat(),
        })
        self.project = entry["state"]
        return {"ok": True, "restored": entry["description"]}

    def redo(self):
        """Re-apply undone state."""
        if not self.redo_stack:
            return {"ok": False, "error": "Nothing to redo"}
        entry = self.redo_stack.pop()
        self.undo_stack.append({
            "state": copy.deepcopy(self.project),
            "description": f"redo: {entry['description']}",
            "timestamp": datetime.now(timezone.utc).isoformat(),
        })
        self.project = entry["state"]
        return {"ok": True, "restored": entry["description"]}

    def save_session(self, path=None):
        """Persist session state to JSON file."""
        path = path or self.project_path
        if not path:
            return {"ok": False, "error": "No project path set"}
        data = {
            "version": "1.0.0",
            "created_at": self.created_at,
            "project": self.project,
        }
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        with open(path, "w") as f:
            json.dump(data, f, indent=2)
        return {"ok": True, "path": path}

    def load_session(self, path):
        """Load session state from JSON file."""
        with open(path) as f:
            data = json.load(f)
        self.project = data.get("project")
        self.project_path = path
        self.created_at = data.get("created_at", self.created_at)
        return {"ok": True, "path": path}

    def list_history(self):
        """Return undo stack descriptions."""
        return [
            {"index": i, "description": e["description"], "timestamp": e["timestamp"]}
            for i, e in enumerate(self.undo_stack)
        ]
