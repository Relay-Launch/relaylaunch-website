# AI Agents & Tools Registry — The Relay Method™

> **The Relay Method™** is RelayLaunch's branded approach to AI-assisted
> business operations. It unifies two open-source agent frameworks — BMAD
> Method and The Agency — into a single coordinated system with short
> trigger commands, specialist roles mapped to real business functions, and
> cross-repo awareness. Every AI tool in the ecosystem (Claude Code, GitHub
> Copilot, Cursor) reads this file to route tasks to the right specialist.

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
| `/security` | Agency Security Engineer | Threat modeling, vulnerability review |
| `/ux` | Agency UX Researcher | User testing, usability, research |
| `/brand` | Agency Brand Guardian | Brand identity, consistency, positioning |
| `/content` | Agency Content Creator | Blog posts, copywriting, editorial |
| `/growth` | Agency Growth Hacker | Acquisition, viral loops, conversion |
| `/social` | Agency Social Media Strategist | Cross-platform social strategy |
| `/ads` | Agency PPC Campaign Strategist | Google/Meta/LinkedIn ad campaigns |
| `/outbound` | Agency Outbound Strategist | Prospecting, cold outreach, sequences |
| `/deals` | Agency Deal Strategist | MEDDPICC, pipeline, win strategy |
| `/proposal` | Agency Proposal Strategist | RFPs, proposals, win themes |
| `/coach` | Agency Sales Coach | Rep development, call review, training |

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

**Infrastructure & Engineering:**
- `/relay arch` — Architecture review and technical decisions
- `/relay deploy` — Cloudflare Workers deployment, CI/CD
- `/relay security` — Security audit, vulnerability scanning
- `/relay data` — Database design, queries, data modeling

---

## The Relay Method™ — How It Works

The Relay Method™ organizes AI agent assistance into three layers:

### Layer 1: BMAD Lifecycle Agents
Structured agile roles that manage the full software development lifecycle.
These are the "process" agents — they know *how* to plan, build, test, and ship.

| Role | Trigger | Specialty | Prompt File |
|------|---------|-----------|-------------|
| *analyst | `/research` | Research & discovery | _(ask to act as *analyst)_ |
| *pm | `/plan` | Requirements & prioritization | _(ask to act as *pm)_ |
| *architect | `/architect` | Technical design & structure | `bmad-architect.prompt.md` |
| *sm | `/sprint` | Story creation & sprint planning | _(ask to act as *sm)_ |
| *dev | `/build` | Implementation & code | `bmad-brand-fix.prompt.md`, `bmad-prettify.prompt.md` |
| *qa | `/qa` | Testing, audit & brand compliance | `bmad-audit.prompt.md` |

### Layer 2: Agency Domain Specialists
Deep-expertise personas that bring subject-matter knowledge. These are the
"what" agents — they know the craft inside and out.

### Layer 3: RelayLaunch Business Context
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

---

## Full Agent Roster by Category

### 🏗️ Architecture & Code Quality

| Trigger | Agent | Framework | How to Activate |
|---------|-------|-----------|-----------------|
| `/architect` | BMAD *architect | BMAD | `.github/prompts/bmad-architect.prompt.md` |
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
| `/build` | BMAD *dev | BMAD | Ask to act as BMAD *dev agent |
| `/brandfix` | BMAD *dev (brand) | BMAD | `.github/prompts/bmad-brand-fix.prompt.md` |
| `/prettify` | BMAD *dev + *qa | BMAD | `.github/prompts/bmad-prettify.prompt.md` |
| `/frontend` | Agency Frontend Developer | Agency | Activate "Frontend Developer" persona |
| `/backend` | Agency Backend Architect | Agency | Activate "Backend Architect" persona |
| `/mobile` | Agency Mobile App Builder | Agency | Activate "Mobile App Builder" persona |
| `/prototype` | Agency Rapid Prototyper | Agency | Activate "Rapid Prototyper" persona |
| `/devops` | Agency DevOps Automator | Agency | Activate "DevOps Automator" persona |
| `/docs` | Agency Technical Writer | Agency | Activate "Technical Writer" persona |

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
| `/plan` | BMAD *pm | BMAD | Ask to act as BMAD *pm agent |
| `/research` | BMAD *analyst | BMAD | Ask to act as BMAD *analyst agent |
| `/sprint` | BMAD *sm | BMAD | Ask to act as BMAD *sm agent |
| `/qa` | BMAD *qa | BMAD | Ask to act as BMAD *qa agent |

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
| *qa | Testing & audit | `bmad-audit.prompt.md` | `/audit` | Full brand compliance audit |
| *dev | Implementation | `bmad-brand-fix.prompt.md` | `/brandfix` | Find and fix brand color violations |
| *dev + *qa | Polish | `bmad-prettify.prompt.md` | `/prettify` | Aesthetic improvements with brand compliance |
| *pm | Requirements | `bmad-seo.prompt.md` | `/seo` | SEO audit with prioritized fixes |
| *analyst | Research | _(no prompt file yet)_ | `/research` | Research and discovery |
| *sm | Scrum master | _(no prompt file yet)_ | `/sprint` | Story creation and sprint planning |

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
3. SEO *pm audits and optimizes search performance
4. *qa audits brand compliance on all new content

### 📈 Scale Growth Specialist
**Trigger:** `/relay scale`
**Agents:** BMAD *pm + Agency Growth Hacker + PPC Strategist + Content Creator
**When:** Running a premium growth retainer — expanded deliverables, advanced builds.
**Workflow:**
1. *pm sets quarterly growth OKRs and sprint plans
2. Growth Hacker designs experiments and conversion funnels
3. PPC Strategist manages paid acquisition channels
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

## About The Relay Method™

The Relay Method™ is a proprietary framework developed by RelayLaunch LLC
for orchestrating AI agents across the full spectrum of digital business
operations — from code to content to client delivery.

It combines:
- **BMAD Method** for structured agile development lifecycle
- **The Agency** for deep domain specialist expertise
- **RelayLaunch business context** for service-tier workflows and brand standards

The name reflects the relay race metaphor: each specialist picks up the
baton, runs their leg with precision, and hands off cleanly to the next.
Just like a relay team, the method is faster than any individual and every
handoff is deliberate.

© RelayLaunch LLC. "The Relay Method" is a trademark of RelayLaunch LLC.
