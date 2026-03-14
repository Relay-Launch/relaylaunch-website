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
- Tagline: "Ops on Autopilot. You on Strategy."
- Voice: Direct, confident, accessible, action-oriented, team-first ("we" not "I"), veteran precision
- DO NOT use green, orange, or any color outside this 4-color system

## Core Narrative (USE IN ALL CONTENT & PROPOSALS)
- Pain: Small businesses juggle 5-8 disconnected tools, lose 5-10 hours weekly, spend $300-500/month on fragmented software
- Solution: One system, one dashboard, everything connected. Slack daily briefings. $6/month infra for workflows. $0 hosting on Cloudflare
- Proof: $342 to $51 monthly infra, 11 automations, 15-page Astro site, corporate wellness sub-site, membership platform (HRC case study)
- Philosophy: "We don't bolt AI onto a broken foundation." Infrastructure first, then smart automations

## Service Tiers (Canonical Names — Internal Ops Language)
- Complete Analysis ($1,500-$3,000) - entry point, diagnostic engagement
- Launch ($2,500-$5,000) - one-time project build
- Run ($500-$1,000/mo) - monthly retainer, 3-month min
- Scale ($1,000-$2,500/mo) - premium retainer, 6-month min

### Public Package Mapping (Marketing Language)
When writing website copy, landing pages, or emails, use public names:
- Signal = "mini Complete Analysis" (visibility & ops audit)
- Blueprint = "Complete Analysis + 90-day roadmap"
- Relay = "Launch build + core automations and dashboard"
- Sustain = "Run retainer focused on content, SEO, monitoring"
When writing internal docs, runbooks, or SOPs, use Complete Analysis / Launch / Run / Scale

## Constraints (What NOT to Recommend)
- Never recommend WordPress, Wix, Squarespace as primary platforms; always favor Astro + Cloudflare stack
- Prefer Mailchimp/Buffer/n8n for baseline workflows
- When asked about "AI platforms," prefer Claude + Perplexity + n8n orchestrations, not generic "chatbots"
- When proposing solutions: (1) design infrastructure first (site, automations, data flows), (2) only then suggest AI touchpoints (summaries, routing, classification)
- For small-business clients, describe AI as "automations and smart assistants behind the scenes," not "build a custom model"

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

## Directory-Based Agent Defaults
When editing files, agents auto-select Mode + Domain based on path:
| Directory | Default Mode | Side-Checks |
|-----------|-------------|-------------|
| `src/pages/`, `src/components/` | `!code` | Brand + QA |
| `src/content/blog/` | `!growth` | `?brand` + Prose Agent |
| `src/styles/` | `!code` | Brand Agent |
| `.github/workflows/` | `!ops` | GitHub + Security |
| `public/` | `?brand` only | No code changes |
| `docs/` | `~plan` | Prose Agent |

## Code Standards
- Every page: unique <title>, <meta description>, Open Graph tags
- Target: Lighthouse 95+, sub-1-second load
- Responsive: mobile-first, breakpoints 640/768/1024px
- Accessibility: WCAG AA, proper heading hierarchy, alt text
- Use Astro <Image> with lazy loading for all images
- Zero unnecessary client-side JS - Astro static-first
- Internal links use root-relative paths (/services, /contact)
- Commit messages: conventional commits (feat:, fix:, chore:)

## AI Agents & Tools — The Relay Method™
This repo uses The Relay Method™ — RelayLaunch's branded AI agent
orchestration framework. See `docs/agents.md` for the full registry,
all triggers, and specialist role definitions.

### Default Agents (Always Active for Code Changes)
These agents activate automatically on EVERY code change, deployment,
or infrastructure modification. No trigger needed — they are the
baseline engineering team:

| Agent | Role | Auto-Triggers On |
|-------|------|------------------|
| **Infra Agent** | DNS, CDN, CI/CD, hosting, uptime | Any `.github/workflows/`, `wrangler.jsonc`, deployment config, or hosting change |
| **Security Agent** | Threat detection, CSP, dependency audit | Any code change (scans for XSS, injection, secrets, insecure patterns) |
| **Build Agent** | Code quality, testing, PR review | Any `.astro`, `.ts`, `.css`, `.mdx` file change (enforces standards, runs build) |
| **Brand Agent** | Colors, fonts, voice, visual identity | Any UI/content change (enforces 4-color system, font stack, voice guidelines) |
| **QA Agent** | Accessibility, Lighthouse, responsive | Any page or component change (WCAG AA, heading hierarchy, Lighthouse 95+) |
| **GitHub Agent** | Workflows, Actions, branch protection | Any `.github/` change, PR creation, deployment pipeline modification |
| **Prose Agent** | Human language, AI-ism detection | Any `.astro`, `.mdx`, `.md`, `.json` with visible text (em dashes, AI vocabulary, passive voice) |

