"""Tests for canvas operations."""

import pytest

from cli_anything.gimp.core.canvas import (
    resize_canvas, scale_canvas, crop_canvas,
    set_mode, set_dpi, get_canvas_info,
)


@pytest.fixture
def project():
    return {
        "name": "test",
        "canvas": {"width": 800, "height": 600, "dpi": 72, "mode": "RGB"},
        "layers": [
            {"id": "l1", "name": "BG", "offset_x": 0, "offset_y": 0},
        ],
        "filters": [],
    }


class TestResizeCanvas:
    def test_resize_center(self, project):
        result = resize_canvas(project, 1000, 800, "center")
        assert result["ok"]
        assert project["canvas"]["width"] == 1000
        assert project["canvas"]["height"] == 800

    def test_resize_top_left(self, project):
        result = resize_canvas(project, 1000, 800, "top-left")
        assert result["ok"]
        assert result["offset"]["x"] == 0
        assert result["offset"]["y"] == 0

    def test_invalid_anchor(self, project):
        result = resize_canvas(project, 1000, 800, "invalid")
        assert not result["ok"]


class TestScaleCanvas:
    def test_scale(self, project):
        result = scale_canvas(project, 1600, 1200)
        assert result["ok"]
        assert result["scale"]["x"] == 2.0
        assert result["scale"]["y"] == 2.0


class TestCropCanvas:
    def test_crop(self, project):
        result = crop_canvas(project, 100, 100, 500, 400)
        assert result["ok"]
        assert project["canvas"]["width"] == 400
        assert project["canvas"]["height"] == 300

    def test_invalid_crop(self, project):
        result = crop_canvas(project, 500, 400, 100, 100)
        assert not result["ok"]


class TestSetMode:
    def test_valid_mode(self, project):
        result = set_mode(project, "RGBA")
        assert result["ok"]
        assert project["canvas"]["mode"] == "RGBA"

    def test_invalid_mode(self, project):
        result = set_mode(project, "INVALID")
        assert not result["ok"]


class TestSetDpi:
    def test_valid_dpi(self, project):
        result = set_dpi(project, 300)
        assert result["ok"]
        assert project["canvas"]["dpi"] == 300

    def test_invalid_dpi(self, project):
        result = set_dpi(project, 0)
        assert not result["ok"]


class TestGetCanvasInfo:
    def test_info(self, project):
        result = get_canvas_info(project)
        assert result["ok"]
        assert result["canvas"]["width"] == 800
