"""Project creation and management with canvas presets."""

import json
import os
from datetime import datetime, timezone


PROFILES = {
    "hd720p": {"width": 1280, "height": 720, "dpi": 72},
    "hd1080p": {"width": 1920, "height": 1080, "dpi": 72},
    "4k": {"width": 3840, "height": 2160, "dpi": 72},
    "instagram_post": {"width": 1080, "height": 1080, "dpi": 72},
    "instagram_story": {"width": 1080, "height": 1920, "dpi": 72},
    "twitter_header": {"width": 1500, "height": 500, "dpi": 72},
    "facebook_cover": {"width": 820, "height": 312, "dpi": 72},
    "youtube_thumbnail": {"width": 1280, "height": 720, "dpi": 72},
    "a4_300dpi": {"width": 2480, "height": 3508, "dpi": 300},
    "a4_150dpi": {"width": 1240, "height": 1754, "dpi": 150},
    "letter_300dpi": {"width": 2550, "height": 3300, "dpi": 300},
    "poster_24x36": {"width": 7200, "height": 10800, "dpi": 300},
    "icon_512": {"width": 512, "height": 512, "dpi": 72},
    "favicon": {"width": 64, "height": 64, "dpi": 72},
}


def create_project(name, width=1920, height=1080, dpi=72, mode="RGB",
                    profile=None, output=None):
    """Create a new project manifest."""
    if profile and profile in PROFILES:
        p = PROFILES[profile]
        width, height, dpi = p["width"], p["height"], p["dpi"]

    project = {
        "name": name,
        "canvas": {
            "width": width,
            "height": height,
            "dpi": dpi,
            "mode": mode,
            "background": "#FFFFFF",
        },
        "layers": [],
        "filters": [],
        "metadata": {
            "created": datetime.now(timezone.utc).isoformat(),
            "modified": datetime.now(timezone.utc).isoformat(),
            "generator": "cli-anything-gimp/1.0.0",
        },
    }

    path = output or f"{name}.json"
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w") as f:
        json.dump(project, f, indent=2)

    return {"ok": True, "project": project, "path": path}


def open_project(path):
    """Open an existing project manifest."""
    with open(path) as f:
        project = json.load(f)
    return {"ok": True, "project": project, "path": path}


def save_project(project, path):
    """Save project manifest to disk."""
    project["metadata"]["modified"] = datetime.now(timezone.utc).isoformat()
    with open(path, "w") as f:
        json.dump(project, f, indent=2)
    return {"ok": True, "path": path}


def get_project_info(project):
    """Return project summary."""
    return {
        "name": project.get("name", "Untitled"),
        "canvas": project.get("canvas", {}),
        "layer_count": len(project.get("layers", [])),
        "filter_count": len(project.get("filters", [])),
        "metadata": project.get("metadata", {}),
    }


def list_profiles():
    """Return all available canvas presets."""
    return {name: prof for name, prof in PROFILES.items()}
