# AI Agents & Tools Registry — The Relay Method™

> **The Relay Method™** is RelayLaunch's branded approach to AI-assisted
> business operations. It unifies thirteen integrated frameworks — BMAD Method,
> The Agency, Superpowers, Contains Studio, CrewAI, LangGraph, Dotprompt,
> CLI-Anything, LangChain, awesome-scalability, Relay Forge, Relay Council,
> and Deep Research — into a single coordinated system with 280+ specialist
> agents, short trigger commands, roles mapped to real business functions,
> and cross-repo awareness. Every AI tool in the ecosystem (Claude Code,
> GitHub Copilot, Cursor) reads this file to route tasks to the right
> specialist. The system is a symbiote: it learns from every engagement,
> compounds improvements across clients, and self-optimizes quarterly.

---

## Default Agents — Always Active on Code Changes

These seven default agents activate **automatically** on every code change, deployment,
or infrastructure modification. No trigger needed. They represent the baseline
engineering team that protects every change going to production.

| Agent | Role | Auto-Triggers On | Key Checks |
|-------|------|-------------------|------------|
| **Infra Agent** | DNS, CDN, CI/CD, hosting, uptime | `.github/workflows/`, `wrangler.jsonc`, deployment config | Cloudflare config, DNS, edge deployment, build pipeline |
| **Security Agent** | Threats, CSP, dependency audit | Any code change | XSS, injection, secrets exposure, CSP headers, dependency CVEs |
| **Build Agent** | Code quality, testing, PR review | `.astro`, `.ts`, `.css`, `.mdx` changes | Build passes, code standards, TypeScript errors, MDX frontmatter |
| **Brand Agent** | Colors, fonts, voice, identity | Any UI/content change | 4-color system, font stack, voice guidelines, visual consistency |
| **QA Agent** | A11y, Lighthouse, responsive | Page/component changes | WCAG AA, heading hierarchy, Lighthouse 95+, mobile breakpoints |
| **GitHub Agent** | Workflows, Actions, branch protection | `.github/` changes, PRs, deploys | Workflow syntax, secret handling, action versions, CI/CD pipeline |
| **Prose Agent** | Human language, AI-ism detection | Any `.astro`, `.mdx`, `.md`, `.json` with visible text | Em dashes, AI vocabulary, passive voice, sentence length, voice compliance |

### How Default Agents Work
- **On every code PR:** Build Agent validates build, Security Agent scans for
  vulnerabilities, Brand Agent checks color/font compliance, QA Agent verifies
  accessibility
- **On deployment changes:** Infra Agent validates Cloudflare config, GitHub Agent
  checks workflow syntax, Security Agent reviews secrets handling
- **On content changes:** Brand Agent enforces voice guidelines, QA Agent checks
  heading hierarchy and meta tags, Build Agent validates MDX frontmatter,
  Prose Agent scans for AI-isms and enforces human language
- **On going live (production deploy):** All seven agents run a final gate check.
  Infra Agent confirms DNS/CDN, Security Agent runs a production scan, GitHub
  Agent validates the CI/CD pipeline ran green, Prose Agent confirms human voice

---

## Quick Triggers — Cheat Sheet

Type any trigger below in Claude Code, Copilot Chat, or any AI prompt to
instantly activate the matching specialist. Triggers are designed to be
short, memorable, and organized by business function.

### ⚡ One-Word Triggers (Fastest)

| Trigger | Specialist | What It Does |
|---------|-----------|--------------|
| `/architect` | BMAD *architect | Architecture review, structure validation |
| `/audit` | BMAD *qa | Full brand compliance audit |
| `/brandfix` | BMAD *dev (brand) | Find & fix brand color violations |
| `/prettify` | BMAD *dev + *qa | Aesthetic polish with brand compliance |
| `/seo` | BMAD *pm (SEO) | SEO audit with prioritized fixes |
| `/build` | BMAD *dev | Implement features, fix bugs, write code |
| `/plan` | BMAD *pm | Requirements, prioritization, roadmap |
| `/research` | BMAD *analyst | Research, discovery, competitive analysis |
| `/sprint` | BMAD *sm | Story creation, sprint planning, scrum |
| `/qa` | BMAD *qa | Testing, audit, compliance checks |
| `/frontend` | Agency Frontend Developer | React/Vue/Astro UI implementation |
| `/backend` | Agency Backend Architect | API design, server architecture |
| `/devops` | Agency DevOps Automator | CI/CD, pipelines, infrastructure |
| `/infra` | Infra Agent (Default) | DNS, CDN, CI/CD, hosting, uptime monitoring |
| `/security` | Security Agent (Default) | Threat modeling, vulnerability review, CSP |
| `/github` | GitHub Agent (Default) | Workflows, Actions, branch protection, CI/CD |
| `/ux` | Agency UX Researcher | User testing, usability, research |
| `/brand` | Brand Agent (Default) | Brand identity, consistency, positioning |
| `/content` | Agency Content Creator | Blog posts, copywriting, editorial |
| `/growth` | Agency Growth Hacker | Acquisition, viral loops, conversion |
| `/social` | Agency Social Media Strategist | Cross-platform social strategy |
| `/ads` | Agency PPC Campaign Strategist | Google/Meta/LinkedIn ad campaigns |
| `/discovery` | Agency Discovery Coach | Discovery calls, qualifying, needs assessment |
| `/outbound` | Agency Outbound Strategist | Prospecting, cold outreach, sequences |
| `/deals` | Agency Deal Strategist | MEDDPICC, pipeline, win strategy |
| `/proposal` | Agency Proposal Strategist | RFPs, proposals, win themes |
| `/coach` | Agency Sales Coach | Rep development, call review, training |
| `/superpowers` | Superpowers Workflow | Full brainstorm → plan → execute → test → review workflow |
| `/datamodel` | BMAD *architect | Data model and schema review |
| `/api` | BMAD *architect | API endpoint review and validation |
| `/prose` | Prose Agent (Default) | Human language enforcement, AI-ism detection |
| `/cro` | Conversion Architect | CRO, funnel psychology, A/B testing, page structure |
| `/behavioral` | Behavioral Designer | Cognitive science in design, visual hierarchy |
| `/buyer` | Buyer Psychologist | Purchase psychology, objection mapping, trust signals |
| `/neuro` | Neuromarketer | Attention, memory, anchoring, processing fluency |
| `/review` | Meta-Role Code Reviewer | Pre-ship senior code review |
| `/cli-anything` | CLI-Anything Pipeline | Generate agent-native CLI for any software |
| `/council` | Relay Council | Multi-agent structured debate for strategic decisions |
| `/deep-research` | Deep Research Agent | Multi-source trend intelligence using free/OSS tools |
| `/relay forge` | Relay Forge | 5-phase trend-aware build pipeline (research-debate-build-gate-deliver) |
| `~retro` | Meta-Role Retrospective | Structured project retrospective |
| `~biz-finance` | Finance Navigator (Internal) | Business structure and entity planning |
| `?biz-tools` | Tools Coach (Internal) | Tool stack audit and cost optimization |
| `~plan-kpi` | KPI Explainer (Internal) | Business metrics coaching |
| `~plan-ceo-review` | CEO Review (Internal) | Strategic vision review |
| `~plan-eng-review` | Eng Manager Review (Internal) | Architecture maintainability review |

### 🎯 Contextual Triggers (By Business Sector)

These longer triggers provide more context. Use them when you want the AI
to understand the business domain, not just the technical task.

**Website & Digital Presence:**
- `/relay website` — Full website operations (build, SEO, content, design)
- `/relay brand` — Brand standards enforcement across all touchpoints
- `/relay content` — Blog posts, case studies, service page copy
- `/relay performance` — Lighthouse scores, Core Web Vitals, load speed

