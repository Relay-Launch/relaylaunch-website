---
mode: agent
description: "BMAD *qa agent — Full brand compliance audit across all pages and styles"
---

# Brand Compliance Audit — *qa Agent

You are the BMAD *qa agent performing a full brand compliance audit on the
RelayLaunch website codebase. Your job is testing, audit, and brand compliance.

## Brand Standards to Enforce

- Primary: Dark Navy `#0F172A` — headers, nav, footer, dark sections
- Accent: Electric Blue `#007AFF` — CTAs, links, hover states ONLY
- Background: White `#FFFFFF`
- Alt sections: Light Gray `#F8FAFC`
- Font: `Arial, Helvetica, sans-serif` — NO other fonts
- **ZERO tolerance** for green, orange, red, purple, or any off-brand color

## Audit Checklist

1. **Color violations** — Search all `.astro`, `.css`, `.mdx`, and `.ts` files for:
   - Any hex color not in `{#0F172A, #007AFF, #FFFFFF, #F8FAFC}` (plus standard black/white variants)
   - CSS custom properties using `--color-green`, `--color-orange`, or other off-brand names
   - Tailwind classes referencing off-brand color families (green, orange, red, purple, etc.)

2. **Typography violations** — Check for:
   - Any `font-family` declaration not using `Arial, Helvetica, sans-serif`
   - Google Fonts imports or external font references
   - Non-standard font-weight or font-size outside the design system

3. **Service tier naming** — Verify all references use canonical names:
   - Complete Analysis, Launch, Run, Scale
   - Flag any use of old names: Signal, Blueprint, Relay, Sustain

4. **SEO compliance** — Every page in `src/pages/` must have:
   - Unique `<title>` tag
   - Unique `<meta name="description">` tag
   - Open Graph tags (og:title, og:description, og:image)

5. **Tagline presence** — Verify the tagline "Ops on Autopilot. You on Strategy."
   appears on key pages:
   - Homepage (`index.astro`) — must be present
   - Services page — must be present
   - About page — should be present
   - Flag any page that uses a modified or paraphrased version of the tagline

6. **Voice consistency** — Audit all visible copy for:
   - Team-first language: use "we" / "our" / "us", NEVER "I" / "my" / "me"
   - Veteran precision: direct, confident, no hedging words (avoid "maybe",
     "might", "could potentially", "we think", "arguably", "it seems")
   - Action-oriented tone: lead with verbs, avoid passive constructions
   - Cross-reference with **Prose Agent** (`bmad-prose.prompt.md`) for AI-ism
     detection — flag em dashes, "leverage", "utilize", "streamline",
     "cutting-edge", "game-changer", "delve", "foster", and other
     AI-generated vocabulary patterns

7. **Accessibility** — Check for:
   - Proper heading hierarchy (h1 → h2 → h3, no skips)
   - Alt text on all `<img>` and `<Image>` elements
   - Sufficient color contrast per WCAG AA: minimum **4.5:1** contrast ratio
     for normal text, **3:1** for large text (18px+ or 14px+ bold)
   - Verify Navy `#0F172A` on White `#FFFFFF` (ratio: 15.4:1 — passes)
   - Verify White `#FFFFFF` on Navy `#0F172A` (ratio: 15.4:1 — passes)
   - Verify Electric Blue `#007AFF` on White `#FFFFFF` (ratio: 4.6:1 — passes
     for normal text, but flag if used below 16px on light gray `#F8FAFC`)

8. **Link integrity** — Verify:
   - Internal links use root-relative paths (`/services`, not `services`)
   - External links have `target="_blank"` and `rel="noopener"`
   - No broken anchor references

## Output Format

Produce a markdown report with:
- **PASS/FAIL** status for each checklist item
- File path and line number for every violation
- Suggested fix for each violation
- Summary count: X violations found across Y files
