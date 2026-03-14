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

## Service Tiers (Canonical Names)
- Complete Analysis ($1,500-$3,000) - entry point, diagnostic engagement; 8 Ops Suite divisions (audit mode)
- Launch ($2,500-$5,000) - one-time project build; 8 Ops Suite divisions (build mode)
- Run ($500-$1,000/mo) - monthly retainer, 3-month min; 8 Ops Suite divisions (ops mode) + 1 Growth Division
- Scale ($1,000-$2,500/mo) - premium retainer, 6-month min; 8 Ops Suite divisions (ops mode) + 2 Growth Divisions

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
- tools/cli-anything-gimp/ - GIMP CLI harness (CLI-Anything, Python/Click)

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
- `/devops` — CI/CD, pipelines, infrastructure
- `/infra` — Infrastructure, DNS, CDN, CI/CD, hosting
- `/security` — Security audit, vulnerability scanning, CSP
- `/github` — GitHub workflows, Actions, branch protection
- `/ux` — User testing, usability, research
- `/content` — Blog posts, copywriting, editorial
- `/growth` — Acquisition, viral loops, conversion
- `/brand` — Brand identity, consistency, positioning
- `/social` — Cross-platform social strategy
- `/ads` — PPC/paid media campaigns
- `/outbound` — Prospecting, cold outreach
- `/deals` — Deal strategy, pipeline, MEDDPICC
- `/proposal` — RFPs, proposals, win themes
- `/coach` — Rep development, call review, training
- `/superpowers` — Full brainstorm → plan → execute → test → review workflow
- `/datamodel` — Data model and schema review
- `/api` — API endpoint review and validation
- `/prose` — Human language enforcement, AI-ism detection
- `/review` — Pre-ship senior code review
- `/discovery` — Discovery calls, qualifying, needs assessment
- `~retro` — Structured project retrospective
- `~biz-finance` — Business structure and entity planning (internal)
- `?biz-tools` — Tool stack audit and cost optimization (internal)
- `~plan-kpi` — Business metrics coaching (internal)
- `~plan-ceo-review` — Strategic vision review (internal)
- `~plan-eng-review` — Architecture maintainability review (internal)
- `/cli-anything` — Generate agent-native CLI for any software (7-phase pipeline)
- `/cli-anything gimp` — GIMP image processing via CLI-Anything harness
- `/council` — Multi-agent structured debate for strategic decisions
- `/council strategy` — Council preset: business direction
- `/council build` — Council preset: technical architecture
- `/council client` — Council preset: client delivery decisions
- `/council growth` — Council preset: marketing and acquisition
- `/council sales` — Council preset: deal strategy
- `/deep-research` — Multi-source trend intelligence (free/OSS tools)
- `/relay forge [client]` — Full Forge pipeline: research -> debate -> build -> gate -> deliver

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
- `/relay forge [client]` — Trend-aware build pipeline (research, council, build, gate, deliver)
- `/relay council` — Convene specialist agents for structured debate

### Frameworks
- **BMAD Method** — Agile AI development framework (https://github.com/bmad-code-org/BMAD-METHOD)
- **The Agency** — Specialized AI agent personalities (https://github.com/msitarzewski/agency-agents)
- **Superpowers** — Structured multi-step development workflow (https://github.com/obra/superpowers)
- **Contains Studio** — Department-organized agent specs (https://github.com/contains-studio/agents)
- **CrewAI** (Phase 2) — Multi-agent crew orchestration (https://github.com/crewAIInc/crewAI)
- **LangGraph** (Phase 3) — Graph-based workflow execution (https://github.com/langchain-ai/langgraph)
- **Dotprompt** (Phase 2) — Typed prompt templates (https://github.com/google/dotprompt)
- **CLI-Anything** — Agent-native CLI generation for any software (https://github.com/HKUDS/CLI-Anything)
- **LangChain** (Phase 2) — 700+ tool integrations, RAG chains, agent orchestration (https://github.com/langchain-ai/langchain)
- **awesome-scalability** — Scaling patterns and infrastructure knowledge base (https://github.com/binhnguyennus/awesome-scalability)
- **Perplexica** (Phase 1) — OSS Perplexity clone for Deep Research (https://github.com/ItzCrazyKns/Perplexica)
- **SearXNG** (Phase 1) — Meta-search backend for Perplexica (https://github.com/searxng/searxng)
- **Flowise** (Phase 1) — Visual LLM workflow builder (https://github.com/FlowiseAI/Flowise)
- **Activepieces** (Phase 1) — OSS workflow automation (https://github.com/activepieces/activepieces)
- **Ollama** (Phase 1) — Local LLM runner for offline work (https://github.com/ollama/ollama)

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
- `bmad-build.prompt.md` — Feature implementation, bug fixes (*dev)
- `bmad-plan.prompt.md` — Requirements & prioritization (*pm)
- `bmad-prettify.prompt.md` — Aesthetic polish (*dev + *qa)
- `bmad-qa.prompt.md` — Testing, audit & compliance (*qa)
- `bmad-research.prompt.md` — Research & discovery (*analyst)
- `bmad-seo.prompt.md` — SEO audit (*pm)
- `bmad-sprint.prompt.md` — Story creation & sprint planning (*sm)
- `bmad-prose.prompt.md` — Human language enforcement (Prose Agent)
- `bmad-infra.prompt.md` — DNS, CDN, CI/CD, hosting (Infra Agent)
- `bmad-security.prompt.md` — Threat detection, vulnerability scanning (Security Agent)
- `bmad-github.prompt.md` — Workflows, Actions, branch protection (GitHub Agent)
- `finance-founder-navigator.prompt.md` — Business entity & cashflow coaching (Internal)
- `finance-tools-coach.prompt.md` — Tool stack audit & cost optimization (Internal)
- `finance-kpi-explainer.prompt.md` — Business metrics translation (Internal)
- `relay-meta-roles.prompt.md` — CEO/Eng/Code Review/Retro overlays (Internal)
- `cli-anything.prompt.md` — CLI-Anything agent-native CLI generator
- `relay-forge.prompt.md` — Relay Forge trend-aware build pipeline (Layer 11)
- `relay-council.prompt.md` — Relay Council multi-agent debate engine (Layer 12)
- `relay-deep-research.prompt.md` — Deep Research multi-source intelligence (Layer 13)

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
- Image processing/GIMP → CLI-Anything GIMP Agent
- Strategy/decisions → Relay Council (`/council`)
- Trends/intelligence → Deep Research (`/deep-research`)
- Client onboarding → Relay Forge (`/relay forge [client]`)
- Business sectors → See `docs/agents.md` Business Sector Playbooks

## CLI-Anything Tools
Agent-native CLI harnesses for software automation. See `docs/agents.md` for
the full registry and `tools/cli-anything-*/` for installed packages.
- **GIMP CLI** (`cli-anything-gimp`) — Raster image processing: layers, filters, canvas, export
  - Install: `cd tools/cli-anything-gimp && pip install -e .`
  - Usage: `cli-anything-gimp --json project new --name poster --profile hd1080p -o poster.json`
  - Tests: `cd tools/cli-anything-gimp && pytest cli_anything/gimp/tests/ -v`
  - Workflow: `.github/workflows/cli-anything.yml`

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