**Client Delivery & Operations:**
- `/relay analysis` — Complete Analysis diagnostic engagement workflow
- `/relay launch` — Launch tier project build workflow
- `/relay run` — Run tier monthly retainer operations
- `/relay scale` — Scale tier premium growth operations

**Sales & Business Development:**
- `/relay pipeline` — Pipeline health, forecasting, deal review
- `/relay outreach` — Outbound prospecting and lead generation
- `/relay proposal` — Proposal writing, RFP responses, pricing
- `/relay discovery` — Discovery calls, qualifying, needs assessment

**Marketing & Growth:**
- `/relay seo` — Technical SEO, content SEO, local SEO
- `/relay social` — Social media strategy and content calendar
- `/relay ads` — Paid media campaigns and ad creative
- `/relay email` — Email marketing, sequences, newsletters

**Intelligence & Strategy:**
- `/relay forge [client]` — Full Forge pipeline: research, council, build, gate, deliver
- `/relay council` — Convene specialist agents for structured debate
- `/relay research-deep` — Multi-source trend intelligence gathering
- `/council strategy` — Council preset: business direction debate
- `/council build` — Council preset: technical architecture debate
- `/council client` — Council preset: client delivery decisions
- `/council growth` — Council preset: marketing and acquisition strategy
- `/council sales` — Council preset: deal strategy and pricing

**Infrastructure & Engineering:**
- `/relay arch` — Architecture review and technical decisions
- `/relay deploy` — Cloudflare Workers deployment, CI/CD
- `/relay security` — Security audit, vulnerability scanning
- `/relay data` — Database design, queries, data modeling
- `/relay golive` — Full production deployment gate (all 7 default agents run final checks)
- `/relay ci` — GitHub Actions workflow validation and CI/CD pipeline review
- `/relay optimize` — Agents review and improve their own prompt files
- `/cli-anything gimp` — GIMP image processing via CLI-Anything harness
- `/cli-anything <software>` — Generate new CLI harness (7-phase pipeline)
- `/ship` — Push to remote + create PR with full gate check by all 7 default agents

---

## Mode + Domain Trigger System

The Relay Method™ now supports a **Mode + Domain** shorthand for faster,
more precise agent activation. Use a mode prefix to tell the agent HOW
to behave, combined with a domain family for WHAT expertise to use.

### Operation Modes

Every interaction can start with a mode that controls agent behavior.
Both symbol and word prefixes are supported — they are equivalent.

| Symbol | Word | Mode | Behavior |
|--------|------|------|----------|
| `?` | `check` | **Check** | Read-only. Audit, review, report. No code changes. |
| `!` | `do` | **Do** | Execute. Write code, fix issues, produce commits. |
| `~` | `think` | **Think** | Brainstorm. Explore ideas, research, no changes. |

**Rules:**
- `check` mode agents must NEVER modify files — only read, analyze, report
- `think` mode agents must NEVER modify files — only discuss and propose
- `do` mode is the only mode that produces code changes
- If no mode is specified, the agent infers from context
- Modes work with ALL triggers (one-word, domain, contextual, service-tier)

### Domain Families

Seven memorable domains group agents by business function:

| Domain | Covers | Maps To |
|--------|--------|---------|
| **code** | Engineering, architecture, build, frontend, backend, APIs | `/architect`, `/build`, `/frontend`, `/backend`, `/datamodel`, `/api`, `/devops` |
| **brand** | Colors, fonts, voice, design, UI/UX, aesthetics | `/audit`, `/brandfix`, `/prettify`, `/brand`, `/ui`, `/ux` |
| **growth** | Marketing, SEO, content, social, ads, email | `/seo`, `/content`, `/growth`, `/social`, `/ads` |
| **ops** | Infrastructure, CI/CD, deployment, security, GitHub | `/infra`, `/security`, `/github` |
| **biz** | Sales, deals, proposals, pipeline, outbound | `/outbound`, `/deals`, `/proposal`, `/coach`, `/pipeline` |
| **plan** | Strategy, research, sprint planning, roadmap | `/plan`, `/research`, `/sprint` |
| **qa** | Testing, accessibility, Lighthouse, compliance | `/qa`, `/superpowers` |

### Usage Examples

| What You Type | What Happens |
|---------------|--------------|
| `?brand` or `check brand` | Audit brand compliance. Report only, no changes. |
| `!brand` or `do brand` | Fix all brand violations in code. |
| `~brand` or `think brand` | Brainstorm brand direction and messaging. |
| `?code` or `check code` | Architecture review, code quality audit. |
| `!code` or `do code` | Build features, fix bugs, write code. |
| `~growth` or `think growth` | Workshop marketing strategy and campaign ideas. |
| `?qa` or `check qa` | Full QA audit — accessibility, Lighthouse, responsive. |
| `!ops` or `do ops` | Fix deployment issues, update workflows. |
| `~biz` or `think biz` | Workshop deal strategy, explore pricing. |

Modes also work with specific triggers: `?seo`, `!brandfix`, `~architect`.

### Compatibility

This system is **additive** — all existing triggers work unchanged.
Mode + Domain is an optional layer for faster, clearer communication.

---

## The Ship Gate — Coordinating Multi-Agent Work

When multiple agents work in parallel, use the **Ship Gate** to prevent
premature pushes and ensure clean delivery.

### Rules

- Agents CAN commit locally at any time (incremental saves are fine)
- Agents must NOT push to remote without `/ship`
- Agents must NOT create PRs without `/ship`

### The `/ship` Command

When you type `/ship`, the following sequence runs:

1. **Freeze** — All agents stop making changes
2. **Gate check** — All 7 default agents run final review:
   - Build Agent: `npm run build` passes
   - Security Agent: No secrets, no injection vectors
   - Brand Agent: 4-color system, font stack, voice compliance
   - QA Agent: Accessibility, heading hierarchy, Lighthouse targets
   - Prose Agent: No AI-isms in text content
   - Infra Agent: Config files valid (if changed)
   - GitHub Agent: Workflow syntax valid (if changed)
3. **Report** — Results presented to you
4. **Push** — If all gates pass (or you override), push to remote
5. **PR** — Create PR with consolidated summary of all changes

### Emergency Override

- `/ship --force` — Push immediately, skip gate checks (use sparingly)

---

## Agent Self-Optimization — `/relay optimize`

Use the agents to review and improve their own instructions.

**Trigger:** `/relay optimize`
**Agents:** All BMAD lifecycle agents + default agents

### Workflow

1. **Self-audit** — Each agent reads its own prompt file, identifies gaps
2. **Cross-audit** — Each agent reads adjacent prompt files, finds overlaps
3. **Propose** — New versioned prompt files generated (e.g., `bmad-seo-v2`)
4. **Human review** — All proposals go through PR review (never auto-deploy)

Run quarterly or when adding new agents.

---

## Business Sector Playbooks

Pre-configured agent combinations and Forge presets for common client
verticals. Each sector maps to specific agents, research queries, and
deliverables. Use these to onboard new clients faster (80% reuse, 20%
customization per client).

### Wellness & Spa

| Phase | Agents | Deliverables |
|-------|--------|-------------|
| Discovery | `/deep-research` + `/discovery` | Competitor audit, booking tech comparison |
| Strategy | `/council client` | Service page structure, booking flow, GBP optimization plan |
| Build | `/relay launch` + `/prettify` | Custom site with booking widget, review schema, seasonal pages |
| Operate | `/relay run` + `/relay forge` | Monthly content, seasonal promos, trend-based service updates |

**Key automations:** Appointment booking (Calendly/Acuity), review request emails (n8n), seasonal landing pages, GBP post scheduling.

### Fitness & Training

