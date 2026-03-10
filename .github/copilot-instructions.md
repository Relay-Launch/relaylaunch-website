# RelayLaunch — GitHub Copilot Instructions

This file is auto-loaded by GitHub Copilot on every prompt in VS Code.
It defines the brand standards, tech stack, and code standards for all
code generation and suggestions in this repository.

## Project Overview

RelayLaunch (relaylaunch.com) is a veteran-owned digital infrastructure
consultancy website. Built with Astro 5 + Tailwind CSS 4.2 + MDX.
Deployed to Cloudflare via wrangler (CI: GitHub Actions → wrangler deploy).
Founder: Victor David Medina, USMC Sergeant (E-5), Watertown MA.

## Brand Standards — ENFORCE ON ALL CHANGES

- Primary: Dark Navy `#0F172A` — headers, nav, footer, dark sections
- Accent: Electric Blue `#007AFF` — CTAs, links, hover states ONLY
- Background: White `#FFFFFF`
- Alt sections: Light Gray `#F8FAFC`
- Font: `Arial, Helvetica, sans-serif` — NO other fonts
- Tagline: "Launch your digital infrastructure, without pausing your business."
- Voice: Direct, confident, accessible, action-oriented, veteran precision
- **DO NOT** use green, orange, or any color outside this 4-color system

## Service Tiers (Canonical Names)

| Tier | Price | Description |
|------|-------|-------------|
| Complete Analysis | $1,500–$3,000 | Entry point, diagnostic engagement |
| Launch | $2,500–$5,000 | One-time project build |
| Run | $500–$1,000/mo | Monthly retainer, 3-month min |
| Scale | $1,000–$2,500/mo | Premium retainer, 6-month min |

## Tech Stack

- **Framework:** Astro 5 (static output, islands architecture)
- **Styling:** Tailwind CSS 4.2 + custom CSS variables + Starwind components
- **Content:** MDX blog posts via Astro Content Collections
- **Deployment:** Cloudflare Pages/Workers via wrangler
- **CI/CD:** GitHub Actions (.github/workflows/astro.yml → wrangler deploy)
- **Domain:** relaylaunch.com (Registrar: Porkbun, DNS: Cloudflare)
- **Adapter:** @astrojs/cloudflare

## Project Structure

- `src/pages/` — Astro page routes
- `src/content/blog/` — MDX blog posts with frontmatter schema
- `src/components/` — Reusable Astro components (Nav, Footer, SEO)
- `src/components/starwind/` — Starwind design system components
- `src/components/layouts/` — BaseLayout.astro, BlogPostLayout.astro
- `src/layouts/` — Page layout wrapper (Layout.astro)
- `src/styles/` — Global CSS (global.css, starwind.css)
- `src/utils/` — Utility functions (blog.ts)
- `public/` — Static assets (favicon, robots.txt, og-default.png)

## Code Standards

- Every page must have a unique `<title>`, `<meta description>`, and Open Graph tags
- Target: Lighthouse 95+, sub-1-second load
- Responsive: mobile-first, breakpoints at 640px / 768px / 1024px
- Accessibility: WCAG AA, proper heading hierarchy, alt text on all images
- Use Astro `<Image>` component with lazy loading for all images
- Zero unnecessary client-side JS — Astro static-first approach
- Internal links use root-relative paths (`/services`, `/contact`)
- Commit messages: conventional commits (`feat:`, `fix:`, `chore:`)

## Color Rules for Code Generation

When generating CSS, Tailwind classes, or inline styles:

- Use `#0F172A` / `slate-900` for dark backgrounds, text, nav, footer
- Use `#007AFF` for buttons, links, hover states, and CTAs only
- Use `#FFFFFF` for page backgrounds
- Use `#F8FAFC` / `slate-50` for alternating section backgrounds
- Never introduce `green`, `orange`, `red`, `purple`, or any other hue
- Never use Tailwind color classes outside `slate`, `white`, and the custom `#007AFF` accent

## Known Issues

- `global.css` still uses `--color-green` and `--color-orange` — these MUST be replaced
- `starwind.css` theme may reference wrong color palette
- `README.md` may show old tier names (Signal/Blueprint/Relay/Sustain)
