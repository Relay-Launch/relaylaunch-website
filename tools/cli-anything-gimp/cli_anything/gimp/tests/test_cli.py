"""End-to-end tests for GIMP CLI commands."""

import json
import os
import pytest
from click.testing import CliRunner

from cli_anything.gimp.gimp_cli import main


@pytest.fixture
def runner():
    return CliRunner()


@pytest.fixture
def project_file(tmp_path):
    return str(tmp_path / "test_project.json")


class TestProjectCommands:
    def test_new_project(self, runner, project_file):
        result = runner.invoke(main, ["--json", "project", "new", "--name", "test", "-o", project_file])
        assert result.exit_code == 0
        data = json.loads(result.output)
        assert data["ok"]
        assert data["project"]["name"] == "test"

    def test_new_project_with_profile(self, runner, project_file):
        result = runner.invoke(main, ["--json", "project", "new", "--profile", "instagram_post", "-o", project_file])
        assert result.exit_code == 0
        data = json.loads(result.output)
        assert data["project"]["canvas"]["width"] == 1080
        assert data["project"]["canvas"]["height"] == 1080

    def test_project_info(self, runner, project_file):
        runner.invoke(main, ["project", "new", "-o", project_file])
        result = runner.invoke(main, ["--json", "-p", project_file, "project", "info"])
        assert result.exit_code == 0

    def test_list_profiles(self, runner):
        result = runner.invoke(main, ["--json", "project", "profiles"])
        assert result.exit_code == 0
        data = json.loads(result.output)
        assert "hd1080p" in data["profiles"]


class TestLayerCommands:
    def test_add_layer(self, runner, project_file):
        runner.invoke(main, ["project", "new", "-o", project_file])
        result = runner.invoke(main, [
            "--json", "-p", project_file,
            "layer", "add", "-n", "Background", "--type", "solid", "--color", "#000000"
        ])
        assert result.exit_code == 0
        data = json.loads(result.output)
        assert data["ok"]
        assert data["layer"]["name"] == "Background"

    def test_list_layers(self, runner, project_file):
        runner.invoke(main, ["project", "new", "-o", project_file])
        runner.invoke(main, ["-p", project_file, "layer", "add", "-n", "L1"])
        runner.invoke(main, ["-p", project_file, "layer", "add", "-n", "L2"])
        result = runner.invoke(main, ["--json", "-p", project_file, "layer", "list"])
        assert result.exit_code == 0
        data = json.loads(result.output)
        assert data["count"] == 2


class TestFilterCommands:
    def test_add_filter(self, runner, project_file):
        runner.invoke(main, ["project", "new", "-o", project_file])
        result = runner.invoke(main, [
            "--json", "-p", project_file,
            "filter", "add", "brightness", "-p", "factor=1.5"
        ])
        assert result.exit_code == 0
        data = json.loads(result.output)
        assert data["ok"]
        assert data["filter"]["filter"] == "brightness"

    def test_list_available_filters(self, runner):
        result = runner.invoke(main, ["--json", "filter", "list", "--available"])
        assert result.exit_code == 0
        data = json.loads(result.output)
        assert "brightness" in data["filters"]


class TestCanvasCommands:
    def test_canvas_info(self, runner, project_file):
        runner.invoke(main, ["project", "new", "-o", project_file])
        result = runner.invoke(main, ["--json", "-p", project_file, "canvas", "info"])
        assert result.exit_code == 0
        data = json.loads(result.output)
        assert data["canvas"]["width"] == 1920

    def test_canvas_dpi(self, runner, project_file):
        runner.invoke(main, ["project", "new", "-o", project_file])
        result = runner.invoke(main, ["--json", "-p", project_file, "canvas", "dpi", "300"])
        assert result.exit_code == 0


class TestExportCommands:
    def test_list_presets(self, runner):
        result = runner.invoke(main, ["--json", "export", "presets"])
        assert result.exit_code == 0
        data = json.loads(result.output)
        assert "png" in data["presets"]
        assert "jpeg-high" in data["presets"]


class TestSessionCommands:
    def test_history(self, runner):
        result = runner.invoke(main, ["--json", "session", "history"])
        assert result.exit_code == 0

    def test_undo_empty(self, runner):
        result = runner.invoke(main, ["--json", "session", "undo"])
        assert result.exit_code == 0


class TestVersionFlag:
    def test_version(self, runner):
        result = runner.invoke(main, ["--version"])
        assert "1.0.0" in result.output
