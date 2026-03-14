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

### 1b. Scan for font-family violations
Search all `.astro`, `.css`, `.mdx`, `.ts`, `.tsx` files for:
- Any `font-family` declaration not using `Arial, Helvetica, sans-serif`
- Google Fonts imports (`fonts.googleapis.com`, `fonts.gstatic.com`)
- `@import` or `<link>` tags loading external font files (`.woff`, `.woff2`, `.ttf`, `.otf`)
- Tailwind `font-*` utility classes referencing non-default font families
- Any reference to specific named fonts (e.g., Inter, Roboto, Poppins, etc.)

### 1c. Audit Starwind component colors
In `src/components/starwind/`, check every component for:
- Hardcoded hex colors instead of CSS custom properties
- Starwind CSS variables that resolve to off-brand colors
- Background, border, text, and shadow colors that fall outside the approved palette
- Component variants or states (hover, focus, active, disabled) using off-brand colors

### 2. Fix each violation
- Replace `--color-green` → `--color-accent` (`#007AFF`)
- Replace `--color-orange` → `--color-accent` (`#007AFF`) or `--color-primary` (`#0F172A`) based on context
- Replace off-brand Tailwind classes with the correct brand equivalents
- For hover states, use `#007AFF` (Electric Blue) exclusively
- Ensure sufficient contrast: light text on dark bg, dark text on light bg

### 3. Validate CSS custom properties
In `src/styles/global.css` and `src/styles/starwind.css`, ensure the
CSS custom property definitions only reference approved brand colors.

### 3b. Enforce CSS variable naming conventions
- Brand color variables must use the `--color-` prefix:
  `--color-primary`, `--color-accent`, `--color-background`, `--color-alt`
- Verify no duplicate or conflicting variable definitions across stylesheets
- Starwind overrides in `starwind.css` should map to brand variables, not raw hex
- Flag any ad-hoc variable names (e.g., `--blue`, `--navy`, `--btn-color`)
  that bypass the naming convention

### 4. Verify after fixes
- Run `npm run build` to confirm no build errors
- Confirm no remaining off-brand color references in the codebase

## Output
- List every file changed with a summary of what was fixed
- Confirm build passes after all changes
