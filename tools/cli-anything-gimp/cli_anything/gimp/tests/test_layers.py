"""Tests for layer management."""

import pytest

from cli_anything.gimp.core.layers import (
    add_layer, add_from_file, remove_layer, duplicate_layer,
    move_layer, set_layer_property, get_layer, list_layers,
    flatten_layers, merge_down, BLEND_MODES,
)


@pytest.fixture
def project():
    return {
        "name": "test",
        "canvas": {"width": 800, "height": 600, "dpi": 72, "mode": "RGB"},
        "layers": [],
        "filters": [],
    }


class TestAddLayer:
    def test_add_solid(self, project):
        result = add_layer(project, "Background", "solid", "#000000")
        assert result["ok"]
        assert result["layer"]["name"] == "Background"
        assert len(project["layers"]) == 1

    def test_add_with_position(self, project):
        add_layer(project, "Layer 1")
        add_layer(project, "Layer 2")
        add_layer(project, "Middle", position=1)
        assert project["layers"][1]["name"] == "Middle"
        assert len(project["layers"]) == 3

    def test_opacity_clamped(self, project):
        result = add_layer(project, "Test", opacity=1.5)
        assert result["layer"]["opacity"] == 1.0
        result = add_layer(project, "Test2", opacity=-0.5)
        assert result["layer"]["opacity"] == 0.0


class TestRemoveLayer:
    def test_remove_existing(self, project):
        result = add_layer(project, "ToRemove")
        lid = result["layer"]["id"]
        result = remove_layer(project, lid)
        assert result["ok"]
        assert len(project["layers"]) == 0

    def test_remove_missing(self, project):
        result = remove_layer(project, "nonexistent")
        assert not result["ok"]


class TestDuplicateLayer:
    def test_duplicate(self, project):
        result = add_layer(project, "Original")
        lid = result["layer"]["id"]
        dup_result = duplicate_layer(project, lid)
        assert dup_result["ok"]
        assert len(project["layers"]) == 2
        assert dup_result["layer"]["name"] == "Original (copy)"

    def test_duplicate_custom_name(self, project):
        result = add_layer(project, "Original")
        lid = result["layer"]["id"]
        dup_result = duplicate_layer(project, lid, "Custom Name")
        assert dup_result["layer"]["name"] == "Custom Name"


class TestMoveLayer:
    def test_move(self, project):
        add_layer(project, "A")
        result = add_layer(project, "B")
        lid = result["layer"]["id"]
        move_result = move_layer(project, lid, 0)
        assert move_result["ok"]
        assert project["layers"][0]["name"] == "B"


class TestSetLayerProperty:
    def test_set_opacity(self, project):
        result = add_layer(project, "Test")
        lid = result["layer"]["id"]
        result = set_layer_property(project, lid, "opacity", 0.5)
        assert result["ok"]
        assert result["layer"]["opacity"] == 0.5

    def test_set_blend_mode(self, project):
        result = add_layer(project, "Test")
        lid = result["layer"]["id"]
        result = set_layer_property(project, lid, "blend_mode", "multiply")
        assert result["ok"]

    def test_invalid_blend_mode(self, project):
        result = add_layer(project, "Test")
        lid = result["layer"]["id"]
        result = set_layer_property(project, lid, "blend_mode", "invalid")
        assert not result["ok"]

    def test_invalid_property(self, project):
        result = add_layer(project, "Test")
        lid = result["layer"]["id"]
        result = set_layer_property(project, lid, "nonexistent", "val")
        assert not result["ok"]


class TestListLayers:
    def test_empty(self, project):
        result = list_layers(project)
        assert result["ok"]
        assert result["count"] == 0

    def test_with_layers(self, project):
        add_layer(project, "A")
        add_layer(project, "B")
        result = list_layers(project)
        assert result["count"] == 2


class TestFlattenLayers:
    def test_flatten(self, project):
        add_layer(project, "A")
        add_layer(project, "B")
        result = flatten_layers(project)
        assert result["ok"]
        assert len(project["layers"]) == 1
        assert project["layers"][0]["type"] == "flattened"

    def test_flatten_empty(self, project):
        result = flatten_layers(project)
        assert not result["ok"]


class TestMergeDown:
    def test_merge(self, project):
        add_layer(project, "Bottom")
        result = add_layer(project, "Top")
        lid = result["layer"]["id"]
        result = merge_down(project, lid)
        assert result["ok"]
        assert len(project["layers"]) == 1

    def test_merge_bottom_fails(self, project):
        result = add_layer(project, "Bottom")
        lid = result["layer"]["id"]
        result = merge_down(project, lid)
        assert not result["ok"]
