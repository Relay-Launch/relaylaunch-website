# RelayLaunch Website

## Project Overview
RelayLaunch (relaylaunch.com) is a veteran-owned digital infrastructure
consultancy website. Built with Astro 5 + Tailwind CSS 4.2 + MDX.
Deployed to Cloudflare via wrangler (CI: GitHub Actions -> wrangler deploy).
Founder: Victor David Medina, USMC Sergeant (E-5), Watertown MA.
Live URL: https://www.relaylaunch.com

## Brand Standards (ENFORCE ON ALL CHANGES)
- Primary: Dark Navy #0F172A (headers, nav, footer, dark sections)
- Accent: Electric Blue #007AFF (CTAs, links, hover states ONLY)
- Background: White #FFFFFF
- Alt sections: Light Gray #F8FAFC
- Font: Arial, Helvetica, sans-serif - NO other fonts
- Tagline: "Launch your digital infrastructure, without pausing your business."
- Voice: Direct, confident, accessible, action-oriented, veteran precision
- DO NOT use green, orange, or any color outside this 4-color system

## Service Tiers (Canonical Names)
- Complete Analysis ($1,500-$3,000) - entry point, diagnostic engagement
- Launch ($2,500-$5,000) - one-time project build
- Run ($500-$1,000/mo) - monthly retainer, 3-month min
- Scale ($1,000-$2,500/mo) - premium retainer, 6-month min

## Tech Stack
- Framework: Astro 5 (static output, islands architecture)
- Styling: Tailwind CSS 4.2 + custom CSS variables + Starwind components
- Content: MDX blog posts via Astro Content Collections
- Deployment: Cloudflare Workers via wrangler deploy
- CI/CD: GitHub Actions (.github/workflows/astro.yml -> wrangler deploy)
- Domain: relaylaunch.com (Registrar: Porkbun, DNS: Cloudflare)
- Custom Domains: relaylaunch.com + www.relaylaunch.com (both via Workers custom domains in wrangler.jsonc)
- Adapter: @astrojs/cloudflare

## DNS & Domain Configuration
- Registrar: Porkbun (domain purchased here, DO NOT transfer for 60 days after registration)
- DNS: Cloudflare (nameservers: lindsey.ns.cloudflare.com, steven.ns.cloudflare.com)
- Zone ID: 1113a607a714b1f4f3467003a78175fa
- Both apex (relaylaunch.com) and www are served by Workers custom domains
- Workers custom domains REQUIRE Cloudflare DNS - do NOT move DNS away from Cloudflare
- Email: MX records point to Porkbun forwarding (fwd1/fwd2.porkbun.com) + smtp.google.com
- DKIM/DMARC/SPF configured for Google Workspace email
- API token requires these permissions: Workers Edit, Workers Routes Edit, Zone Read, DNS Edit

## Commands
- npm ci - install dependencies
- npm run dev - start dev server at localhost:4321
- npm run build - production build to dist/
- npm run preview - build + wrangler dev (local Cloudflare preview)
- npm run deploy - build + wrangler deploy (push to production)

## Project Structure
- src/pages/ - Astro page routes
- src/content/blog/ - MDX blog posts with frontmatter schema
- src/components/ - Reusable Astro components (Nav, Footer, SEO)
- src/components/starwind/ - Starwind design system components
- src/components/layouts/ - BaseLayout.astro, BlogPostLayout.astro
- src/layouts/ - Page layout wrapper (Layout.astro)
- src/styles/ - Global CSS (global.css, starwind.css)
- src/utils/ - Utility functions (blog.ts)
- public/ - Static assets (favicon, robots.txt, og-default.png)

## Code Standards
- Every page: unique <title>, <meta description>, Open Graph tags
- Target: Lighthouse 95+, sub-1-second load
- Responsive: mobile-first, breakpoints 640/768/1024px
- Accessibility: WCAG AA, proper heading hierarchy, alt text
- Use Astro <Image> with lazy loading for all images
- Zero unnecessary client-side JS - Astro static-first
- Internal links use root-relative paths (/services, /contact)
- Commit messages: conventional commits (feat:, fix:, chore:)

## AI Agents & Tools
This repo uses two agent frameworks. See `docs/agents.md` for the full
registry with trigger keywords by category.

### Frameworks
- **BMAD Method** - Agile AI development framework (https://github.com/bmad-code-org/BMAD-METHOD)
- **The Agency** - Specialized AI agent personalities (https://github.com/msitarzewski/agency-agents)

### BMAD Agent Roles
When acting as a BMAD agent, follow the role:
- *analyst = Research & discovery
- *pm = Requirements & prioritization
- *architect = Technical design & structure
- *sm = Story creation & sprint planning
- *dev = Implementation & code
- *qa = Testing, audit & brand compliance

### BMAD Prompt Files (.github/prompts/)
- `bmad-architect.prompt.md` — Architecture review (*architect)
- `bmad-audit.prompt.md` — Brand compliance audit (*qa)
- `bmad-brand-fix.prompt.md` — Fix brand color violations (*dev)
- `bmad-prettify.prompt.md` — Aesthetic polish (*dev + *qa)
- `bmad-seo.prompt.md` — SEO audit (*pm)

### Quick Agent Lookup
When the user asks for help with a topic, check `docs/agents.md` to find
the right agent. Key mappings for this repo:
- Brand/colors/fonts → BMAD *qa or *dev (brand), Agency Brand Guardian
- SEO/meta/schema → BMAD *pm (SEO)
- Architecture/structure → BMAD *architect, Agency Software Architect
- Code/build/fix → BMAD *dev, Agency Frontend Developer
- Content/blog/copy → Agency Content Creator
- Design/UI/UX → Agency UI Designer, UX Researcher
- Growth/marketing → Agency Growth Hacker, Social Media Strategist

## Agent Team Coordination
When working as a teammate in an agent team:
- Check the task list before starting new work
- Module boundaries: pages are self-contained, components are shared
- Do NOT modify .github/workflows/ unless explicitly asked
- Lock brand colors - never introduce new colors
- PR branches: claude/description-XXXXX format

## Related Repositories
This repo is part of the RelayLaunch multi-repo ecosystem:
- **relaylaunch-website** (this repo) - Public-facing marketing site (Astro 5 + Cloudflare)
- **relaylaunch-control-center** - Internal Command Center app (client dashboard, operations tools)

When working on features that span both repos (API integrations, shared data
models, webhook contracts), check `docs/blueprints/` for cross-repo specs.

## Blueprints (AI-Assisted Development)
Before implementing new features, check `docs/blueprints/` for:
- Architecture documents and system design specs
- API contracts and webhook payload schemas
- Feature requirements and acceptance criteria
- Shared standards between this repo and the Command Center

Upload blueprint documents to `docs/blueprints/` before starting a build
session. Reference them in prompts: "Read docs/blueprints/[file] first."

## Known Issues
- Third-party tool logos in index.astro marquee use external brand colors (exempt from 4-color brand standard)
- Micro-element border-radius (3px, 6px) in complete-analysis.astro progress bars/badges left as literal values (too small for CSS variables)