| Phase | Agents | Deliverables |
|-------|--------|-------------|
| Discovery | `/deep-research` + `/discovery` | Class booking tech audit, social presence analysis |
| Strategy | `/council client` | Membership funnel, class schedule UX, retention strategy |
| Build | `/relay launch` + `/frontend` | Class booking integration, trainer profiles, progress tracking |
| Operate | `/relay run` + `/relay forge` | Social content calendar, member retention campaigns, seasonal challenges |

**Key automations:** Class reminders (n8n), new member welcome sequences (MailChimp), social proof collection, referral tracking.

### Local Restaurants

| Phase | Agents | Deliverables |
|-------|--------|-------------|
| Discovery | `/deep-research` + `/discovery` | Menu SEO audit, online ordering comparison, review analysis |
| Strategy | `/council client` | Menu page design, ordering flow, local SEO plan |
| Build | `/relay launch` + `/seo` | Menu pages with schema, online ordering setup, location pages |
| Operate | `/relay run` + `/relay forge` | Seasonal menu updates, review management, event promotion |

**Key automations:** Order notification routing (n8n), review response templates, seasonal menu page generation, event landing pages.

### Professional Services (Accountants, Lawyers, Consultants)

| Phase | Agents | Deliverables |
|-------|--------|-------------|
| Discovery | `/deep-research` + `/discovery` | Authority content audit, client acquisition channel analysis |
| Strategy | `/council client` | Content strategy, intake automation, client portal design |
| Build | `/relay launch` + `/content` | Authority blog, intake forms, resource library, client portal |
| Operate | `/relay run` + `/relay forge` | Monthly thought leadership, newsletter, SEO-driven content |

**Key automations:** Client intake forms (n8n), appointment scheduling, document request workflows, newsletter automation.

### Home Services (HVAC, Plumbing, Electrical, Landscaping)

| Phase | Agents | Deliverables |
|-------|--------|-------------|
| Discovery | `/deep-research` + `/discovery` | Service area analysis, competitor review funnel audit |
| Strategy | `/council client` | Service area page strategy, emergency page design, review funnel |
| Build | `/relay launch` + `/seo` | Service area pages, emergency service pages, review collection |
| Operate | `/relay run` + `/relay forge` | Seasonal campaign pages, review management, GBP optimization |

**Key automations:** Emergency request routing (n8n), review request sequences, seasonal service reminders, quote follow-ups.

### Retail & E-commerce

| Phase | Agents | Deliverables |
|-------|--------|-------------|
| Discovery | `/deep-research` + `/discovery` | Product page audit, local delivery feasibility, competitor analysis |
| Strategy | `/council client` | Product catalog structure, checkout flow, local delivery setup |
| Build | `/relay launch` + `/frontend` | Product pages, shopping cart, local delivery/pickup options |
| Operate | `/relay run` + `/relay forge` | Product updates, seasonal promotions, inventory sync |

**Key automations:** Order notifications (n8n), inventory alerts, abandoned cart emails, seasonal sale page generation.

### Healthcare & Dental

| Phase | Agents | Deliverables |
|-------|--------|-------------|
| Discovery | `/deep-research` + `/discovery` | Patient acquisition audit, telehealth platform comparison |
| Strategy | `/council client` | Patient portal design, appointment flow, HIPAA compliance review |
| Build | `/relay launch` + `/security` | Appointment booking, patient resources, HIPAA-compliant forms |
| Operate | `/relay run` + `/relay forge` | Health content calendar, patient education, seasonal wellness campaigns |

**Key automations:** Appointment reminders (n8n), patient intake forms, follow-up sequences, insurance verification workflows.

### Real Estate

| Phase | Agents | Deliverables |
|-------|--------|-------------|
| Discovery | `/deep-research` + `/discovery` | Market area analysis, competitor site audit, lead capture analysis |
| Strategy | `/council client` | Neighborhood page strategy, listing display, lead capture funnel |
| Build | `/relay launch` + `/seo` | Neighborhood pages, listing integration, lead capture forms |
| Operate | `/relay run` + `/relay forge` | Market update content, listing refresh, neighborhood guides |

**Key automations:** New listing alerts (n8n), lead nurture sequences, open house landing pages, market report generation.

### Education & Tutoring

| Phase | Agents | Deliverables |
|-------|--------|-------------|
| Discovery | `/deep-research` + `/discovery` | Platform comparison, parent acquisition channel analysis |
| Strategy | `/council client` | Course catalog design, booking flow, parent communication plan |
| Build | `/relay launch` + `/content` | Course pages, booking system, resource library, parent portal |
| Operate | `/relay run` + `/relay forge` | Educational content, seasonal enrollment campaigns, progress updates |

**Key automations:** Session booking (n8n), progress report generation, enrollment campaigns, parent communication sequences.

### Nonprofits

| Phase | Agents | Deliverables |
|-------|--------|-------------|
| Discovery | `/deep-research` + `/discovery` | Donor engagement audit, grant opportunity research |
| Strategy | `/council client` | Impact storytelling strategy, donation flow, volunteer portal |
| Build | `/relay launch` + `/content` | Impact pages, donation flow (Stripe), volunteer sign-up, event pages |
| Operate | `/relay run` + `/relay forge` | Impact reports, donor newsletters, event promotion, grant applications |

**Key automations:** Donation receipts (n8n + Stripe), volunteer onboarding sequences, event registration, donor thank-you workflows.

---

## The Relay Method™ — How It Works

The Relay Method™ organizes 280+ AI agents across thirteen integrated frameworks into these layers:

| Layer | Purpose | Source |
|-------|---------|--------|
| **1. BMAD Lifecycle Agents** | Structured agile roles for the full SDLC (plan, build, test, ship) | BMAD Method |
| **2. Agency Domain Specialists** | Deep-expertise personas for subject-matter knowledge | The Agency |
| **3. Contains Studio Specialists** | Department-organized agent specs (design, eng, marketing, ops) | Contains Studio |
| **4. Superpowers Workflow Engine** | Structured multi-step development workflow (brainstorm -> ship) | Superpowers |
| **5. CrewAI Orchestration** | Multi-agent crew orchestration for complex workflows | CrewAI |
| **6. LangGraph Workflows** | Graph-based workflow execution and state management | LangGraph |
| **7. LangChain Integrations** | 700+ tool integrations, RAG chains, agent orchestration | LangChain |
| **8. CLI-Anything Harnesses** | Agent-native CLI generation for any software | CLI-Anything |
| **9. Meta-Role Overlays & Finance** | Executive review, business health, KPI coaching | Internal |
| **10. RelayLaunch Business Context** | Service-tier workflows, brand standards, triggers, Ship Gate | Internal |
| **11. Relay Forge Engine** | Trend-aware build pipeline: research, debate, build, gate, deliver | Relay Forge |
| **12. Relay Council** | Multi-agent structured debate for strategic decisions | Relay Council |
| **13. Deep Research Intelligence** | Multi-source trend intelligence using free/OSS tools | Deep Research |
| **14. Behavioral Design & CRO** | Conversion psychology, cognitive science, buyer behavior, neuromarketing | Relay Behavioral |

### Layer 1: BMAD Lifecycle Agents
Structured agile roles that manage the full software development lifecycle.
These are the "process" agents — they know *how* to plan, build, test, and ship.

| Role | Trigger | Specialty | Prompt File |
|------|---------|-----------|-------------|
| *analyst | `/research` | Research & discovery | `bmad-research.prompt.md` |
| *pm | `/plan` | Requirements & prioritization | `bmad-plan.prompt.md` |
| *architect | `/architect` | Technical design & structure | `bmad-architect.prompt.md` |
| *architect | `/datamodel` | Data model & schema review | `bmad-data-model.prompt.md` |
| *architect | `/api` | API endpoint review & validation | `bmad-api-review.prompt.md` |
| *sm | `/sprint` | Story creation & sprint planning | `bmad-sprint.prompt.md` |
| *dev | `/build` | Implementation & code | `bmad-build.prompt.md` |
| *dev | `/brandfix` | Brand color violation fixes | `bmad-brand-fix.prompt.md` |
| *dev + *qa | `/prettify` | Aesthetic polish | `bmad-prettify.prompt.md` |
| *qa | `/qa` | Testing, audit & compliance | `bmad-qa.prompt.md` |
| *qa | `/audit` | Brand compliance audit | `bmad-audit.prompt.md` |

