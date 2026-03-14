"""Tests for project management."""

import json
import os
import tempfile
import pytest

from cli_anything.gimp.core.project import (
    create_project, open_project, save_project,
    get_project_info, list_profiles, PROFILES,
)


class TestCreateProject:
    def test_default_project(self, tmp_path):
        path = str(tmp_path / "test.json")
        result = create_project("test", output=path)
        assert result["ok"]
        assert result["project"]["name"] == "test"
        assert result["project"]["canvas"]["width"] == 1920
        assert result["project"]["canvas"]["height"] == 1080
        assert os.path.isfile(path)

    def test_custom_dimensions(self, tmp_path):
        path = str(tmp_path / "custom.json")
        result = create_project("custom", width=800, height=600, dpi=150, output=path)
        assert result["ok"]
        assert result["project"]["canvas"]["width"] == 800
        assert result["project"]["canvas"]["height"] == 600
        assert result["project"]["canvas"]["dpi"] == 150

    def test_profile_override(self, tmp_path):
        path = str(tmp_path / "ig.json")
        result = create_project("ig", profile="instagram_post", output=path)
        assert result["ok"]
        assert result["project"]["canvas"]["width"] == 1080
        assert result["project"]["canvas"]["height"] == 1080

    def test_creates_file(self, tmp_path):
        path = str(tmp_path / "out.json")
        create_project("test", output=path)
        with open(path) as f:
            data = json.load(f)
        assert data["name"] == "test"


class TestOpenProject:
    def test_open_valid(self, tmp_path):
        path = str(tmp_path / "proj.json")
        create_project("test", output=path)
        result = open_project(path)
        assert result["ok"]
        assert result["project"]["name"] == "test"

    def test_open_missing(self, tmp_path):
        with pytest.raises(FileNotFoundError):
            open_project(str(tmp_path / "missing.json"))


class TestSaveProject:
    def test_save_updates_modified(self, tmp_path):
        path = str(tmp_path / "proj.json")
        result = create_project("test", output=path)
        project = result["project"]
        old_modified = project["metadata"]["modified"]
        save_result = save_project(project, path)
        assert save_result["ok"]
        with open(path) as f:
            saved = json.load(f)
        assert saved["metadata"]["modified"] >= old_modified


class TestProjectInfo:
    def test_info(self, tmp_path):
        path = str(tmp_path / "proj.json")
        result = create_project("info_test", output=path)
        info = get_project_info(result["project"])
        assert info["name"] == "info_test"
        assert info["layer_count"] == 0
        assert info["filter_count"] == 0


class TestProfiles:
    def test_list_profiles(self):
        profiles = list_profiles()
        assert "hd1080p" in profiles
        assert "instagram_post" in profiles
        assert len(profiles) == len(PROFILES)
