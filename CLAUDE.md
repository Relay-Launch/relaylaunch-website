# RelayLaunch Website

## Project Overview
RelayLaunch (relaylaunch.com) is a veteran-owned digital infrastructure
consultancy website. Built with Astro 5 + Tailwind CSS 4.2 + MDX.
Deployed to Cloudflare via wrangler (CI: GitHub Actions → wrangler deploy).
Founder: Victor David Medina, USMC Sergeant (E-5), Watertown MA.
Live URL: https://www.relaylaunch.com

## Brand Standards (ENFORCE ON ALL CHANGES)
- Primary: Dark Navy #0F172A (headers, nav, footer, dark sections)
- Accent: Electric Blue #007AFF (CTAs, links, hover states ONLY)
- Background: White #FFFFFF
- Alt sections: Light Gray #F8FAFC
- Font: Arial, Helvetica, sans-serif — NO other fonts
- Tagline: "Launch your digital infrastructure, without pausing your business."
- Voice: Direct, confident, accessible, action-oriented, veteran precision
- DO NOT use green, orange, or any color outside this 4-color system

## Service Tiers (Canonical Names)
- Complete Analysis ($1,500–$3,000) — entry point, diagnostic engagement
- Launch ($2,500–$5,000) — one-time project build
- Run ($500–$1,000/mo) — monthly retainer, 3-month min
- Scale ($1,000–$2,500/mo) — premium retainer, 6-month min

## Tech Stack
- Framework: Astro 5 (static output, islands architecture)
- Styling: Tailwind CSS 4.2 + custom CSS variables + Starwind components
- Content: MDX blog posts via Astro Content Collections
- Deployment: Cloudflare Pages/Workers via wrangler
- CI/CD: GitHub Actions (.github/workflows/astro.yml → wrangler deploy)
- Domain: relaylaunch.com (Registrar: Porkbun, DNS: Cloudflare)
- Adapter: @astrojs/cloudflare

## Commands
- npm ci — install dependencies
- npm run dev — start dev server at localhost:4321
- npm run build — production build to dist/
- npm run preview — build + wrangler dev (local Cloudflare preview)
- npm run deploy — build + wrangler deploy (push to production)

## Project Structure
- src/pages/ — Astro page routes
- src/content/blog/ — MDX blog posts with frontmatter schema
- src/components/ — Reusable Astro components (Nav, Footer, SEO)
- src/components/starwind/ — Starwind design system components
- src/components/layouts/ — BaseLayout.astro, BlogPostLayout.astro
- src/layouts/ — Page layout wrapper (Layout.astro)
- src/styles/ — Global CSS (global.css, starwind.css)
- src/utils/ — Utility functions (blog.ts)
- public/ — Static assets (favicon, robots.txt, og-default.png)

## Code Standards
- Every page: unique <title>, <meta description>, Open Graph tags
- Target: Lighthouse 95+, sub-1-second load
- Responsive: mobile-first, breakpoints 640/768/1024px
- Accessibility: WCAG AA, proper heading hierarchy, alt text
- Use Astro <Image> with lazy loading for all images
- Zero unnecessary client-side JS — Astro static-first
- Internal links use root-relative paths (/services, /contact)
- Commit messages: conventional commits (feat:, fix:, chore:)

## BMAD Agent Roles
When acting as a BMAD agent, follow the role:
- *analyst = Research & discovery
- *pm = Requirements & prioritization
- *architect = Technical design & structure
- *sm = Story creation & sprint planning
- *dev = Implementation & code
- *qa = Testing, audit & brand compliance

## Agent Team Coordination
When working as a teammate in an agent team:
- Check the task list before starting new work
- Module boundaries: pages are self-contained, components are shared
- Do NOT modify .github/workflows/ unless explicitly asked
- Lock brand colors — never introduce new colors
- PR branches: claude/description-XXXXX format

## Known Issues
- Third-party tool logos in index.astro marquee use external brand colors (exempt from 4-color brand standard)
- Micro-element border-radius (3px, 6px) in complete-analysis.astro progress bars/badges left as literal values (too small for CSS variables)