### Layer 2: Agency Domain Specialists
Deep-expertise personas that bring subject-matter knowledge. These are the
"what" agents — they know the craft inside and out.

### Layer 3: Superpowers Workflow Engine
Structured multi-step development workflow that enforces a systematic process
from brainstorming through shipping. Activated via `/superpowers`.

### Layer 4: RelayLaunch Business Context
Service-tier workflows and brand standards that ground every agent in
RelayLaunch's specific business model, pricing, voice, and client delivery.

---

## Installed Frameworks

### BMAD Method (BMM)

- **What:** AI-driven agile development framework with specialized agents and
  structured workflows for the full software lifecycle
- **Source:** <https://github.com/bmad-code-org/BMAD-METHOD>
- **Docs:** <https://docs.bmad-method.org>
- **Install:** `npx bmad-method install`
- **Help command:** Ask `bmad-help` for guidance on what to do next
- **Used in:** Both repos (relaylaunch-website, relaylaunch-control-center)

### The Agency (Agency Agents)

- **What:** Collection of specialized AI agent personalities — engineering,
  design, marketing, sales — each with deep domain expertise
- **Source:** <https://github.com/msitarzewski/agency-agents>
- **Install:** Clone the repo, then copy agents to `~/.claude/agents/` for
  Claude Code or run `./scripts/install.sh` from the cloned Agency repo
  to install for Cursor, Copilot, Aider, or Windsurf
- **Used in:** Both repos (relaylaunch-website, relaylaunch-control-center)

### Superpowers

- **What:** Full software development workflow system for coding agents
- **Source:** <https://github.com/obra/superpowers>
- **Install:** Plugin marketplace or manual setup
- **Philosophy:** Test-driven development, systematic processes, complexity reduction
- **Used in:** Both repos (relaylaunch-website, relaylaunch-control-center)

---

## Full Agent Roster by Category

### 🏗️ Architecture & Code Quality

| Trigger | Agent | Framework | How to Activate |
|---------|-------|-----------|-----------------|
| `/architect` | BMAD *architect | BMAD | `.github/prompts/bmad-architect.prompt.md` |
| `/datamodel` | BMAD *architect (data) | BMAD | `.github/prompts/bmad-data-model.prompt.md` |
| `/api` | BMAD *architect (API) | BMAD | `.github/prompts/bmad-api-review.prompt.md` |
| `/review` | Agency Code Reviewer | Agency | Activate "Code Reviewer" persona |
| `/security` | Agency Security Engineer | Agency | Activate "Security Engineer" persona |
| `/database` | Agency Database Optimizer | Agency | Activate "Database Optimizer" persona |
| `/gitflow` | Agency Git Workflow Master | Agency | Activate "Git Workflow Master" persona |
| `/sysdesign` | Agency Software Architect | Agency | Activate "Software Architect" persona |
| `/sre` | Agency SRE | Agency | Activate "SRE" persona |

**Also responds to:** architecture, structure, review, tech debt, code review,
PR review, maintainability, vulnerabilities, threat model, database, queries,
schema, indexing, git, branching, commits, system design, DDD, patterns,
reliability, SLOs, observability

### 💻 Frontend & Development

| Trigger | Agent | Framework | How to Activate |
|---------|-------|-----------|-----------------|
| `/build` | BMAD *dev | BMAD | `.github/prompts/bmad-build.prompt.md` |
| `/brandfix` | BMAD *dev (brand) | BMAD | `.github/prompts/bmad-brand-fix.prompt.md` |
| `/prettify` | BMAD *dev + *qa | BMAD | `.github/prompts/bmad-prettify.prompt.md` |
| `/frontend` | Agency Frontend Developer | Agency | Activate "Frontend Developer" persona |
| `/backend` | Agency Backend Architect | Agency | Activate "Backend Architect" persona |
| `/mobile` | Agency Mobile App Builder | Agency | Activate "Mobile App Builder" persona |
| `/prototype` | Agency Rapid Prototyper | Agency | Activate "Rapid Prototyper" persona |
| `/devops` | Agency DevOps Automator | Agency | Activate "DevOps Automator" persona |
| `/docs` | Agency Technical Writer | Agency | Activate "Technical Writer" persona |
| `/superpowers` | Superpowers Workflow | Superpowers | Activate full brainstorm → ship workflow |

**Also responds to:** implement, build, code, fix, component, brand fix, color
violations, CSS, prettify, polish, aesthetics, spacing, React, Vue, Angular,
UI, API, backend, server, microservice, mobile, iOS, Android, prototype, MVP,
CI/CD, pipeline, deploy, documentation

### 🎨 Design & Brand

| Trigger | Agent | Framework | How to Activate |
|---------|-------|-----------|-----------------|
| `/audit` | BMAD *qa | BMAD | `.github/prompts/bmad-audit.prompt.md` |
| `/ui` | Agency UI Designer | Agency | Activate "UI Designer" persona |
| `/ux` | Agency UX Researcher | Agency | Activate "UX Researcher" persona |
| `/brand` | Agency Brand Guardian | Agency | Activate "Brand Guardian" persona |
| `/story` | Agency Visual Storyteller | Agency | Activate "Visual Storyteller" persona |
| `/whimsy` | Agency Whimsy Injector | Agency | Activate "Whimsy Injector" persona |
| `/imageprompt` | Agency Image Prompt Engineer | Agency | Activate "Image Prompt Engineer" persona |

**Also responds to:** brand audit, compliance, colors, fonts, UI design,
component library, design system, UX, user testing, usability, brand identity,
consistency, positioning, visual story, multimedia, delight, micro-interactions,
AI images, Midjourney, DALL-E

### 🧠 Behavioral Design & CRO

| Trigger | Agent | Framework | How to Activate |
|---------|-------|-----------|-----------------|
| `/cro` | Conversion Architect | Relay | `.github/prompts/relay-behavioral-design.prompt.md` |
| `/behavioral` | Behavioral Designer | Relay | `.github/prompts/relay-behavioral-design.prompt.md` |
| `/buyer` | Buyer Psychologist | Relay | `.github/prompts/relay-behavioral-design.prompt.md` |
| `/neuro` | Neuromarketer | Relay | `.github/prompts/relay-behavioral-design.prompt.md` |

**Also responds to:** conversion, funnel, A/B testing, CRO, cognitive load,
visual hierarchy, font sizing, spacing, whitespace, Hick's Law, Fitts' Law,
buyer psychology, purchase decision, objection handling, anchoring, social proof,
neuromarketing, attention, memory, processing fluency, choice architecture

### 📈 SEO & Content

| Trigger | Agent | Framework | How to Activate |
|---------|-------|-----------|-----------------|
| `/seo` | BMAD *pm (SEO) | BMAD | `.github/prompts/bmad-seo.prompt.md` |
| `/content` | Agency Content Creator | Agency | Activate "Content Creator" persona |
| `/growth` | Agency Growth Hacker | Agency | Activate "Growth Hacker" persona |
| `/social` | Agency Social Media Strategist | Agency | Activate "Social Media Strategist" persona |
| `/twitter` | Agency Twitter Engager | Agency | Activate "Twitter Engager" persona |
| `/instagram` | Agency Instagram Curator | Agency | Activate "Instagram Curator" persona |
| `/tiktok` | Agency TikTok Strategist | Agency | Activate "TikTok Strategist" persona |
| `/reddit` | Agency Reddit Community Builder | Agency | Activate "Reddit Community Builder" persona |
| `/aso` | Agency App Store Optimizer | Agency | Activate "App Store Optimizer" persona |

