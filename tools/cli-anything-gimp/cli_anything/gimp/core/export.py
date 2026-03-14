"""Export and render pipeline for GIMP CLI projects."""

import os

try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False

try:
    from PIL import Image, ImageEnhance, ImageFilter, ImageOps
    HAS_PILLOW = True
except ImportError:
    HAS_PILLOW = False


EXPORT_PRESETS = {
    "png": {"format": "PNG", "ext": ".png", "params": {}},
    "jpeg-high": {"format": "JPEG", "ext": ".jpg", "params": {"quality": 95}},
    "jpeg-med": {"format": "JPEG", "ext": ".jpg", "params": {"quality": 75}},
    "jpeg-low": {"format": "JPEG", "ext": ".jpg", "params": {"quality": 50}},
    "webp": {"format": "WEBP", "ext": ".webp", "params": {"quality": 85}},
    "webp-lossless": {"format": "WEBP", "ext": ".webp", "params": {"lossless": True}},
    "tiff": {"format": "TIFF", "ext": ".tiff", "params": {}},
    "bmp": {"format": "BMP", "ext": ".bmp", "params": {}},
    "gif": {"format": "GIF", "ext": ".gif", "params": {}},
    "pdf": {"format": "PDF", "ext": ".pdf", "params": {}},
    "ico": {"format": "ICO", "ext": ".ico", "params": {}},
    "png-8bit": {"format": "PNG", "ext": ".png", "params": {"optimize": True}},
    "jpeg-progressive": {"format": "JPEG", "ext": ".jpg", "params": {"quality": 85, "progressive": True}},
}


def _apply_single_filter(img, filter_entry):
    """Apply a single filter to a PIL Image."""
    name = filter_entry["filter"]
    params = filter_entry.get("params", {})
    registry_info = filter_entry.get("_registry", {})
    engine = registry_info.get("engine", "")

    if name == "brightness":
        return ImageEnhance.Brightness(img).enhance(params.get("factor", 1.0))
    elif name == "contrast":
        return ImageEnhance.Contrast(img).enhance(params.get("factor", 1.0))
    elif name == "saturation":
        return ImageEnhance.Color(img).enhance(params.get("factor", 1.0))
    elif name == "sharpness":
        return ImageEnhance.Sharpness(img).enhance(params.get("factor", 1.0))
    elif name == "autocontrast":
        return ImageOps.autocontrast(img, cutoff=params.get("cutoff", 0))
    elif name == "equalize":
        return ImageOps.equalize(img)
    elif name == "invert":
        return ImageOps.invert(img.convert("RGB"))
    elif name == "posterize":
        return ImageOps.posterize(img.convert("RGB"), params.get("bits", 4))
    elif name == "solarize":
        return ImageOps.solarize(img, threshold=params.get("threshold", 128))
    elif name == "grayscale":
        return ImageOps.grayscale(img).convert("RGB")
    elif name == "sepia":
        gray = ImageOps.grayscale(img)
        sepia_r = gray.point(lambda x: min(255, int(x * 1.2)))
        sepia_g = gray.point(lambda x: min(255, int(x * 1.0)))
        sepia_b = gray.point(lambda x: min(255, int(x * 0.8)))
        return Image.merge("RGB", (sepia_r, sepia_g, sepia_b))
    elif name == "gaussian_blur":
        return img.filter(ImageFilter.GaussianBlur(radius=params.get("radius", 2)))
    elif name == "box_blur":
        return img.filter(ImageFilter.BoxBlur(radius=params.get("radius", 2)))
    elif name == "unsharp_mask":
        return img.filter(ImageFilter.UnsharpMask(
            radius=params.get("radius", 2),
            percent=params.get("percent", 150),
            threshold=params.get("threshold", 3),
        ))
    elif name == "smooth":
        return img.filter(ImageFilter.SMOOTH)
    elif name == "find_edges":
        return img.filter(ImageFilter.FIND_EDGES)
    elif name == "emboss":
        return img.filter(ImageFilter.EMBOSS)
    elif name == "contour":
        return img.filter(ImageFilter.CONTOUR)
    elif name == "detail":
        return img.filter(ImageFilter.DETAIL)
    elif name == "rotate":
        return img.rotate(params.get("angle", 90), expand=True)
    elif name == "flip_h":
        return img.transpose(Image.FLIP_LEFT_RIGHT)
    elif name == "flip_v":
        return img.transpose(Image.FLIP_TOP_BOTTOM)
    elif name == "resize":
        return img.resize((params.get("width", img.width), params.get("height", img.height)), Image.LANCZOS)
    elif name == "crop":
        return img.crop((params.get("left", 0), params.get("top", 0),
                         params.get("right", img.width), params.get("bottom", img.height)))
    return img


