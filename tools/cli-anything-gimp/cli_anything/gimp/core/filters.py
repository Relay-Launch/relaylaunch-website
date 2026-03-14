"""Filter registry and management for GIMP CLI."""

import uuid


FILTER_REGISTRY = {
    # Adjustments
    "brightness": {
        "category": "adjustment", "engine": "enhance",
        "params": {"factor": {"type": "float", "default": 1.0, "min": 0.0, "max": 3.0}},
    },
    "contrast": {
        "category": "adjustment", "engine": "enhance",
        "params": {"factor": {"type": "float", "default": 1.0, "min": 0.0, "max": 3.0}},
    },
    "saturation": {
        "category": "adjustment", "engine": "enhance",
        "params": {"factor": {"type": "float", "default": 1.0, "min": 0.0, "max": 3.0}},
    },
    "sharpness": {
        "category": "adjustment", "engine": "enhance",
        "params": {"factor": {"type": "float", "default": 1.0, "min": 0.0, "max": 3.0}},
    },
    "autocontrast": {
        "category": "adjustment", "engine": "ops",
        "params": {"cutoff": {"type": "float", "default": 0.0, "min": 0.0, "max": 50.0}},
    },
    "equalize": {
        "category": "adjustment", "engine": "ops",
        "params": {},
    },
    "invert": {
        "category": "adjustment", "engine": "ops",
        "params": {},
    },
    "posterize": {
        "category": "adjustment", "engine": "ops",
        "params": {"bits": {"type": "int", "default": 4, "min": 1, "max": 8}},
    },
    "solarize": {
        "category": "adjustment", "engine": "ops",
        "params": {"threshold": {"type": "int", "default": 128, "min": 0, "max": 255}},
    },
    "grayscale": {
        "category": "adjustment", "engine": "ops",
        "params": {},
    },
    "sepia": {
        "category": "adjustment", "engine": "custom",
        "params": {"intensity": {"type": "float", "default": 0.8, "min": 0.0, "max": 1.0}},
    },
    # Blur
    "gaussian_blur": {
        "category": "blur", "engine": "filter",
        "params": {"radius": {"type": "int", "default": 2, "min": 0, "max": 100}},
    },
    "box_blur": {
        "category": "blur", "engine": "filter",
        "params": {"radius": {"type": "int", "default": 2, "min": 0, "max": 100}},
    },
    "unsharp_mask": {
        "category": "blur", "engine": "filter",
        "params": {
            "radius": {"type": "int", "default": 2, "min": 0, "max": 100},
            "percent": {"type": "int", "default": 150, "min": 0, "max": 500},
            "threshold": {"type": "int", "default": 3, "min": 0, "max": 255},
        },
    },
    "smooth": {
        "category": "blur", "engine": "filter",
        "params": {},
    },
    # Stylize
    "find_edges": {
        "category": "stylize", "engine": "filter",
        "params": {},
    },
    "emboss": {
        "category": "stylize", "engine": "filter",
        "params": {},
    },
    "contour": {
        "category": "stylize", "engine": "filter",
        "params": {},
    },
    "detail": {
        "category": "stylize", "engine": "filter",
        "params": {},
    },
    # Transform
    "rotate": {
        "category": "transform", "engine": "transform",
        "params": {"angle": {"type": "float", "default": 90.0, "min": -360.0, "max": 360.0}},
    },
    "flip_h": {
        "category": "transform", "engine": "transform",
        "params": {},
    },
    "flip_v": {
        "category": "transform", "engine": "transform",
        "params": {},
    },
    "resize": {
        "category": "transform", "engine": "transform",
        "params": {
            "width": {"type": "int", "default": 800, "min": 1, "max": 65535},
            "height": {"type": "int", "default": 600, "min": 1, "max": 65535},
        },
    },
    "crop": {
        "category": "transform", "engine": "transform",
        "params": {
            "left": {"type": "int", "default": 0, "min": 0, "max": 65535},
            "top": {"type": "int", "default": 0, "min": 0, "max": 65535},
            "right": {"type": "int", "default": 800, "min": 1, "max": 65535},
            "bottom": {"type": "int", "default": 600, "min": 1, "max": 65535},
        },
    },
}


def validate_params(filter_name, params):
    """Validate filter parameters against the registry."""
    if filter_name not in FILTER_REGISTRY:
        return {"ok": False, "error": f"Unknown filter: {filter_name}"}
    spec = FILTER_REGISTRY[filter_name]["params"]
    validated = {}
    for key, meta in spec.items():
        val = params.get(key, meta["default"])
        if meta["type"] == "float":
            val = max(meta["min"], min(meta["max"], float(val)))
        elif meta["type"] == "int":
            val = max(meta["min"], min(meta["max"], int(val)))
        validated[key] = val
    return {"ok": True, "params": validated}


def add_filter(project, filter_name, target="canvas", layer_id=None, **params):
    """Add a filter to the project or a specific layer."""
    if filter_name not in FILTER_REGISTRY:
        return {"ok": False, "error": f"Unknown filter: {filter_name}"}
    result = validate_params(filter_name, params)
    if not result["ok"]:
        return result
    entry = {
        "id": str(uuid.uuid4())[:8],
        "filter": filter_name,
        "category": FILTER_REGISTRY[filter_name]["category"],
        "params": result["params"],
        "enabled": True,
    }
    if target == "layer" and layer_id:
        for layer in project.get("layers", []):
            if layer["id"] == layer_id:
                layer.setdefault("filters", []).append(entry)
                return {"ok": True, "filter": entry, "target": f"layer:{layer_id}"}
        return {"ok": False, "error": f"Layer not found: {layer_id}"}
    else:
        project.setdefault("filters", []).append(entry)
        return {"ok": True, "filter": entry, "target": "canvas"}


def remove_filter(project, filter_id, layer_id=None):
    """Remove a filter by ID."""
    if layer_id:
        for layer in project.get("layers", []):
            if layer["id"] == layer_id:
                for i, f in enumerate(layer.get("filters", [])):
                    if f["id"] == filter_id:
                        return {"ok": True, "removed": layer["filters"].pop(i)}
                return {"ok": False, "error": f"Filter not found: {filter_id}"}
    for i, f in enumerate(project.get("filters", [])):
        if f["id"] == filter_id:
            return {"ok": True, "removed": project["filters"].pop(i)}
    return {"ok": False, "error": f"Filter not found: {filter_id}"}


def set_filter_param(project, filter_id, param, value, layer_id=None):
    """Update a parameter on an existing filter."""
    sources = []
    if layer_id:
        for layer in project.get("layers", []):
            if layer["id"] == layer_id:
                sources = layer.get("filters", [])
                break
    else:
        sources = project.get("filters", [])
    for f in sources:
        if f["id"] == filter_id:
            spec = FILTER_REGISTRY.get(f["filter"], {}).get("params", {})
            if param in spec:
                meta = spec[param]
                if meta["type"] == "float":
                    value = max(meta["min"], min(meta["max"], float(value)))
                elif meta["type"] == "int":
                    value = max(meta["min"], min(meta["max"], int(value)))
            f["params"][param] = value
            return {"ok": True, "filter": f}
    return {"ok": False, "error": f"Filter not found: {filter_id}"}


def list_filters(project=None, category=None):
    """List available filters or filters applied to a project."""
    if project is None:
        filters = FILTER_REGISTRY
        if category:
            filters = {k: v for k, v in filters.items() if v["category"] == category}
        return {"ok": True, "filters": filters}
    applied = project.get("filters", [])
    if category:
        applied = [f for f in applied if f["category"] == category]
    return {"ok": True, "filters": applied, "count": len(applied)}