**Also responds to:** SEO, meta tags, schema, sitemap, rankings, content, blog,
editorial, copywriting, growth, acquisition, viral, conversion, social media,
Twitter, LinkedIn, thought leadership, Instagram, TikTok, Reddit, community

### 📊 Planning & Project Management

| Trigger | Agent | Framework | How to Activate |
|---------|-------|-----------|-----------------|
| `/plan` | BMAD *pm | BMAD | `.github/prompts/bmad-plan.prompt.md` |
| `/research` | BMAD *analyst | BMAD | `.github/prompts/bmad-research.prompt.md` |
| `/sprint` | BMAD *sm | BMAD | `.github/prompts/bmad-sprint.prompt.md` |
| `/qa` | BMAD *qa | BMAD | `.github/prompts/bmad-qa.prompt.md` |

**Also responds to:** requirements, prioritize, roadmap, backlog, research,
discovery, analysis, sprint, stories, scrum, test, audit, compliance

### 💰 Paid Media & Advertising

| Trigger | Agent | Framework | How to Activate |
|---------|-------|-----------|-----------------|
| `/ads` | Agency PPC Campaign Strategist | Agency | Activate "PPC Campaign Strategist" persona |
| `/searchterms` | Agency Search Query Analyst | Agency | Activate "Search Query Analyst" persona |
| `/adaudit` | Agency Paid Media Auditor | Agency | Activate "Paid Media Auditor" persona |
| `/tracking` | Agency Tracking Specialist | Agency | Activate "Tracking & Measurement Specialist" persona |
| `/adcopy` | Agency Ad Creative Strategist | Agency | Activate "Ad Creative Strategist" persona |
| `/display` | Agency Programmatic Buyer | Agency | Activate "Programmatic & Display Buyer" persona |
| `/paidsocial` | Agency Paid Social Strategist | Agency | Activate "Paid Social Strategist" persona |

**Also responds to:** PPC, Google Ads, bidding, ad spend, search queries,
negative keywords, ad audit, account review, tracking, GTM, GA4, conversions,
ad copy, creative, RSA, Performance Max, display, programmatic, DSP, ABM,
Meta Ads, LinkedIn Ads, TikTok Ads

### 🤝 Sales & Business Development

| Trigger | Agent | Framework | How to Activate |
|---------|-------|-----------|-----------------|
| `/outbound` | Agency Outbound Strategist | Agency | Activate "Outbound Strategist" persona |
| `/discovery` | Agency Discovery Coach | Agency | Activate "Discovery Coach" persona |
| `/deals` | Agency Deal Strategist | Agency | Activate "Deal Strategist" persona |
| `/saleseng` | Agency Sales Engineer | Agency | Activate "Sales Engineer" persona |
| `/proposal` | Agency Proposal Strategist | Agency | Activate "Proposal Strategist" persona |
| `/pipeline` | Agency Pipeline Analyst | Agency | Activate "Pipeline Analyst" persona |
| `/accounts` | Agency Account Strategist | Agency | Activate "Account Strategist" persona |
| `/coach` | Agency Sales Coach | Agency | Activate "Sales Coach" persona |

**Also responds to:** outbound, prospecting, cold outreach, discovery calls,
qualifying, SPIN, deal strategy, MEDDPICC, pipeline, demo, POC, pre-sales,
battlecard, proposal, RFP, win themes, forecast, pipeline health, RevOps,
account planning, expand, QBR, NRR, coaching, rep development, call review

---

## BMAD Prompt Files in This Repo

Copilot prompt files live in `.github/prompts/` and are activated
automatically when referenced. Claude Code reads them via `CLAUDE.md`.

| Agent | Role | Prompt File | Trigger | Purpose |
|-------|------|-------------|---------|---------|
| *architect | Technical design | `bmad-architect.prompt.md` | `/architect` | Architecture review, structure validation |
| *architect | Data model | `bmad-data-model.prompt.md` | `/datamodel` | Data model and schema review |
| *architect | API review | `bmad-api-review.prompt.md` | `/api` | API endpoint review and validation |
| *analyst | Research | `bmad-research.prompt.md` | `/research` | Research, discovery, competitive analysis |
| *pm | Requirements | `bmad-plan.prompt.md` | `/plan` | Requirements, prioritization, roadmap |
| *sm | Sprint planning | `bmad-sprint.prompt.md` | `/sprint` | Story creation, sprint planning, scrum |
| *dev | Implementation | `bmad-build.prompt.md` | `/build` | Implement features, fix bugs, write code |
| *dev | Brand fixes | `bmad-brand-fix.prompt.md` | `/brandfix` | Find and fix brand color violations |
| *dev + *qa | Polish | `bmad-prettify.prompt.md` | `/prettify` | Aesthetic improvements with brand compliance |
| *qa | Testing & audit | `bmad-audit.prompt.md` | `/audit` | Full brand compliance audit |
| *qa | QA & compliance | `bmad-qa.prompt.md` | `/qa` | Testing, audit, compliance checks |
| *pm | SEO | `bmad-seo.prompt.md` | `/seo` | SEO audit with prioritized fixes |
| Prose Agent | Language | `bmad-prose.prompt.md` | _(default, auto-triggers on content changes)_ | Human language enforcement, AI-ism detection |
| Infra Agent | Infrastructure | `bmad-infra.prompt.md` | `/infra` | DNS, CDN, CI/CD, hosting review |
| Security Agent | Security | `bmad-security.prompt.md` | `/security` | Threat detection, vulnerability scanning, CSP |
| GitHub Agent | GitHub | `bmad-github.prompt.md` | `/github` | Workflows, Actions, branch protection |
| Relay Forge | Forge Engine | `relay-forge.prompt.md` | `/relay forge` | Trend-aware build pipeline |
| Relay Council | Decision Engine | `relay-council.prompt.md` | `/council` | Multi-agent structured debate |
| Deep Research | Intelligence | `relay-deep-research.prompt.md` | `/deep-research` | Multi-source trend research |
| Conversion Architect | CRO | `relay-behavioral-design.prompt.md` | `/cro` | Conversion optimization, funnel psychology |
| Behavioral Designer | Cognitive design | `relay-behavioral-design.prompt.md` | `/behavioral` | Visual hierarchy, spacing, cognitive load |
| Buyer Psychologist | Purchase psychology | `relay-behavioral-design.prompt.md` | `/buyer` | Buyer personas, objection mapping, trust signals |
| Neuromarketer | Neuromarketing | `relay-behavioral-design.prompt.md` | `/neuro` | Attention, anchoring, memory, processing fluency |
| Backend Architect | Backend | `agency-backend-architect.prompt.md` | `/backend` | Cloudflare/D1/n8n stack architecture |
| Brand Guardian | Brand | `agency-brand-guardian.prompt.md` | `/brand` | 4-color system, typography, voice enforcement |
| Content Creator | Content | `agency-content-creator.prompt.md` | `/content` | Blog posts, service pages, case studies |
| DevOps Automator | DevOps | `agency-devops-automator.prompt.md` | `/devops` | GitHub Actions + Cloudflare Workers |
| Frontend Developer | Frontend | `agency-frontend-developer.prompt.md` | `/frontend` | Astro 5, Tailwind 4.2, Starwind |
| Growth Hacker | Growth | `agency-growth-hacker.prompt.md` | `/growth` | Funnel architecture, channel strategy |
| Proposal Strategist | Sales | `agency-proposal-strategist.prompt.md` | `/proposal` | Win themes, value-based pricing |

### Adding New Prompt Files

Create a file in `.github/prompts/` with this format:

