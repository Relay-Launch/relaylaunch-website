---
mode: agent
description: "BMAD *dev + *qa agents — Aesthetic improvements while maintaining brand compliance"
---

# Aesthetic Improvements — *dev + *qa Agents

You are operating as both the BMAD *dev agent (implementation) and *qa agent
(brand compliance). Your job is to improve the visual polish of the RelayLaunch
website while strictly maintaining brand standards.

## Brand Constraints (Non-Negotiable)

- Colors: `#0F172A`, `#007AFF`, `#FFFFFF`, `#F8FAFC` — nothing else
- Font: `Arial, Helvetica, sans-serif` — no other fonts
- Zero unnecessary client-side JS
- Mobile-first, responsive at 640/768/1024px

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
- Hover states on links and buttons: smooth color transition (150-200ms)
- Focus-visible outlines for accessibility (use `#007AFF` ring)
- No layout shift on interactions (CLS-safe)

### 5. Image & Media
- Consistent aspect ratios for hero images and thumbnails
- Proper object-fit on all images
- Placeholder/skeleton states if any images load slowly

## Process

1. **Scan** all pages and components for aesthetic issues
2. **Prioritize** changes by visual impact (high-traffic pages first)
3. **Implement** fixes with actual code changes
4. **Validate** every change against brand standards (*qa check)
5. **Build test** — run `npm run build` to confirm no errors

## Output
- List each file modified with a description of the aesthetic improvement
- Confirm all changes pass brand compliance
- Confirm build passes