#### Default Agent Behaviors
- **On every code PR:** Build Agent validates the build passes, Security Agent scans for vulnerabilities, Brand Agent checks color/font compliance, QA Agent verifies accessibility
- **On deployment changes:** Infra Agent validates Cloudflare config, GitHub Agent checks workflow syntax, Security Agent reviews secrets handling
- **On content changes:** Brand Agent enforces voice guidelines, QA Agent checks heading hierarchy and meta tags, Build Agent validates MDX frontmatter, Prose Agent enforces human language (no AI-isms)

### Quick Triggers
Type any trigger in your prompt to activate the matching specialist:
- `/architect` — Architecture review & structure validation
- `/audit` — Full brand compliance audit
- `/brandfix` — Find & fix brand color violations
- `/prettify` — Aesthetic polish with brand compliance
- `/seo` — SEO audit with prioritized fixes
- `/build` — Implement features, fix bugs, write code
- `/plan` — Requirements, prioritization, roadmap
- `/research` — Research, discovery, competitive analysis
- `/sprint` — Story creation, sprint planning
- `/qa` — Testing, audit, compliance checks
- `/frontend` — UI implementation (React/Vue/Astro)
- `/backend` — API design, server architecture
- `/infra` — Infrastructure, DNS, CDN, CI/CD, hosting
- `/security` — Security audit, vulnerability scanning, CSP
- `/github` — GitHub workflows, Actions, branch protection
- `/content` — Blog posts, copywriting, editorial
- `/growth` — Acquisition, viral loops, conversion
- `/brand` — Brand identity, consistency, positioning
- `/social` — Cross-platform social strategy
- `/ads` — PPC/paid media campaigns
- `/outbound` — Prospecting, cold outreach
- `/deals` — Deal strategy, pipeline, MEDDPICC
- `/proposal` — RFPs, proposals, win themes
- `/superpowers` — Full brainstorm → plan → execute → test → review workflow
- `/datamodel` — Data model and schema review
- `/api` — API endpoint review and validation

### Mode + Domain Triggers
Use a mode prefix + domain for fast, precise agent calls. Both symbol
and word prefixes work. See `docs/blueprints/rl-trigger-system-v1.md`
for the full spec.

**Modes:**
- `?` or `check` — Review only, no code changes (audit, report)
- `!` or `do` — Execute, make changes, produce commits
- `~` or `think` — Brainstorm, explore ideas, no changes

**Domains:** `code`, `brand`, `growth`, `ops`, `biz`, `plan`, `qa`

**Examples:** `?brand` (audit brand), `!code` (build feature),
`~growth` (brainstorm marketing), `check security` (security review)

### The Ship Gate
- Agents CAN commit locally but must NOT push to remote without `/ship`
- `/ship` — Runs all 7 default agents as gate check, then push + PR
- `/ship --force` — Push without gate checks (emergency only)
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
- **BMAD Method** — Agile AI development framework (https://github.com/bmad-code-org/BMAD-METHOD)
- **The Agency** — Specialized AI agent personalities (https://github.com/msitarzewski/agency-agents)
- **Superpowers** — Structured multi-step development workflow (https://github.com/obra/superpowers)

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
- `bmad-data-model.prompt.md` — Data model and schema review (*architect)
- `bmad-api-review.prompt.md` — API endpoint review (*architect)
- `bmad-audit.prompt.md` — Brand compliance audit (*qa)
- `bmad-brand-fix.prompt.md` — Fix brand color violations (*dev)
- `bmad-prettify.prompt.md` — Aesthetic polish (*dev + *qa)
- `bmad-seo.prompt.md` — SEO audit (*pm)
- `bmad-plan.prompt.md` — Requirements, prioritization, roadmap (*pm)
- `bmad-research.prompt.md` — Research and discovery (*analyst)
- `bmad-sprint.prompt.md` — Sprint planning and story creation (*sm)
- `bmad-build.prompt.md` — Feature implementation and code (*dev)
- `bmad-qa.prompt.md` — Testing, accessibility, Lighthouse (*qa)
- `bmad-prose.prompt.md` — Human language enforcement (Prose Agent)
- `bmad-security.prompt.md` — Threat detection, vulnerability scanning (Security Agent)
- `bmad-infra.prompt.md` — DNS, CDN, CI/CD, hosting (Infra Agent)
- `bmad-github.prompt.md` — Workflows, Actions, branch protection (GitHub Agent)

### Orchestration Frameworks (Future Integration)
See `docs/blueprints/rl-agent-frameworks-v1.md` for implementation guides:
- **LangGraph** — Graph-based Ship Gate and multi-stage workflows
- **CrewAI** — Productized multi-agent crews for service-tier delivery
- **Dotprompt** — Typed, versioned prompt templates for CI/CD integration
- **Contains Studio Agents** — Extended agent library for domain specialists
- **NotebookLM** — Per-client knowledge vault for diagnostics and context

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
