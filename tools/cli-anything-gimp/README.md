# cli-anything-gimp

CLI harness for GIMP. Raster image processing via CLI. Generated using the
[CLI-Anything](https://github.com/HKUDS/CLI-Anything) 7-phase pipeline.

## Installation

```bash
cd tools/cli-anything-gimp
pip install -e .
```

## Usage

```bash
# Create a new project
cli-anything-gimp project new --name poster --width 1920 --height 1080 -o poster.json

# JSON output for agent consumption
cli-anything-gimp --json project new --name banner --profile instagram_post -o banner.json

# Add layers
cli-anything-gimp -p poster.json layer add -n "Background" --type solid --color "#0F172A"
cli-anything-gimp -p poster.json layer add-file photo.png -n "Photo"

# Apply filters
cli-anything-gimp -p poster.json filter add gaussian_blur -p radius=5
cli-anything-gimp -p poster.json filter add brightness -p factor=1.3

# Export
cli-anything-gimp -p poster.json export render output.png --preset png
cli-anything-gimp -p poster.json export render output.jpg --preset jpeg-high

# Interactive REPL
cli-anything-gimp repl

# Inspect media
cli-anything-gimp media probe photo.png
```

## Command Groups

| Group | Description |
|-------|------------|
| `project` | Create, open, save projects with canvas presets |
| `layer` | Add, remove, duplicate, move, flatten layers |
| `canvas` | Resize, scale, crop, set mode/DPI |
| `filter` | 24+ filters: blur, sharpen, adjust, stylize, transform |
| `media` | Probe images, check references, histograms |
| `export` | Render with 13 format presets (PNG, JPEG, WebP, TIFF, etc.) |
| `draw` | GIMP batch mode operations (requires GIMP installed) |
| `session` | Undo/redo with 50-step history |

## Architecture

- **Primary engine:** Pillow (always available)
- **Optional backend:** GIMP batch mode via `gimp -i -b` (Script-Fu)
- **State model:** JSON project manifests with layer stacks
- **Output:** Dual-mode, human-readable or `--json` for agents
- **REPL:** Interactive mode via prompt-toolkit

## Requirements

- Python 3.10+
- Pillow 10+
- click 8+
- prompt-toolkit 3+
- Optional: numpy (for advanced blend modes), GIMP (for batch operations)