```markdown
---
mode: agent
description: "BMAD *role agent — Short description"
---

# Task Title — *role Agent

You are the BMAD *role agent. [Instructions...]
```

---

## Superpowers Integration

When complex multi-step tasks arise, use `/superpowers` to activate the
structured workflow:

### Phases

1. **Brainstorm** — Refine ideas through clarifying questions before coding
2. **Plan** — Break work into small, testable tasks (2-5 min each)
3. **Execute** — Implement tasks with review checkpoints using subagents
4. **Test** — RED-GREEN-REFACTOR test-driven methodology
5. **Review** — Validate work against the implementation plan
6. **Finish** — Handle branch merging and cleanup

### When to Use

- New feature implementations spanning multiple files
- Refactoring tasks that touch core architecture
- Bug fixes requiring systematic debugging
- Any task that benefits from structured planning

### Combo Triggers

- `/superpowers` + `/architect` → Structured architecture design with planning
- `/superpowers` + `/build` → TDD feature implementation with review checkpoints
- `/superpowers` + `/qa` → Systematic audit with test-driven validation

---

## RelayLaunch Specialist Roles

These are RelayLaunch-specific specialist combinations that pair the right
agents together for common business workflows. Use these when working on
RelayLaunch client deliverables or internal operations.

### 🎖️ Complete Analysis Specialist
**Trigger:** `/relay analysis`
**Agents:** BMAD *analyst + *pm + Agency UX Researcher
**When:** Running an 8-area business infrastructure diagnostic for a client.
**Workflow:**
1. *analyst researches the client's current tech stack and digital presence
2. UX Researcher evaluates user experience across all client touchpoints
3. *pm prioritizes findings into a 20-30 page report with roadmap

### 🚀 Launch Specialist
**Trigger:** `/relay launch`
**Agents:** BMAD *architect + *dev + Agency Frontend Developer + DevOps Automator
**When:** Building a client's full infrastructure from scratch (website,
automations, email, social, dashboard).
**Workflow:**
1. *architect designs the system and defines component structure
2. Frontend Developer and *dev implement the build
3. DevOps Automator sets up CI/CD, hosting, and monitoring

### 🔄 Run Operations Specialist
**Trigger:** `/relay run`
**Agents:** BMAD *pm + *qa + Agency Content Creator + SEO (BMAD *pm)
**When:** Managing a client's monthly retainer — content, SEO, monitoring.
**Workflow:**
1. *pm plans the monthly deliverables and priorities
2. Content Creator produces blog posts, social content, and copy
3. BMAD *pm (SEO) audits and optimizes search performance
4. *qa audits brand compliance on all new content

### 📈 Scale Growth Specialist
**Trigger:** `/relay scale`
**Agents:** BMAD *pm + Agency Growth Hacker + PPC Strategist + Content Creator
**When:** Running a premium growth retainer — expanded deliverables, advanced builds.
**Workflow:**
1. *pm sets quarterly growth OKRs and sprint plans
2. Growth Hacker designs experiments and conversion funnels
3. PPC Campaign Strategist manages paid acquisition channels
4. Content Creator produces high-volume content assets

### 🛡️ Brand Guardian Specialist
**Trigger:** `/relay brand`
**Agents:** BMAD *qa + *dev (brand) + Agency Brand Guardian
**When:** Enforcing brand standards across all code, content, and design.
**Workflow:**
1. *qa audits the entire codebase for brand violations
2. *dev (brand) fixes any color, font, or style violations
3. Brand Guardian reviews positioning and messaging consistency

### 🔍 SEO & Performance Specialist
**Trigger:** `/relay performance`
**Agents:** BMAD *pm (SEO) + *architect + Agency Growth Hacker
**When:** Optimizing site performance, Core Web Vitals, and search rankings.
**Workflow:**
1. SEO *pm audits all pages for meta tags, schema, and content gaps
2. *architect reviews performance architecture (bundle size, lazy loading)
3. Growth Hacker identifies conversion optimization opportunities

---

## Founder-Only Finance Agents (Internal Use Only)

> These agents exist to help Victor think clearly about RelayLaunch's own
> business finances, tools, and metrics. They are **not** client-facing,
> we do not market on the website, and they must never present output as legal,
> tax, or investment advice.

### 💰 Founder Finance Navigator
**Trigger:** `~biz-finance` or `think finance`
**File:** `.github/prompts/finance-founder-navigator.prompt.md`
**Role:** Explain business entity options, cashflow concepts, and tax/logistics
considerations in plain language. Prepare checklists and questions for CPAs,
attorneys, and bookkeepers.
**Use when:** Considering entity changes, pricing decisions, or how to structure
pay/reinvestment.

### 🔧 Small Biz Expense & Tools Coach
**Trigger:** `?biz-tools` or `check tools`
**File:** `.github/prompts/finance-tools-coach.prompt.md`
**Role:** Audit your tool and subscription stack. Categorize each as keep/monitor/
downgrade/replace/cancel. Suggest alternatives from the free-for-dev ecosystem.
Estimate savings.
**Use when:** Reducing monthly burn, consolidating overlapping tools, or evaluating
a new paid tool.

### 📊 Founder KPI Explainer
**Trigger:** `~plan-kpi` or `think kpi`
**File:** `.github/prompts/finance-kpi-explainer.prompt.md`
**Role:** Explain core metrics (MRR, runway, utilization, project vs retainer mix)
in terms that fit a tiny AI services studio. Suggest which 3-5 metrics to track
and simple ways to track them.
**Use when:** Sanity-checking revenue targets, deciding which offers to emphasize,
or designing a personal runway plan.

### Finance Agent Rules
- These triggers are reserved for the founder only.
- We do not use these in client projects, proposals, or website copy.
- If you repurpose outputs for content (blog posts, educational material), strip
  personal numbers and re-phrase for general audiences.
- All outputs carry the disclaimer: "Not legal or tax advice."

---

## Meta-Role Overlays (Internal Use Only)

