---
mode: agent
description: "BMAD *qa agent — Full brand compliance audit across all pages and styles"
---

# Brand Compliance Audit — *qa Agent

**Trigger:** `/audit` or `?brand`
**Source of truth:** `CLAUDE.md` (brand standards, service tiers, code standards)
**Mode behavior:**
- `?` / `check` — Audit only, produce report, no code changes (default)
- `!` / `do` — Audit and fix violations in-place (delegates to `bmad-brand-fix.prompt.md`)
- `~` / `think` — Brainstorm audit scope improvements, no changes

**Related agents:**
- `bmad-brand-fix.prompt.md` — Fix violations found by this audit (`/brandfix`)
- `bmad-prettify.prompt.md` — Aesthetic polish within brand constraints (`/prettify`)
- `bmad-qa.prompt.md` — General QA, accessibility, Lighthouse, responsive (`/qa`)
- `bmad-prose.prompt.md` — Human language enforcement (AI-ism detection)
- `bmad-seo.prompt.md` — SEO-specific audit (`/seo`)
- `bmad-build.prompt.md` — Build validation after fixes (`/build`)
- `bmad-security.prompt.md` — Dependency and security audit (`/security`)

You are the BMAD *qa agent performing a full brand compliance audit on the
RelayLaunch website codebase. Your job is testing, audit, and brand compliance.

## Brand Standards to Enforce

Per `CLAUDE.md` Brand Standards:

- Primary: Dark Navy `#0F172A` — headers, nav, footer, dark sections
- Accent: Electric Blue `#007AFF` — CTAs, links, hover states ONLY
- Background: White `#FFFFFF`
- Alt sections: Light Gray `#F8FAFC`
- Font: `Arial, Helvetica, sans-serif` — NO other fonts
- Tagline: "Ops on Autopilot. You on Strategy."
- **ZERO tolerance** for green, orange, red, purple, or any off-brand color

## Known Exemptions

- **Third-party tool logos** in `index.astro` marquee use external brand colors
  (e.g., Astro #FF5D01, Cloudflare #F48120) — exempt per `CLAUDE.md` Known Issues
- **Starwind design system** components in `src/components/starwind/` may use
  CSS custom properties that resolve to brand colors — audit the resolved values,
  not the variable names
- **Micro-element border-radius** (3px, 6px) in `complete-analysis.astro`
  progress bars/badges — left as literal values per `CLAUDE.md` Known Issues
- **Print styles** — exempt from color enforcement

## Audit Checklist

1. **Color violations** — Search all `.astro`, `.css`, `.mdx`, and `.ts` files for:
   - Any hex color not in `{#0F172A, #007AFF, #FFFFFF, #F8FAFC}` (plus standard black/white variants)
   - CSS custom properties using `--color-green`, `--color-orange`, or other off-brand names
   - Tailwind classes referencing off-brand color families (green, orange, red, purple, etc.)

2. **Typography violations** — Check for:
   - Any `font-family` declaration not using `Arial, Helvetica, sans-serif`
   - Google Fonts imports or external font references
   - Non-standard font-weight or font-size outside the design system

3. **Service tier naming** — Verify all references use canonical names and prices:
   - Complete Analysis ($1,500-$3,000) — entry point, diagnostic engagement
   - Launch ($2,500-$5,000) — one-time project build
   - Run ($500-$1,000/mo) — monthly retainer, 3-month min
   - Scale ($1,000-$2,500/mo) — premium retainer, 6-month min
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

9. **Prompt file integrity** — Verify all 16 BMAD prompt files exist in
   `.github/prompts/`: bmad-architect, bmad-api-review, bmad-audit,
   bmad-brand-fix, bmad-build, bmad-data-model, bmad-github, bmad-infra,
   bmad-plan, bmad-prettify, bmad-prose, bmad-qa, bmad-research,
   bmad-security, bmad-seo, bmad-sprint

## Output Format

Produce a markdown report with:
- **PASS/FAIL** status for each checklist item
- File path and line number for every violation
- Suggested fix for each violation (or delegate to `bmad-brand-fix.prompt.md` in `!` mode)
- Summary count: X violations found across Y files
