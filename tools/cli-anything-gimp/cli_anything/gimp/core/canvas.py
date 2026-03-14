"""Canvas manipulation for GIMP CLI projects."""


ANCHOR_MAP = {
    "center": (0.5, 0.5),
    "top-left": (0.0, 0.0),
    "top": (0.5, 0.0),
    "top-right": (1.0, 0.0),
    "left": (0.0, 0.5),
    "right": (1.0, 0.5),
    "bottom-left": (0.0, 1.0),
    "bottom": (0.5, 1.0),
    "bottom-right": (1.0, 1.0),
}


def resize_canvas(project, width, height, anchor="center"):
    """Resize canvas with anchor positioning."""
    if anchor not in ANCHOR_MAP:
        return {"ok": False, "error": f"Invalid anchor: {anchor}. Valid: {list(ANCHOR_MAP.keys())}"}
    old_w = project["canvas"]["width"]
    old_h = project["canvas"]["height"]
    ax, ay = ANCHOR_MAP[anchor]
    offset_x = int((width - old_w) * ax)
    offset_y = int((height - old_h) * ay)
    project["canvas"]["width"] = width
    project["canvas"]["height"] = height
    for layer in project.get("layers", []):
        layer["offset_x"] = layer.get("offset_x", 0) + offset_x
        layer["offset_y"] = layer.get("offset_y", 0) + offset_y
    return {
        "ok": True,
        "canvas": project["canvas"],
        "offset": {"x": offset_x, "y": offset_y},
    }


def scale_canvas(project, width, height):
    """Scale canvas and mark layers for proportional scaling."""
    old_w = project["canvas"]["width"]
    old_h = project["canvas"]["height"]
    scale_x = width / old_w if old_w else 1
    scale_y = height / old_h if old_h else 1
    project["canvas"]["width"] = width
    project["canvas"]["height"] = height
    for layer in project.get("layers", []):
        layer["_scale_x"] = scale_x
        layer["_scale_y"] = scale_y
        layer["offset_x"] = int(layer.get("offset_x", 0) * scale_x)
        layer["offset_y"] = int(layer.get("offset_y", 0) * scale_y)
    return {"ok": True, "canvas": project["canvas"], "scale": {"x": scale_x, "y": scale_y}}


def crop_canvas(project, left, top, right, bottom):
    """Crop canvas to a bounding box."""
    if right <= left or bottom <= top:
        return {"ok": False, "error": "Invalid crop region"}
    project["canvas"]["width"] = right - left
    project["canvas"]["height"] = bottom - top
    for layer in project.get("layers", []):
        layer["offset_x"] = layer.get("offset_x", 0) - left
        layer["offset_y"] = layer.get("offset_y", 0) - top
    return {"ok": True, "canvas": project["canvas"]}


def set_mode(project, mode):
    """Set canvas color mode (RGB, RGBA, L, CMYK)."""
    valid = {"RGB", "RGBA", "L", "CMYK"}
    if mode not in valid:
        return {"ok": False, "error": f"Invalid mode: {mode}. Valid: {valid}"}
    project["canvas"]["mode"] = mode
    return {"ok": True, "canvas": project["canvas"]}


def set_dpi(project, dpi):
    """Set canvas DPI."""
    if dpi < 1 or dpi > 9600:
        return {"ok": False, "error": "DPI must be between 1 and 9600"}
    project["canvas"]["dpi"] = dpi
    return {"ok": True, "canvas": project["canvas"]}


def get_canvas_info(project):
    """Return canvas details."""
    return {"ok": True, "canvas": project.get("canvas", {})}