> Strategic review personas that overlay on top of existing Relay agents.
> They add executive-level perspective for big decisions.
> Source inspiration: gstack (https://github.com/garrytan/gstack)

### 🎯 CEO / Vision Review
**Trigger:** `~plan-ceo-review`
**File:** `.github/prompts/relay-meta-roles.prompt.md`
**Role:** Challenge assumptions, ask hard questions about direction, timing, and
trade-offs. Produce a "Founder Review" with strengths, concerns, and alternatives.

### 🏗️ Engineering Manager / Staff Engineer Review
**Trigger:** `~plan-eng-review`
**File:** `.github/prompts/relay-meta-roles.prompt.md`
**Role:** Evaluate architecture decisions for a solo founder. Check for
over-engineering, assess maintainability, and suggest simplifications.

### 🔍 Code Review (Pre-Ship)
**Trigger:** `?code-review` or `/review`
**File:** `.github/prompts/relay-meta-roles.prompt.md`
**Role:** Senior code review before `/ship`. Catch logic errors, naming confusion,
dead code, and issues automated linters miss.

### 🔄 Retrospective Facilitator
**Trigger:** `~retro`
**File:** `.github/prompts/relay-meta-roles.prompt.md`
**Role:** Guide structured reflection on completed projects. Extract actionable
improvements for processes, tools, and agent workflows.

### Meta-Role Rules
- Overlays only; they produce reports and recommendations.
- Never auto-execute changes (think/check modes only).
- Can be used on client projects for premium "Strategic Review" deliverables.

---

## External Resources & Future Verticals

> External repos, tools, and research catalogs that feed into the Relay Method.
> Documented here so all AI tools know what's available.

| Resource | GitHub | Status | Use In Relay |
|----------|--------|--------|--------------|
| **gstack** | [garrytan/gstack](https://github.com/garrytan/gstack) | Reference | Meta-role overlays for CEO/Eng review |
| **claude-skills** | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | Phase 1 | Atomic micro-skills for agent prompts |
| **free-for-dev** | [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev) | Research | Tools Coach and Complete Analysis alternatives |
| **Contains Studio** | [contains-studio/agents](https://github.com/contains-studio/agents) | Phase 1 | 30+ specialist agents to port |
| **OpenBB** | [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | Future | Founder finance data helpers |
| **MindsDB** | [mindsdb/mindsdb](https://github.com/mindsdb/mindsdb) | Future | Control Center data agents |
| **GLM-5** | [docs.z.ai](https://docs.z.ai/guides/llm/glm-5) | Future | Infra super-architect second opinions |
| **http.zig** | [karlseguin/http.zig](https://github.com/karlseguin/http.zig) | Future | Ultra-lean edge microservices |
| **LangGraph** | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | Phase 3 | Ship Gate and build flow graphs |
| **CrewAI** | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | Phase 2 | Service-tier multi-agent crews |
| **Dotprompt** | [google/dotprompt](https://github.com/google/dotprompt) | Phase 2 | Typed audit/report templates |
| **LangChain** | [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | Phase 2 | 700+ tool integrations, RAG chains, agent orchestration |
| **awesome-scalability** | [binhnguyennus/awesome-scalability](https://github.com/binhnguyennus/awesome-scalability) | Active | Scaling patterns, infra knowledge base (400+ resources) |
| **Perplexica** | [ItzCrazyKns/Perplexica](https://github.com/ItzCrazyKns/Perplexica) | Phase 1 | OSS Perplexity clone for Deep Research (self-hosted, $0) |
| **SearXNG** | [searxng/searxng](https://github.com/searxng/searxng) | Phase 1 | Meta-search backend for Perplexica (70+ engines) |
| **Morphic** | [miurla/morphic](https://github.com/miurla/morphic) | Phase 1 | Secondary OSS search engine for Forge validation |
| **Flowise** | [FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise) | Phase 1 | Visual LLM workflow builder for client demos |
| **Activepieces** | [activepieces/activepieces](https://github.com/activepieces/activepieces) | Phase 1 | OSS workflow automation (450+ integrations) |
| **Ollama** | [ollama/ollama](https://github.com/ollama/ollama) | Phase 1 | Local LLM runner for offline/privacy-sensitive work |
| **Langflow** | [logspace-ai/langflow](https://github.com/logspace-ai/langflow) | Phase 2 | Visual LangChain builder for Forge graph prototyping |

---

## Agent Count Summary

### Public-Facing Agents (Website)

The website showcases **11 divisions** organized into two categories:

### Relay Method Ops Suite (8 divisions, included in every tier)

| # | Division | Agent Count | Public Role |
|---|----------|-------------|-------------|
| 1 | **Infrastructure Command** | 18 | DNS, CDN, hosting, uptime |
| 2 | **Security Division** | 14 | Threat detection, vulnerability scanning |
| 3 | **Engineering Corps** | 28 | Code quality, testing, PR review |
| 4 | **Content Studio** | 32 | Blog, email, SEO, copywriting |
| 5 | **Brand & Design Lab** | 20 | Colors, fonts, voice, identity |
| 6 | **Ops & Automation** | 8 | CI/CD, workflows, integrations |
| 7 | **QA & Compliance** | 10 | Accessibility, Lighthouse, standards |
| 8 | **Strategy & Planning** | 8 | Research, roadmaps, sprint planning |

### Growth Divisions (3 divisions, unlocked in Run/Scale retainers)

| # | Division | Agent Count | Public Role | Unlocked In |
|---|----------|-------------|-------------|-------------|
| 9 | **Growth Engine** | 30 | Acquisition, conversion, analytics | Run (+1) or Scale (+2) |
| 10 | **Sales & Pipeline** | 12 | Outbound, proposals, pipeline | Run (+1) or Scale (+2) |
| 11 | **Social Media Command** | 10 | Cross-platform strategy, engagement | Run (+1) or Scale (+2) |

### Tier Packaging

| Tier | Ops Suite | Growth Divisions | Total Agent Access |
|------|-----------|-----------------|-------------------|
| Complete Analysis | 8 (audit mode) | 0 | ~180 |
| Launch | 8 (build mode) | 0 | ~180 |
| Run | 8 (ops mode) | +1 (client picks 1 of 3) | ~210-220 |
| Scale | 8 (ops mode) | +2 (client picks 2 of 3) | ~240-252 |

### Internal-Only Agents (Not on Website)

| Agent | Domain | Trigger |
|-------|--------|---------|
| Founder Finance Navigator | biz | `~biz-finance` |
| Small Biz Expense & Tools Coach | biz | `?biz-tools` |
| Founder KPI Explainer | plan | `~plan-kpi` |
| CEO / Vision Review | plan | `~plan-ceo-review` |
| Engineering Manager Review | code | `~plan-eng-review` |
| Code Review (Pre-Ship) | code | `?code-review` |
| Retrospective Facilitator | plan | `~retro` |

### Total Agent Ecosystem

| Category | Count |
|----------|-------|
| Default agents (always-on) | 7 |
| BMAD + Relay prompt files | 32 |
| Finance agents (internal) | 3 |
| Meta-role overlays (internal) | 4 |
| Agency domain specialists | 30+ |
| Contains Studio specialists (Phase 1) | 30+ |
| CrewAI service-tier crews (Phase 2) | 4 |
| CLI-Anything harnesses | 1 (GIMP) |
| LangChain tool agents (Phase 2) | 50+ |
| awesome-scalability patterns | 10 |
| Relay Forge pipeline agents | 5 |
| Relay Council presets | 5 |
| Deep Research tool integrations | 8 |
| Business sector playbooks | 10 |
| Behavioral Design & CRO agents | 4 |
| Total named triggers | 80+ |
| Total specialist agents | 300+ |

---

## Cross-Repo Agent Setup

Both `relaylaunch-website` and `relaylaunch-control-center` should maintain
a copy of this file at `docs/agents.md` so AI tools in either repo know the
full agent roster. The website repo is the source of truth for this file.

When setting up a new repo in the RelayLaunch ecosystem:

1. Copy `docs/agents.md` into the new repo
2. Add BMAD prompt files to `.github/prompts/` as needed
3. Reference agents in `CLAUDE.md` and `.github/copilot-instructions.md`
4. Install frameworks: `npx bmad-method install` and copy Agency agents

---

## CLI-Anything — Agent-Native Software CLIs

The Relay Method™ integrates [CLI-Anything](https://github.com/HKUDS/CLI-Anything),
the open-source framework that turns any software into an agent-friendly CLI.
CLI-Anything generates complete Python CLI harnesses using a 7-phase pipeline:
Analyze, Design, Implement, Plan Tests, Write Tests, Document, Publish.

### Installed CLI Harnesses

| Software | CLI Command | Location | Status |
|----------|------------|----------|--------|
| **GIMP** | `cli-anything-gimp` | `tools/cli-anything-gimp/` | Installed |

### GIMP CLI Agent

The GIMP CLI agent provides raster image processing via a stateful CLI with
layers, filters, canvas manipulation, and export. It runs on Pillow with
optional GIMP batch mode as fallback.

**Command Groups:** `project`, `layer`, `canvas`, `filter`, `media`, `export`, `draw`, `session`

**Triggers:**
- `/cli-anything gimp` — Activate GIMP CLI agent for image processing tasks
- `/cli-anything` — Generate a new CLI harness for any software (7-phase pipeline)

**Capabilities:**
- 14 canvas presets (HD, 4K, social media, print)
- 24+ filters (adjustment, blur, stylize, transform)
- 15 blend modes with numpy compositing
- 13 export presets (PNG, JPEG, WebP, TIFF, PDF, etc.)
- Session persistence with 50-step undo/redo
- Dual output: human-readable or `--json` for agent consumption
- Interactive REPL mode via prompt-toolkit

**Installation:**
```bash
cd tools/cli-anything-gimp && pip install -e .
```

### Adding New CLI Harnesses

To generate a CLI for new software using the CLI-Anything methodology:

1. Run `/cli-anything <software>` to start the 7-phase pipeline
2. Output goes to `tools/cli-anything-<software>/`
3. Register the new harness in this table
4. Add trigger to Quick Triggers section
5. Update `CLAUDE.md` with the new CLI tool reference

---

## Relay Forge — Trend-Aware Build Engine (Layer 11)

The Relay Forge is a 5-phase pipeline that turns market intelligence into
concrete client deliverables. It compounds improvements across engagements.

**Trigger:** `/relay forge [client-name]`
**Prompt File:** `.github/prompts/relay-forge.prompt.md`

### Pipeline Phases

1. **Deep Research** (`/deep-research`) — Pull live trends from free tools
2. **Council Debate** (`/council`) — 5-7 agents debate what to build
3. **Task Provisioning** — Convert verdict into agent assignments
4. **Ship Gate** — Standard 7-agent gate check on all changes
5. **Deliver and Log** — Push, dashboard update, archive for learning

### Forge Pricing by Tier

| Tier | Forge Frequency | Upsell |
|------|----------------|--------|
| Complete Analysis | One-time trend snapshot | Included in diagnostic |
| Launch | Trend-informed build | During project |
| Run | Monthly cycle | $100-250/mo add-on |
| Scale | Bi-weekly cycle | Included |
| AI Operations Partner | Weekly cycle | Included |

---

## Relay Council — Multi-Agent Decision Engine (Layer 12)

Structured adversarial debate among specialist agents. Every strategic
recommendation gets stress-tested before execution.

**Trigger:** `/council` | `/relay council`
**Prompt File:** `.github/prompts/relay-council.prompt.md`

### Council Presets

| Preset | Trigger | Seated Agents |
|--------|---------|---------------|
| Strategy | `/council strategy` | CEO Review, Growth, Finance, Brand, Content |
| Build | `/council build` | Architect, Build, Security, UX, Eng Manager |
| Client | `/council client` | Growth, Content, SEO, UX, Brand |
| Growth | `/council growth` | Growth, SEO, Content, Social, Ads |
| Sales | `/council sales` | Deals, Discovery, Proposal, Coach, CEO Review |

### Council Output

Every session produces a Verdict:
1. Consensus points (where agents agreed)
2. Key disagreements (where they split and why)
3. Ranked recommendations (top 3 by impact/effort)
4. Dissenting views (preserved, not dismissed)
5. Decision for the founder (options laid out)

---

## Deep Research — Trend Intelligence (Layer 13)

Multi-source market intelligence using free and open-source search tools.
Phase 1 of the Relay Forge pipeline.

**Trigger:** `/deep-research` | `/relay research-deep`
**Prompt File:** `.github/prompts/relay-deep-research.prompt.md`

### Free Research Tool Stack

| Tool | Cost | Monthly Limit | Best For |
|------|------|---------------|----------|
| **Perplexica** (self-hosted) | $0 ongoing | Unlimited | General research with citations |
| **SearXNG** | $0 (self-hosted) | Unlimited | Meta-search across 70+ engines |
| **Serper.dev** | $0 | 2,500 searches | Google SERP and keyword research |
| **Brave Search API** | $0 | 2,000 queries | Independent index, no Google dependency |
| **Tavily** | $0 | 1,000 searches | AI-optimized trend signals |
| **Firecrawl** | $0 | 500 pages | Competitor site crawling |
| **Morphic** (self-hosted) | $0 | Unlimited | Secondary search validation |
| **Google Trends** | $0 | Unlimited | Seasonal patterns |

**Total research cost:** $6-10/mo (VPS for self-hosted tools only).

---

## Free & Low-Cost Tool Stack

Complete list of free tools that power the Relay Method ecosystem. These
replace $330-600/mo of typical small business SaaS spend with under $51/mo.

### Your Operating Stack (What RelayLaunch Pays)

| Tool | Plan | Monthly Cost |
|------|------|-------------|
| Cloudflare Pages | Free | $0 |
| n8n (self-hosted) | VPS | $6-10 |
| MailChimp | Free (<500 contacts) | $0 |
| Buffer | Free (3 channels) | $0 |
| GitHub | Free | $0 |
| Stripe | 2.9% + $0.30/txn | Pay-per-use |
| Calendly | Free | $0 |
| Claude Pro | Pro | $20 |
| Domain | Annual | ~$1 |
| **Total** | | **~$27-31/mo** |

### Client Stack (What They Pay After Handoff)

| Tool | Plan | Monthly Cost |
|------|------|-------------|
| Cloudflare Pages | Free | $0 |
| n8n VPS | Self-hosted | $6-10 |
| MailChimp | Essentials | $13-45 |
| Buffer | Essentials | $6-18 |
| Calendly | Free/Premium | $0-8 |
| Stripe | 2.9% + $0.30 | Pay-per-use |
| **Total** | | **$25-81/mo** |

**Savings vs. typical stack:** $280-550/mo saved ($3,360-6,600/yr).
Lead every proposal with this number.

### Additional Free AI/Automation Tools

| Tool | What It Does | Relay Use |
|------|-------------|-----------|
| **Ollama** | Run LLMs locally (LLaMA, Mistral, DeepSeek) | Offline audits for privacy-sensitive clients |
| **Open WebUI** | Chat interface for Ollama | Test local agents before deploying |
| **Flowise** | Drag-drop LLM workflow builder | Visual agent builder for client demos |
| **Activepieces** | OSS workflow automation (450+ integrations) | n8n alternative for no-code client flows |
| **Whisper** | Free speech-to-text | Transcribe discovery calls |
| **Langflow** | Visual LangChain/agent builder | Prototype Forge graphs before LangGraph |

---

## About The Relay Method™

The Relay Method™ is a proprietary framework developed by RelayLaunch LLC
for orchestrating AI agents across the full spectrum of digital business
operations, from code to content to client delivery.

It combines:
- **BMAD Method** for structured agile development lifecycle
- **The Agency** for deep domain specialist expertise
- **Superpowers** for systematic multi-step development workflows
- **Contains Studio** for department-organized specialist agents
- **RelayLaunch business context** for service-tier workflows and brand standards
- **Mode + Domain** trigger system for precise, memorable agent activation
- **Ship Gate** for coordinated multi-agent delivery
- **Prose Agent** for human language enforcement on every change
- **Meta-Role Overlays** for executive-level strategic review
- **Founder Finance Agents** for internal business health and clarity
- **Relay Forge** for trend-aware, self-improving build pipelines
- **Relay Council** for multi-agent structured debate on strategic decisions
- **Deep Research** for free multi-source market intelligence
- **CrewAI** (Phase 2) for multi-agent service-tier crews
- **LangGraph** (Phase 3) for executable workflow graphs
- **LangChain** (Phase 2) for 700+ tool integrations and RAG chains
- **awesome-scalability** for infrastructure scaling knowledge patterns
- **Dotprompt** (Phase 2) for typed audit and report templates
- **Business Sector Playbooks** for 80% reuse across 10 client verticals

The name reflects the relay race metaphor. Each specialist picks up the
baton, runs their leg with precision, and hands off cleanly to the next.
The method is faster than any individual. Every handoff is deliberate.

The system is a **symbiote**: it lives inside your codebase, learns from
every engagement, compounds improvements across clients, and self-optimizes
quarterly via `/relay optimize`. The more you use it, the better it gets.
No other local agency has this.

(c) RelayLaunch LLC. "The Relay Method" is a trademark of RelayLaunch LLC.
