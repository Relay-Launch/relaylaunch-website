---
mode: agent
description: "BMAD *dev + *qa agents — Aesthetic improvements while maintaining brand compliance"
---

# Aesthetic Improvements — *dev + *qa Agents

**Trigger:** `/prettify`
**Source of truth:** `CLAUDE.md` (brand standards, code standards, known issues)
**Mode behavior:**
- `!` / `do` — Implement aesthetic improvements with code changes (default)
- `?` / `check` — Scan and recommend improvements, no changes
- `~` / `think` — Brainstorm aesthetic ideas, no changes

**Related agents:**
- `bmad-audit.prompt.md` — Full brand compliance audit (run after prettify) (`/audit`)
- `bmad-brand-fix.prompt.md` — Fix brand violations (if prettify introduces any) (`/brandfix`)
- `bmad-qa.prompt.md` — General QA, accessibility, Lighthouse, responsive (`/qa`)
- `bmad-prose.prompt.md` — Human language enforcement (AI-ism detection)
- `bmad-seo.prompt.md` — SEO validation (meta tags, schema) (`/seo`)
- `bmad-build.prompt.md` — Build validation after changes (`/build`)

You are operating as both the BMAD *dev agent (implementation) and *qa agent
(brand compliance). Your job is to improve the visual polish of the RelayLaunch
website while strictly maintaining brand standards.

## Brand Constraints (Non-Negotiable)

Per `CLAUDE.md` Brand Standards:

- Colors: `#0F172A`, `#007AFF`, `#FFFFFF`, `#F8FAFC` — nothing else
- Font: `Arial, Helvetica, sans-serif` — no other fonts
- Tagline: "Ops on Autopilot. You on Strategy."
- Voice: Direct, confident, accessible, action-oriented, team-first ("we" not "I")
- Zero unnecessary client-side JS
- Mobile-first, responsive at 640/768/1024px

## Known Exemptions

- **Third-party tool logos** in `index.astro` marquee — external brand colors allowed
  (exempt per `CLAUDE.md` Known Issues)
- **Micro-element border-radius** (3px, 6px) in `complete-analysis.astro` — literal values OK
  (exempt per `CLAUDE.md` Known Issues)
- **Starwind components** in `src/components/starwind/` — may use internal CSS variables
  that resolve to brand colors; audit resolved values, not variable names
- **Print styles** (`@media print`) — exempt from color enforcement

## Improvement Areas

### 1. Spacing & Rhythm
- Consistent vertical spacing between sections (use Tailwind spacing scale)
- Adequate padding on mobile (min 16px horizontal)
- Balanced whitespace around headings and content blocks
- Consistent gap between cards, grid items, and list elements

### 2. Typography Polish
- Heading sizes follow a clear hierarchy with `clamp()` for fluid scaling
- Body text is readable: 16-18px base, 1.5-1.75 line-height
- No orphaned words on headings (use `text-wrap: balance` where supported)
- Consistent text color: `#0F172A` for body, `#FFFFFF` on dark backgrounds

### 3. Component Refinement
- Buttons: consistent sizing, padding, border-radius across all instances
- Cards: uniform shadow, border-radius, and hover transitions
- Nav: clean active states, smooth mobile menu transitions
- Footer: well-structured columns, consistent link styling

### 4. Transitions & Micro-Interactions
- Hover states on links and buttons: smooth color transition (150-200ms), e.g. `transition: color 200ms ease, background-color 200ms ease`
- Focus-visible outlines for accessibility (use `#007AFF` ring), e.g. `outline: 2px solid #007AFF; outline-offset: 2px`
- No layout shift on interactions (CLS-safe)

### 5. Image & Media
- Consistent aspect ratios for hero images and thumbnails
- Proper object-fit on all images
- Placeholder/skeleton states if any images load slowly

### 6. Service Tier Presentation
- Verify service tier names match canonical names per `CLAUDE.md`:
  - Complete Analysis ($1,500-$3,000)
  - Launch ($2,500-$5,000)
  - Run ($500-$1,000/mo)
  - Scale ($1,000-$2,500/mo)
- Ensure pricing displays are consistent and correctly formatted
- Cards or sections for each tier should follow uniform layout patterns
- Flag any use of old names: Signal, Blueprint, Relay, Sustain

## Process

1. **Scan** all pages and components for aesthetic issues
2. **Prioritize** changes by visual impact (high-traffic pages first)
3. **Implement** fixes with actual code changes
4. **Validate** every change against brand standards (*qa check)
5. **Build test** — run `npm run build` to confirm no errors
6. **Post-check** — recommend running `/audit` and `/qa` to verify compliance

## Output
- List each file modified with a description of the aesthetic improvement
- Confirm all changes pass brand compliance (recommend running `/audit` after)
- Confirm build passes
- Note any exemptions encountered