def _blend_with_mode(base, top, mode):
    """Blend two images using the specified blend mode with numpy."""
    if not HAS_NUMPY:
        return Image.alpha_composite(base.convert("RGBA"), top.convert("RGBA"))

    b = np.array(base.convert("RGBA"), dtype=np.float64) / 255.0
    t = np.array(top.convert("RGBA"), dtype=np.float64) / 255.0
    br, bg, bb, ba = b[:,:,0], b[:,:,1], b[:,:,2], b[:,:,3]
    tr, tg, tb, ta = t[:,:,0], t[:,:,1], t[:,:,2], t[:,:,3]

    if mode == "multiply":
        rr, rg, rb = br*tr, bg*tg, bb*tb
    elif mode == "screen":
        rr, rg, rb = 1-(1-br)*(1-tr), 1-(1-bg)*(1-tg), 1-(1-bb)*(1-tb)
    elif mode == "overlay":
        rr = np.where(br < 0.5, 2*br*tr, 1-2*(1-br)*(1-tr))
        rg = np.where(bg < 0.5, 2*bg*tg, 1-2*(1-bg)*(1-tg))
        rb = np.where(bb < 0.5, 2*bb*tb, 1-2*(1-bb)*(1-tb))
    elif mode == "darken":
        rr, rg, rb = np.minimum(br, tr), np.minimum(bg, tg), np.minimum(bb, tb)
    elif mode == "lighten":
        rr, rg, rb = np.maximum(br, tr), np.maximum(bg, tg), np.maximum(bb, tb)
    elif mode == "color_dodge":
        rr = np.where(tr < 1.0, np.minimum(1.0, br / (1.0 - tr + 1e-10)), 1.0)
        rg = np.where(tg < 1.0, np.minimum(1.0, bg / (1.0 - tg + 1e-10)), 1.0)
        rb = np.where(tb < 1.0, np.minimum(1.0, bb / (1.0 - tb + 1e-10)), 1.0)
    elif mode == "color_burn":
        rr = np.where(tr > 0, 1.0 - np.minimum(1.0, (1.0 - br) / (tr + 1e-10)), 0.0)
        rg = np.where(tg > 0, 1.0 - np.minimum(1.0, (1.0 - bg) / (tg + 1e-10)), 0.0)
        rb = np.where(tb > 0, 1.0 - np.minimum(1.0, (1.0 - bb) / (tb + 1e-10)), 0.0)
    elif mode == "hard_light":
        rr = np.where(tr < 0.5, 2*br*tr, 1-2*(1-br)*(1-tr))
        rg = np.where(tg < 0.5, 2*bg*tg, 1-2*(1-bg)*(1-tg))
        rb = np.where(tb < 0.5, 2*bb*tb, 1-2*(1-bb)*(1-tb))
    elif mode == "soft_light":
        rr = np.where(tr < 0.5, br-(1-2*tr)*br*(1-br), br+(2*tr-1)*(np.sqrt(br)-br))
        rg = np.where(tg < 0.5, bg-(1-2*tg)*bg*(1-bg), bg+(2*tg-1)*(np.sqrt(bg)-bg))
        rb = np.where(tb < 0.5, bb-(1-2*tb)*bb*(1-bb), bb+(2*tb-1)*(np.sqrt(bb)-bb))
    elif mode == "difference":
        rr, rg, rb = np.abs(br-tr), np.abs(bg-tg), np.abs(bb-tb)
    elif mode == "exclusion":
        rr, rg, rb = br+tr-2*br*tr, bg+tg-2*bg*tg, bb+tb-2*bb*tb
    else:
        rr, rg, rb = tr, tg, tb

    ra = np.clip(ba + ta * (1 - ba), 0, 1)
    result = np.stack([
        np.clip(rr * ta + br * (1 - ta), 0, 1),
        np.clip(rg * ta + bg * (1 - ta), 0, 1),
        np.clip(rb * ta + bb * (1 - ta), 0, 1),
        ra,
    ], axis=-1)
    return Image.fromarray((result * 255).astype(np.uint8), "RGBA")


