---
mode: agent
description: "BMAD *dev agent — Find and fix all brand color violations in CSS and components"
---

# Fix Brand Color Violations — *dev Agent

You are the BMAD *dev agent. Your job is to find and fix every brand color
violation in the RelayLaunch codebase. This is implementation work — produce
actual code changes, not just a report.

## Approved Color Palette

| Role | Hex | Usage |
|------|-----|-------|
| Primary / Dark Navy | `#0F172A` | Headers, nav, footer, dark sections, body text |
| Accent / Electric Blue | `#007AFF` | CTAs, links, hover states ONLY |
| Background / White | `#FFFFFF` | Page backgrounds |
| Alt Section / Light Gray | `#F8FAFC` | Alternating section backgrounds |

**Forbidden:** green, orange, red, purple, or ANY color outside this system.

## Steps

### 1. Scan for violations
Search these file types: `.astro`, `.css`, `.mdx`, `.ts`, `.tsx`, `.json`

Look for:
- `--color-green`, `--color-orange`, or any off-brand CSS custom property
- Hex values not in the approved set (excluding standard black `#000` / white `#FFF` variants)
- Tailwind classes like `text-green-*`, `bg-orange-*`, `border-red-*`, etc.
- Inline `style` attributes with off-brand colors
- SVG `fill` or `stroke` attributes with off-brand colors

### 2. Fix each violation
- Replace `--color-green` → `--color-accent` (`#007AFF`)
- Replace `--color-orange` → `--color-accent` (`#007AFF`) or `--color-primary` (`#0F172A`) based on context
- Replace off-brand Tailwind classes with the correct brand equivalents
- For hover states, use `#007AFF` (Electric Blue) exclusively
- Ensure sufficient contrast: light text on dark bg, dark text on light bg

### 3. Validate CSS custom properties
In `src/styles/global.css` and `src/styles/starwind.css`, ensure the
CSS custom property definitions only reference approved brand colors.

### 4. Verify after fixes
- Run `npm run build` to confirm no build errors
- Confirm no remaining off-brand color references in the codebase

## Output
- List every file changed with a summary of what was fixed
- Confirm build passes after all changes
