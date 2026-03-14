"""Tests for filter management."""

import pytest

from cli_anything.gimp.core.filters import (
    validate_params, add_filter, remove_filter,
    set_filter_param, list_filters, FILTER_REGISTRY,
)


@pytest.fixture
def project():
    return {
        "name": "test",
        "canvas": {"width": 800, "height": 600},
        "layers": [
            {"id": "layer1", "name": "Test Layer", "filters": []},
        ],
        "filters": [],
    }


class TestValidateParams:
    def test_valid_params(self):
        result = validate_params("brightness", {"factor": 1.5})
        assert result["ok"]
        assert result["params"]["factor"] == 1.5

    def test_clamps_values(self):
        result = validate_params("brightness", {"factor": 10.0})
        assert result["params"]["factor"] == 3.0

    def test_unknown_filter(self):
        result = validate_params("nonexistent", {})
        assert not result["ok"]

    def test_default_params(self):
        result = validate_params("brightness", {})
        assert result["params"]["factor"] == 1.0


class TestAddFilter:
    def test_add_to_canvas(self, project):
        result = add_filter(project, "brightness", factor=1.5)
        assert result["ok"]
        assert result["target"] == "canvas"
        assert len(project["filters"]) == 1

    def test_add_to_layer(self, project):
        result = add_filter(project, "gaussian_blur", "layer", "layer1", radius=3)
        assert result["ok"]
        assert result["target"] == "layer:layer1"
        assert len(project["layers"][0]["filters"]) == 1

    def test_unknown_filter(self, project):
        result = add_filter(project, "nonexistent")
        assert not result["ok"]

    def test_layer_not_found(self, project):
        result = add_filter(project, "brightness", "layer", "missing")
        assert not result["ok"]


class TestRemoveFilter:
    def test_remove_canvas_filter(self, project):
        add_result = add_filter(project, "contrast", factor=1.2)
        fid = add_result["filter"]["id"]
        result = remove_filter(project, fid)
        assert result["ok"]
        assert len(project["filters"]) == 0

    def test_remove_layer_filter(self, project):
        add_result = add_filter(project, "brightness", "layer", "layer1", factor=1.5)
        fid = add_result["filter"]["id"]
        result = remove_filter(project, fid, "layer1")
        assert result["ok"]

    def test_remove_missing(self, project):
        result = remove_filter(project, "missing")
        assert not result["ok"]


class TestSetFilterParam:
    def test_set_param(self, project):
        add_result = add_filter(project, "brightness", factor=1.0)
        fid = add_result["filter"]["id"]
        result = set_filter_param(project, fid, "factor", 2.0)
        assert result["ok"]
        assert result["filter"]["params"]["factor"] == 2.0

    def test_clamps_param(self, project):
        add_result = add_filter(project, "brightness", factor=1.0)
        fid = add_result["filter"]["id"]
        result = set_filter_param(project, fid, "factor", 99.0)
        assert result["filter"]["params"]["factor"] == 3.0


class TestListFilters:
    def test_list_available(self):
        result = list_filters()
        assert result["ok"]
        assert "brightness" in result["filters"]
        assert "gaussian_blur" in result["filters"]

    def test_list_by_category(self):
        result = list_filters(category="blur")
        assert all(v["category"] == "blur" for v in result["filters"].values())

    def test_list_project_filters(self, project):
        add_filter(project, "brightness", factor=1.5)
        add_filter(project, "contrast", factor=1.2)
        result = list_filters(project)
        assert result["count"] == 2

    def test_registry_completeness(self):
        assert len(FILTER_REGISTRY) >= 24
        categories = {v["category"] for v in FILTER_REGISTRY.values()}
        assert "adjustment" in categories
        assert "blur" in categories
        assert "stylize" in categories
        assert "transform" in categories