def _composite_layer(canvas, layer, project_dir):
    """Composite a single layer onto the canvas."""
    if not layer.get("visible", True):
        return canvas
    opacity = layer.get("opacity", 1.0)
    blend_mode = layer.get("blend_mode", "normal")
    source = layer.get("source")

    if source and os.path.isfile(source):
        layer_img = Image.open(source).convert("RGBA")
    elif layer.get("type") == "solid":
        color = layer.get("color", "#FFFFFF")
        layer_img = Image.new("RGBA", canvas.size, color)
    else:
        return canvas

    if layer_img.size != canvas.size:
        paste_img = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
        ox = layer.get("offset_x", 0)
        oy = layer.get("offset_y", 0)
        paste_img.paste(layer_img, (ox, oy))
        layer_img = paste_img

    for f in layer.get("filters", []):
        layer_img = _apply_single_filter(layer_img, f)

    if opacity < 1.0:
        alpha = layer_img.split()[3]
        alpha = alpha.point(lambda a: int(a * opacity))
        layer_img.putalpha(alpha)

    if blend_mode == "normal":
        canvas = Image.alpha_composite(canvas, layer_img)
    else:
        canvas = _blend_with_mode(canvas, layer_img, blend_mode)

    return canvas


MAX_CANVAS_DIMENSION = 10000
MAX_CANVAS_PIXELS = 100_000_000  # 100 megapixels


def render(project, output, preset="png", quality=None):
    """Render project to an image file."""
    if not HAS_PILLOW:
        return {"ok": False, "error": "Pillow not installed"}

    canvas_info = project.get("canvas", {})
    w = canvas_info.get("width", 1920)
    h = canvas_info.get("height", 1080)
    bg = canvas_info.get("background", "#FFFFFF")

    if w > MAX_CANVAS_DIMENSION or h > MAX_CANVAS_DIMENSION:
        return {"ok": False, "error": f"Canvas dimensions exceed {MAX_CANVAS_DIMENSION}px limit: {w}x{h}"}
    if w * h > MAX_CANVAS_PIXELS:
        return {"ok": False, "error": f"Canvas exceeds {MAX_CANVAS_PIXELS} pixel limit: {w*h}"}
    if w < 1 or h < 1:
        return {"ok": False, "error": f"Canvas dimensions must be positive: {w}x{h}"}

    canvas = Image.new("RGBA", (w, h), bg)
    project_dir = os.path.dirname(os.path.abspath(output))

    for layer in project.get("layers", []):
        canvas = _composite_layer(canvas, layer, project_dir)

    from cli_anything.gimp.core.filters import FILTER_REGISTRY
    for f in project.get("filters", []):
        f_copy = dict(f)
        f_copy["_registry"] = FILTER_REGISTRY.get(f["filter"], {})
        canvas = _apply_single_filter(canvas, f_copy)

    if preset in EXPORT_PRESETS:
        fmt_info = EXPORT_PRESETS[preset]
    else:
        fmt_info = EXPORT_PRESETS["png"]

    fmt = fmt_info["format"]
    save_params = dict(fmt_info["params"])
    if quality is not None:
        save_params["quality"] = quality

    if fmt in ("JPEG", "BMP"):
        canvas = canvas.convert("RGB")
    elif fmt == "GIF":
        canvas = canvas.convert("P")

    os.makedirs(os.path.dirname(output) or ".", exist_ok=True)
    canvas.save(output, format=fmt, **save_params)
    file_size = os.path.getsize(output)

    return {
        "ok": True,
        "path": output,
        "format": fmt,
        "dimensions": {"width": w, "height": h},
        "file_size": file_size,
    }


def list_presets():
    """Return all export presets."""
    return {"ok": True, "presets": EXPORT_PRESETS}
