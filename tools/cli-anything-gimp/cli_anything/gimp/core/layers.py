"""Layer management for GIMP CLI projects."""

import os
import uuid


BLEND_MODES = [
    "normal", "multiply", "screen", "overlay", "darken", "lighten",
    "color_dodge", "color_burn", "hard_light", "soft_light",
    "difference", "exclusion", "hue", "saturation", "luminosity",
]


def add_layer(project, name, layer_type="solid", color="#FFFFFF",
              opacity=1.0, visible=True, position=None):
    """Add a new layer to the project."""
    layer = {
        "id": str(uuid.uuid4())[:8],
        "name": name,
        "type": layer_type,
        "color": color,
        "opacity": max(0.0, min(1.0, opacity)),
        "visible": visible,
        "blend_mode": "normal",
        "filters": [],
        "source": None,
        "offset_x": 0,
        "offset_y": 0,
    }
    layers = project.setdefault("layers", [])
    if position is not None and 0 <= position <= len(layers):
        layers.insert(position, layer)
    else:
        layers.append(layer)
    return {"ok": True, "layer": layer}


def add_from_file(project, path, name=None, opacity=1.0, position=None):
    """Add a layer from an image file."""
    if not os.path.isfile(path):
        return {"ok": False, "error": f"File not found: {path}"}
    layer_name = name or os.path.splitext(os.path.basename(path))[0]
    layer = {
        "id": str(uuid.uuid4())[:8],
        "name": layer_name,
        "type": "image",
        "source": os.path.abspath(path),
        "opacity": max(0.0, min(1.0, opacity)),
        "visible": True,
        "blend_mode": "normal",
        "filters": [],
        "offset_x": 0,
        "offset_y": 0,
    }
    layers = project.setdefault("layers", [])
    if position is not None and 0 <= position <= len(layers):
        layers.insert(position, layer)
    else:
        layers.append(layer)
    return {"ok": True, "layer": layer}


def remove_layer(project, layer_id):
    """Remove a layer by ID."""
    layers = project.get("layers", [])
    for i, layer in enumerate(layers):
        if layer["id"] == layer_id:
            removed = layers.pop(i)
            return {"ok": True, "removed": removed}
    return {"ok": False, "error": f"Layer not found: {layer_id}"}


def duplicate_layer(project, layer_id, new_name=None):
    """Duplicate a layer."""
    layers = project.get("layers", [])
    for i, layer in enumerate(layers):
        if layer["id"] == layer_id:
            import copy
            dup = copy.deepcopy(layer)
            dup["id"] = str(uuid.uuid4())[:8]
            dup["name"] = new_name or f"{layer['name']} (copy)"
            layers.insert(i + 1, dup)
            return {"ok": True, "layer": dup}
    return {"ok": False, "error": f"Layer not found: {layer_id}"}


def move_layer(project, layer_id, position):
    """Move a layer to a new position in the stack."""
    layers = project.get("layers", [])
    for i, layer in enumerate(layers):
        if layer["id"] == layer_id:
            layers.pop(i)
            position = max(0, min(position, len(layers)))
            layers.insert(position, layer)
            return {"ok": True, "layer": layer, "position": position}
    return {"ok": False, "error": f"Layer not found: {layer_id}"}


def set_layer_property(project, layer_id, prop, value):
    """Set a property on a layer."""
    valid_props = {"name", "opacity", "visible", "blend_mode", "offset_x", "offset_y", "color"}
    if prop not in valid_props:
        return {"ok": False, "error": f"Invalid property: {prop}. Valid: {valid_props}"}
    if prop == "blend_mode" and value not in BLEND_MODES:
        return {"ok": False, "error": f"Invalid blend mode: {value}. Valid: {BLEND_MODES}"}
    if prop == "opacity":
        value = max(0.0, min(1.0, float(value)))
    layers = project.get("layers", [])
    for layer in layers:
        if layer["id"] == layer_id:
            layer[prop] = value
            return {"ok": True, "layer": layer}
    return {"ok": False, "error": f"Layer not found: {layer_id}"}


def get_layer(project, layer_id):
    """Get layer details by ID."""
    for layer in project.get("layers", []):
        if layer["id"] == layer_id:
            return {"ok": True, "layer": layer}
    return {"ok": False, "error": f"Layer not found: {layer_id}"}


def list_layers(project):
    """List all layers in the project."""
    layers = project.get("layers", [])
    return {"ok": True, "layers": layers, "count": len(layers)}


def flatten_layers(project):
    """Mark all layers for flattening into a single layer."""
    layers = project.get("layers", [])
    if not layers:
        return {"ok": False, "error": "No layers to flatten"}
    flat = {
        "id": str(uuid.uuid4())[:8],
        "name": "Flattened",
        "type": "flattened",
        "opacity": 1.0,
        "visible": True,
        "blend_mode": "normal",
        "filters": [],
        "source_layers": [l["id"] for l in layers],
        "offset_x": 0,
        "offset_y": 0,
    }
    project["layers"] = [flat]
    return {"ok": True, "layer": flat}


def merge_down(project, layer_id):
    """Merge a layer with the one below it."""
    layers = project.get("layers", [])
    for i, layer in enumerate(layers):
        if layer["id"] == layer_id:
            if i == 0:
                return {"ok": False, "error": "Cannot merge bottom layer down"}
            merged = {
                "id": str(uuid.uuid4())[:8],
                "name": f"{layers[i-1]['name']} + {layer['name']}",
                "type": "merged",
                "opacity": 1.0,
                "visible": True,
                "blend_mode": "normal",
                "filters": [],
                "source_layers": [layers[i-1]["id"], layer["id"]],
                "offset_x": 0,
                "offset_y": 0,
            }
            layers[i-1] = merged
            layers.pop(i)
            return {"ok": True, "layer": merged}
    return {"ok": False, "error": f"Layer not found: {layer_id}"}
