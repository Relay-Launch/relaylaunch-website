"""GIMP batch mode backend for operations requiring the real GIMP engine."""

import os
import re
import shutil
import subprocess
import tempfile


# Allowed background color tokens for Script-Fu FILL- constants
_VALID_BG_COLORS = {"WHITE", "BLACK", "FOREGROUND", "BACKGROUND", "PATTERN"}

# Pattern for safe file paths in Script-Fu strings (no quotes, parens, backslashes)
_UNSAFE_PATH_CHARS = re.compile(r'["\\\(\)]')


def _sanitize_path(path):
    """Validate a file path is safe for Script-Fu string interpolation."""
    resolved = os.path.realpath(path)
    if _UNSAFE_PATH_CHARS.search(resolved):
        raise ValueError(f"Path contains unsafe characters for Script-Fu: {resolved}")
    return resolved


def _sanitize_int(value, name="value", min_val=1, max_val=65535):
    """Validate and cast a value to a bounded integer."""
    val = int(value)
    if val < min_val or val > max_val:
        raise ValueError(f"{name} must be between {min_val} and {max_val}, got {val}")
    return val


def _sanitize_float(value, name="value", min_val=-1e6, max_val=1e6):
    """Validate and cast a value to a bounded float."""
    val = float(value)
    if val < min_val or val > max_val:
        raise ValueError(f"{name} must be between {min_val} and {max_val}, got {val}")
    return val


def find_gimp():
    """Locate GIMP executable on the system."""
    candidates = [
        "gimp",
        "gimp-2.10",
        "gimp-2.99",
        "/usr/bin/gimp",
        "/usr/local/bin/gimp",
        "/snap/bin/gimp",
        "/Applications/GIMP-2.10.app/Contents/MacOS/gimp",
    ]
    for name in candidates:
        path = shutil.which(name)
        if path:
            return path
    return None


def batch_script_fu(script, timeout=60):
    """Run a Script-Fu command in GIMP headless batch mode."""
    gimp = find_gimp()
    if not gimp:
        return {"ok": False, "error": "GIMP not found on system PATH"}
    cmd = [gimp, "-i", "-b", script, "-b", "(gimp-quit 0)"]
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        return {
            "ok": result.returncode == 0,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode,
        }
    except subprocess.TimeoutExpired:
        return {"ok": False, "error": f"GIMP timed out after {timeout}s"}
    except FileNotFoundError:
        return {"ok": False, "error": "GIMP executable not found"}


def create_and_export(width, height, output_path, bg_color="white"):
    """Create a blank image via GIMP and export it."""
    width = _sanitize_int(width, "width")
    height = _sanitize_int(height, "height")
    output_path = _sanitize_path(output_path)

    bg_token = bg_color.upper()
    if bg_token not in _VALID_BG_COLORS:
        return {"ok": False, "error": f"Invalid bg_color: {bg_color}. Valid: {_VALID_BG_COLORS}"}

    script = (
        f'(let* ((image (car (gimp-image-new {width} {height} RGB)))'
        f'       (layer (car (gimp-layer-new image {width} {height} RGB-IMAGE "Background" 100 LAYER-MODE-NORMAL))))'
        f'  (gimp-image-insert-layer image layer 0 -1)'
        f'  (gimp-image-set-active-layer image layer)'
        f'  (gimp-edit-fill layer FILL-{bg_token})'
        f'  (file-png-save RUN-NONINTERACTIVE image layer "{output_path}" "{output_path}" 0 9 1 1 1 1 1)'
        f'  (gimp-image-delete image))'
    )
    return batch_script_fu(script)


def apply_filter_and_export(input_path, output_path, filter_name, params=None):
    """Load an image in GIMP, apply a filter, and export."""
    input_path = _sanitize_path(input_path)
    output_path = _sanitize_path(output_path)
    params = params or {}

    filter_scripts = {
        "gaussian_blur": lambda p: (
            f'(plug-in-gauss RUN-NONINTERACTIVE image layer '
            f'{_sanitize_int(p.get("radius", 5), "radius", 0, 500)} '
            f'{_sanitize_int(p.get("radius", 5), "radius", 0, 500)} 0)'
        ),
        "unsharp_mask": lambda p: (
            f'(plug-in-unsharp-mask RUN-NONINTERACTIVE image layer '
            f'{_sanitize_float(p.get("radius", 3), "radius", 0, 500)} '
            f'{_sanitize_float(p.get("amount", 0.5), "amount", 0, 10)} '
            f'{_sanitize_int(p.get("threshold", 0), "threshold", 0, 255)})'
        ),
        "brightness_contrast": lambda p: (
            f'(gimp-brightness-contrast layer '
            f'{_sanitize_int(p.get("brightness", 0), "brightness", -127, 127)} '
            f'{_sanitize_int(p.get("contrast", 0), "contrast", -127, 127)})'
        ),
        "desaturate": lambda _: "(gimp-desaturate-full layer DESATURATE-LUMINOSITY)",
        "invert": lambda _: "(gimp-invert layer)",
    }

    if filter_name not in filter_scripts:
        return {"ok": False, "error": f"Unsupported GIMP filter: {filter_name}"}

    filter_cmd = filter_scripts[filter_name](params)
    ext = os.path.splitext(output_path)[1].lower()

    if ext in (".jpg", ".jpeg"):
        save_cmd = f'(file-jpeg-save RUN-NONINTERACTIVE image layer "{output_path}" "{output_path}" 0.85 0 0 0 "" 0 0 0 2)'
    elif ext == ".png":
        save_cmd = f'(file-png-save RUN-NONINTERACTIVE image layer "{output_path}" "{output_path}" 0 9 1 1 1 1 1)'
    else:
        save_cmd = f'(gimp-file-overwrite RUN-NONINTERACTIVE image layer "{output_path}" "{output_path}")'

    script = (
        f'(let* ((image (car (file-png-load RUN-NONINTERACTIVE "{input_path}" "{input_path}")))'
        f'       (layer (car (gimp-image-flatten image))))'
        f'  {filter_cmd}'
        f'  {save_cmd}'
        f'  (gimp-image-delete image))'
    )
    return batch_script_fu(script)
