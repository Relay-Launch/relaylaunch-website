"""Media inspection utilities for GIMP CLI."""

import os

try:
    from PIL import Image, ExifTags
    HAS_PILLOW = True
except ImportError:
    HAS_PILLOW = False


def probe_image(path):
    """Read image metadata: dimensions, DPI, EXIF, format."""
    if not os.path.isfile(path):
        return {"ok": False, "error": f"File not found: {path}"}
    if not HAS_PILLOW:
        return {"ok": False, "error": "Pillow not installed"}
    img = Image.open(path)
    info = {
        "path": os.path.abspath(path),
        "format": img.format,
        "mode": img.mode,
        "width": img.width,
        "height": img.height,
        "dpi": img.info.get("dpi", (72, 72)),
        "file_size": os.path.getsize(path),
        "is_animated": getattr(img, "is_animated", False),
        "n_frames": getattr(img, "n_frames", 1),
    }
    exif_data = {}
    try:
        raw_exif = img._getexif()
        if raw_exif:
            for tag_id, value in raw_exif.items():
                tag = ExifTags.TAGS.get(tag_id, tag_id)
                if isinstance(value, (str, int, float)):
                    exif_data[tag] = value
    except (AttributeError, Exception):
        pass
    info["exif"] = exif_data
    img.close()
    return {"ok": True, "info": info}


def list_media_in_project(project):
    """List all media files referenced by layers."""
    media = []
    for layer in project.get("layers", []):
        src = layer.get("source")
        if src:
            exists = os.path.isfile(src)
            media.append({
                "layer_id": layer["id"],
                "layer_name": layer["name"],
                "source": src,
                "exists": exists,
            })
    return {"ok": True, "media": media, "count": len(media)}


def check_media(project):
    """Validate all media references exist."""
    missing = []
    for layer in project.get("layers", []):
        src = layer.get("source")
        if src and not os.path.isfile(src):
            missing.append({"layer_id": layer["id"], "source": src})
    return {
        "ok": len(missing) == 0,
        "missing": missing,
        "total_layers": len(project.get("layers", [])),
    }


def get_image_histogram(path):
    """Get color histogram for an image."""
    if not os.path.isfile(path):
        return {"ok": False, "error": f"File not found: {path}"}
    if not HAS_PILLOW:
        return {"ok": False, "error": "Pillow not installed"}
    img = Image.open(path).convert("RGB")
    hist = img.histogram()
    img.close()
    return {
        "ok": True,
        "histogram": {
            "red": hist[0:256],
            "green": hist[256:512],
            "blue": hist[512:768],
        },
    }
