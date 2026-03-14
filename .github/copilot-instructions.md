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
- Tagline: "Ops on Autopilot. You on Strategy."
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
- **Deployment:** Cloudflare Workers via wrangler deploy
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

## AI Agents & Tools — The Relay Method™

This repo uses **The Relay Method™** — RelayLaunch's branded AI agent
orchestration framework. See `docs/agents.md` for the full registry,
all triggers, and specialist role definitions.

### Quick Triggers

Type any `/trigger` in your prompt to activate the matching specialist:

| Trigger | Specialist | Trigger | Specialist |
|---------|-----------|---------|-----------|
| `/architect` | Architecture review | `/frontend` | UI implementation |
| `/audit` | Brand compliance | `/backend` | API/server design |
| `/brandfix` | Fix color violations | `/content` | Blog/copywriting |
| `/prettify` | Aesthetic polish | `/growth` | Acquisition/conversion |
| `/seo` | SEO audit | `/brand` | Brand identity |
| `/build` | Implement code | `/social` | Social strategy |
| `/plan` | Requirements/roadmap | `/ads` | PPC/paid media |
| `/research` | Research/discovery | `/outbound` | Prospecting |
| `/sprint` | Sprint planning | `/deals` | Deal strategy |
| `/qa` | Testing/compliance | `/proposal` | RFP/proposals |
| `/devops` | CI/CD/pipelines | `/coach` | Rep development |
| `/ux` | UX research | `/datamodel` | Data model review |
| `/superpowers` | Workflow engine | `/api` | API endpoint review |

### Mode + Domain Triggers

Use a mode prefix + domain for fast, precise agent activation:

**Modes:** `?` or `check` (review only) | `!` or `do` (make changes) | `~` or `think` (brainstorm)
**Domains:** `code` | `brand` | `growth` | `ops` | `biz` | `plan` | `qa`

Examples: `?brand` = audit brand, `!code` = build feature, `~growth` = brainstorm marketing

### The Ship Gate

- Agents CAN commit locally but must NOT push without `/ship`
- `/ship` runs all 7 default agents as gate check, then push + PR
- Gate order: Build > Security > Brand > QA > Prose > Infra > GitHub

### Service-Tier Triggers

- `/relay analysis` — Complete Analysis diagnostic workflow
- `/relay launch` — Launch tier project build
- `/relay run` — Run tier monthly retainer ops
- `/relay scale` — Scale tier premium growth ops
- `/relay brand` — Brand enforcement across all touchpoints
- `/relay performance` — Lighthouse, Core Web Vitals, SEO
- `/relay optimize` — Agents review and improve their own prompt files

### Frameworks

- **[BMAD Method](https://github.com/bmad-code-org/BMAD-METHOD)** — Agile AI development with specialized agents and structured workflows
- **[The Agency](https://github.com/msitarzewski/agency-agents)** — Curated AI agent personalities for engineering, design, marketing, and sales
- **[Superpowers](https://github.com/obra/superpowers)** — Structured multi-step development workflow (brainstorm → ship)

### BMAD Prompt Files (`.github/prompts/`)

- `bmad-architect.prompt.md` — Architecture review and structure validation
- `bmad-api-review.prompt.md` — API endpoint review and validation
- `bmad-audit.prompt.md` — Full brand compliance audit
- `bmad-brand-fix.prompt.md` — Find and fix brand color violations
- `bmad-build.prompt.md` — Feature implementation, bug fixes
- `bmad-data-model.prompt.md` — Data model and schema review
- `bmad-plan.prompt.md` — Requirements and prioritization
- `bmad-prettify.prompt.md` — Aesthetic polish with brand compliance
- `bmad-qa.prompt.md` — Testing, audit and compliance
- `bmad-research.prompt.md` — Research and discovery
- `bmad-seo.prompt.md` — SEO audit with prioritized fixes
- `bmad-sprint.prompt.md` — Story creation and sprint planning
- `bmad-prose.prompt.md` — Human language enforcement (Prose Agent)
- `bmad-infra.prompt.md` — DNS, CDN, CI/CD, hosting review
- `bmad-security.prompt.md` — Threat detection, vulnerability scanning, CSP
- `bmad-github.prompt.md` — Workflows, Actions, branch protection

### Quick Agent Lookup

When asked for help with a topic, check `docs/agents.md` to match the task
to the right agent. Key mappings for this repo:

- **Brand/colors/fonts** → BMAD `*qa` or `*dev`, Agency Brand Guardian
- **SEO/meta/schema** → BMAD `*pm` (SEO audit prompt)
- **Architecture/structure** → BMAD `*architect`, Agency Software Architect
- **Code/build/fix** → BMAD `*dev`, Agency Frontend Developer
- **Content/blog/copy** → Agency Content Creator
- **Design/UI/UX** → Agency UI Designer, Agency UX Researcher
- **Growth/marketing** → Agency Growth Hacker, Agency Social Media Strategist

## Related Repositories

This repo is part of the RelayLaunch multi-repo ecosystem:

- **relaylaunch-website** (this repo) — Public-facing marketing site (Astro 5 + Cloudflare)
- **relaylaunch-control-center** — Internal Command Center app (client dashboard, operations tools)

When working on features that touch both repos (API integrations, shared data
models, webhook contracts), check `docs/blueprints/` for cross-repo specs.

## Blueprints (AI-Assisted Development)

Before implementing new features, check `docs/blueprints/` for architecture
docs, API contracts, feature requirements, and shared standards. Upload
blueprint documents to that folder before starting a build session.

## Known Issues

- Third-party tool logos in index.astro marquee use external brand colors (exempt from 4-color brand standard)
- Micro-element border-radius (3px, 6px) in complete-analysis.astro progress bars/badges left as literal values (too small for CSS variables)
