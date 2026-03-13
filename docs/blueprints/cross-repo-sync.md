# RelayLaunch Cross-Repo Sync Document

> **Purpose:** This file is the portable data package for syncing AI agent configurations, brand standards, triggers, workflows, and development tooling between RelayLaunch repositories. Copy this document (or its sections) into any RelayLaunch repo that cannot directly access the private `relaylaunch-control-center` repo.
>
> **Source of truth:** `relaylaunch-control-center` (private repo)
> **Last synced:** 2026-03-13
> **Generated from PR #3:** feat: add AI agent framework setup – BMAD Method, Agency Agents, Superpowers

---

## Table of Contents

1. [Brand Standards](#brand-standards)
2. [Service Tiers](#service-tiers)
3. [The Relay Method™ – Overview](#the-relay-method--overview)
4. [Quick Triggers – Cheat Sheet](#quick-triggers--cheat-sheet)
5. [Full Agent Roster](#full-agent-roster)
6. [BMAD Prompt Files](#bmad-prompt-files)
7. [Superpowers Integration](#superpowers-integration)
8. [RelayLaunch Specialist Roles](#relaylaunch-specialist-roles)
9. [Installed Frameworks](#installed-frameworks)
10. [GitHub Templates & Config](#github-templates--config)
11. [Cross-Repo Setup Instructions](#cross-repo-setup-instructions)

---

## Brand Standards

**ENFORCE ON ALL CHANGES – both repos.**

| Role | Hex | Tailwind | Usage |
|------|-----|----------|-------|
| Primary / Dark Navy | `#0F172A` | `slate-900` | Headers, nav, sidebar, footer, dark sections, body text |
| Accent / Electric Blue | `#007AFF` | custom | CTAs, links, hover states ONLY |
| Background / White | `#FFFFFF` | `white` | Page backgrounds |
| Alt Section / Light Gray | `#F8FAFC` | `slate-50` | Alternating section backgrounds |

- **Font:** `Arial, Helvetica, sans-serif` – NO other fonts, NO Google Fonts
- **Voice:** Direct, confident, accessible, action-oriented, veteran precision
- **FORBIDDEN:** green, orange, red, purple, or ANY color outside this 4-color system
- Never use Tailwind color classes outside `slate`, `white`, and custom `#007AFF` accent

---

## Service Tiers

Canonical names – use these exact names everywhere:

| Tier | Price | Description |
|------|-------|-------------|
| Complete Analysis | $1,500–$3,000 | Entry point, diagnostic engagement |
| Launch | $2,500–$5,000 | One-time project build |
| Run | $500–$1,000/mo | Monthly retainer, 3-month min |
| Scale | $1,000–$2,500/mo | Premium retainer, 6-month min |

**Retired names (do NOT use):** Signal, Blueprint, Relay, Sustain

---

## The Relay Method™ – Overview

**The Relay Method™** is RelayLaunch's branded approach to AI-assisted business operations. It unifies three open-source agent frameworks – BMAD Method, The Agency, and Superpowers – into a single coordinated system with short trigger commands, specialist roles mapped to real business functions, and cross-repo awareness.

### Four Layers

| Layer | Purpose | Source |
|-------|---------|--------|
| **1. BMAD Lifecycle Agents** | Structured agile roles for the full SDLC (plan, build, test, ship) | BMAD Method |
| **2. Agency Domain Specialists** | Deep-expertise personas for subject-matter knowledge | The Agency |
| **3. Superpowers Workflow Engine** | Structured multi-step development workflow (brainstorm → ship) | Superpowers |
| **4. RelayLaunch Business Context** | Service-tier workflows and brand standards | Internal |

The name reflects the relay race metaphor: each specialist picks up the baton, runs their leg with precision, and hands off cleanly to the next.

© RelayLaunch LLC. "The Relay Method" is a trademark of RelayLaunch LLC.

---

## Quick Triggers – Cheat Sheet

One-word triggers activate matching specialists instantly across Claude Code, Copilot Chat, or AI prompts.

### One-Word Triggers

| Trigger | Specialist | What It Does |
|---------|-----------|-------------|
| `/architect` | BMAD *architect | Architecture review, structure validation |
| `/audit` | BMAD *qa | Full brand compliance audit |
| `/brandfix` | BMAD *dev (brand) | Find & fix brand color violations |
| `/prettify` | BMAD *dev + *qa | Aesthetic polish with brand compliance |
| `/seo` | BMAD *pm (SEO) | SEO/performance audit with prioritized fixes |
| `/build` | BMAD *dev | Implement features, fix bugs, write code |
| `/plan` | BMAD *pm | Requirements, prioritization, roadmap |
| `/research` | BMAD *analyst | Research, discovery, competitive analysis |
| `/sprint` | BMAD *sm | Story creation, sprint planning, scrum |
| `/qa` | BMAD *qa | Testing, audit, compliance checks |
| `/frontend` | Agency Frontend Developer | React/Next.js/Astro UI implementation |
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
| `/superpowers` | Superpowers Workflow | Full brainstorm → plan → execute → test → review workflow |
| `/datamodel` | BMAD *architect | Data model and schema review |
| `/api` | BMAD *architect | API endpoint review and validation |

### Contextual Triggers (By Business Sector)

**Dashboard & Application:**
- `/relay dashboard` – Full dashboard operations (build, metrics, components)
- `/relay brand` – Brand standards enforcement across all touchpoints
- `/relay performance` – Core Web Vitals, load speed, optimization

**Client Delivery & Operations:**
- `/relay analysis` – Complete Analysis diagnostic engagement workflow
- `/relay launch` – Launch tier project build workflow
- `/relay run` – Run tier monthly retainer operations
- `/relay scale` – Scale tier premium growth operations

**Sales & Business Development:**
- `/relay pipeline` – Pipeline health, forecasting, deal review
- `/relay outreach` – Outbound prospecting and lead generation
- `/relay proposal` – Proposal writing, RFP responses, pricing
- `/relay discovery` – Discovery calls, qualifying, needs assessment

**Marketing & Growth:**
- `/relay seo` – Technical SEO, content SEO, local SEO
- `/relay social` – Social media strategy and content calendar
- `/relay ads` – Paid media campaigns and ad creative
- `/relay email` – Email marketing, sequences, newsletters

**Infrastructure & Engineering:**
- `/relay arch` – Architecture review and technical decisions
- `/relay deploy` – Deployment, CI/CD
- `/relay security` – Security audit, vulnerability scanning
- `/relay data` – Database design, queries, data modeling

---

## Full Agent Roster

### Architecture & Code Quality

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

### Frontend & Development

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
| `/superpowers` | Superpowers Workflow | Superpowers | Activate full brainstorm → ship workflow |

### Design & Brand

| Trigger | Agent | Framework | How to Activate |
|---------|-------|-----------|-----------------|
| `/audit` | BMAD *qa | BMAD | `.github/prompts/bmad-audit.prompt.md` |
| `/ui` | Agency UI Designer | Agency | Activate "UI Designer" persona |
| `/ux` | Agency UX Researcher | Agency | Activate "UX Researcher" persona |
| `/brand` | Agency Brand Guardian | Agency | Activate "Brand Guardian" persona |
| `/story` | Agency Visual Storyteller | Agency | Activate "Visual Storyteller" persona |
| `/whimsy` | Agency Whimsy Injector | Agency | Activate "Whimsy Injector" persona |
| `/imageprompt` | Agency Image Prompt Engineer | Agency | Activate "Image Prompt Engineer" persona |

### SEO, Performance & Content

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

### Planning & Project Management

| Trigger | Agent | Framework | How to Activate |
|---------|-------|-----------|-----------------|
| `/plan` | BMAD *pm | BMAD | Ask to act as BMAD *pm agent |
| `/research` | BMAD *analyst | BMAD | Ask to act as BMAD *analyst agent |
| `/sprint` | BMAD *sm | BMAD | Ask to act as BMAD *sm agent |
| `/qa` | BMAD *qa | BMAD | Ask to act as BMAD *qa agent |

### Paid Media & Advertising

| Trigger | Agent | Framework | How to Activate |
|---------|-------|-----------|-----------------|
| `/ads` | Agency PPC Campaign Strategist | Agency | Activate "PPC Campaign Strategist" persona |
| `/searchterms` | Agency Search Query Analyst | Agency | Activate "Search Query Analyst" persona |
| `/adaudit` | Agency Paid Media Auditor | Agency | Activate "Paid Media Auditor" persona |
| `/tracking` | Agency Tracking Specialist | Agency | Activate "Tracking & Measurement Specialist" persona |
| `/adcopy` | Agency Ad Creative Strategist | Agency | Activate "Ad Creative Strategist" persona |
| `/display` | Agency Programmatic Buyer | Agency | Activate "Programmatic & Display Buyer" persona |
| `/paidsocial` | Agency Paid Social Strategist | Agency | Activate "Paid Social Strategist" persona |

### Sales & Business Development

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

---

## BMAD Prompt Files

These prompt files live in `.github/prompts/` and should be replicated in each repo (adapted for the repo's tech stack).

### BMAD Agent Roles

| Role | Trigger | Specialty |
|------|---------|-----------|
| *analyst | `/research` | Research & discovery |
| *pm | `/plan` | Requirements & prioritization |
| *architect | `/architect` | Technical design & structure |
| *sm | `/sprint` | Story creation & sprint planning |
| *dev | `/build` | Implementation & code |
| *qa | `/qa` | Testing, audit & brand compliance |

### Prompt File Index

| File | Role | Trigger | Purpose |
|------|------|---------|---------|
| `bmad-architect.prompt.md` | *architect | `/architect` | Architecture review, structure validation |
| `bmad-data-model.prompt.md` | *architect | `/datamodel` | Data model and schema review |
| `bmad-api-review.prompt.md` | *architect | `/api` | API endpoint review and validation |
| `bmad-audit.prompt.md` | *qa | `/audit` | Full brand compliance audit |
| `bmad-brand-fix.prompt.md` | *dev | `/brandfix` | Find and fix brand color violations |
| `bmad-prettify.prompt.md` | *dev + *qa | `/prettify` | Aesthetic improvements with brand compliance |
| `bmad-seo.prompt.md` | *pm | `/seo` | Performance & metadata audit |

### Prompt File Contents

> **Note:** When adapting these for the website repo, replace Next.js/Supabase references with Astro/Cloudflare equivalents.

---

#### bmad-architect.prompt.md

```markdown
---
mode: agent
description: "BMAD *architect agent – Technical structure review and architecture validation"
---

# Architecture Review – *architect Agent

You are the BMAD *architect agent performing a technical structure review.
Your job is technical design and structure validation.

## Review Areas

1. **Project Structure** – Files in correct directories, proper component hierarchy
2. **Component Architecture** – Reusable, single-responsibility, Server vs Client
3. **Data Architecture** – Schema matches canonical docs, RLS policies, type safety
4. **API Architecture** – REST conventions, error handling, auth middleware
5. **Performance Architecture** – Server Components, lazy loading, optimized queries
6. **Build & Deployment** – Config, env vars, no secrets in client code

## Output Format

- Architecture score (1-10) per area
- Issues with file paths and specific recommendations
- Quick wins vs. larger refactoring needs
```

---

#### bmad-audit.prompt.md

```markdown
---
mode: agent
description: "BMAD *qa agent – Full brand compliance audit across all pages and styles"
---

# Brand Compliance Audit – *qa Agent

You are the BMAD *qa agent performing a full brand compliance audit.

## Audit Checklist

1. **Color violations** – Any hex not in {#0F172A, #007AFF, #FFFFFF, #F8FAFC}, off-brand Tailwind classes
2. **Typography violations** – Any font-family not Arial/Helvetica/sans-serif
3. **Service tier naming** – Must use: Complete Analysis, Launch, Run, Scale
4. **Metadata compliance** – Every page needs proper metadata
5. **Accessibility** – Heading hierarchy, alt text, color contrast
6. **Link integrity** – Proper Link components, external link attributes

## Output: PASS/FAIL per item, file:line for violations, suggested fixes
```

---

#### bmad-brand-fix.prompt.md

```markdown
---
mode: agent
description: "BMAD *dev agent – Find and fix all brand color violations"
---

# Fix Brand Color Violations – *dev Agent

Approved palette: #0F172A, #007AFF, #FFFFFF, #F8FAFC. Nothing else.

## Steps
1. Scan .tsx, .ts, .css, .json for off-brand colors
2. Replace with brand equivalents
3. Validate CSS custom properties
4. Run build to confirm
```

---

#### bmad-prettify.prompt.md

```markdown
---
mode: agent
description: "BMAD *dev + *qa agents – Aesthetic improvements with brand compliance"
---

# Aesthetic Improvements – *dev + *qa Agents

Improve visual polish while strictly maintaining brand standards.

## Areas: Spacing/rhythm, typography polish, component refinement, transitions
## Constraints: Brand colors only, Arial font only, mobile-first, minimal client JS
```

---

#### bmad-seo.prompt.md

```markdown
---
mode: agent
description: "BMAD *pm agent – Performance and metadata audit with actionable fixes"
---

# Performance & Metadata Audit – *pm Agent

## Audit Areas
1. Page-level metadata (titles, descriptions)
2. Technical performance (Server Components, data fetching)
3. Data loading (efficient queries, no N+1)
4. Accessibility (heading hierarchy, alt text, keyboard nav)
5. Security (RLS, no leaked secrets, auth checks)

## Output: Prioritized table (P0/P1/P2) with issues, files, and fixes
```

---

#### bmad-data-model.prompt.md

```markdown
---
mode: agent
description: "BMAD *architect agent – Data model and schema review"
---

# Data Model Review – *architect Agent

## Review Areas
1. Schema alignment with canonical data model docs
2. Relationships & constraints (FKs, cascades, unique, indexes)
3. Row Level Security (tenant isolation)
4. TypeScript type alignment
5. Migration safety
```

---

#### bmad-api-review.prompt.md

```markdown
---
mode: agent
description: "BMAD *architect agent – API endpoint review and design validation"
---

# API Endpoint Review – *architect Agent

## Review Areas
1. Endpoint coverage (all planned endpoints exist)
2. Response shapes match documented interfaces
3. Authentication & authorization
4. Input validation & sanitization
5. Error handling (structured errors, no internal leaks)
```

---

## Superpowers Integration

When complex multi-step tasks arise, use `/superpowers` to activate the structured workflow:

### Phases

1. **Brainstorm** – Refine ideas through clarifying questions before coding
2. **Plan** – Break work into small, testable tasks (2-5 min each)
3. **Execute** – Implement tasks with review checkpoints using subagents
4. **Test** – RED-GREEN-REFACTOR test-driven methodology
5. **Review** – Validate work against the implementation plan
6. **Finish** – Handle branch merging and cleanup

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

Pre-configured agent combinations for common business workflows:

| Trigger | Agents Used | When |
|---------|------------|------|
| `/relay analysis` | BMAD *analyst + *pm + Agency UX Researcher | Running an 8-area business diagnostic |
| `/relay launch` | BMAD *architect + *dev + Agency Frontend Dev + DevOps + Superpowers | Building client infrastructure from scratch |
| `/relay run` | BMAD *pm + *qa + Agency Content Creator + SEO | Managing monthly retainer |
| `/relay scale` | BMAD *pm + Agency Growth Hacker + PPC + Content | Running premium growth retainer |
| `/relay brand` | BMAD *qa + *dev (brand) + Agency Brand Guardian | Enforcing brand standards everywhere |
| `/relay performance` | BMAD *pm (SEO) + *architect + Agency Growth Hacker + Superpowers | Optimizing performance and Core Web Vitals |

---

## Installed Frameworks

### BMAD Method

- **What:** AI-driven agile development framework with specialized agents
- **Source:** https://github.com/bmad-code-org/BMAD-METHOD
- **Docs:** https://docs.bmad-method.org
- **Install:** `npx bmad-method install`
- **Used in:** Both repos

### The Agency

- **What:** Collection of specialized AI agent personas (engineering, design, marketing, sales)
- **Source:** https://github.com/msitarzewski/agency-agents
- **Install:** Clone repo, copy agents to `~/.claude/agents/` or run `./scripts/install.sh`
- **Used in:** Both repos

### Superpowers

- **What:** Comprehensive software development workflow system for coding agents
- **Source:** https://github.com/obra/superpowers
- **Install:** Plugin marketplace or manual setup
- **Philosophy:** Test-driven development, systematic processes, complexity reduction
- **Used in:** Both repos

---

## GitHub Templates & Config

### Pull Request Template

```markdown
## Summary
<!-- What does this PR do? 1-3 bullet points. -->

## Changes
<!-- List the key files/areas changed. -->

## Checklist
- [ ] Build passes with zero errors
- [ ] Lint passes with zero errors
- [ ] Brand colors only: Navy #0F172A, Blue #007AFF, White #FFFFFF, Gray #F8FAFC
- [ ] No hardcoded secrets or API keys
- [ ] TypeScript strict mode – no `any` types without justification
- [ ] Responsive: tested at 640px, 768px, 1024px breakpoints
- [ ] Accessibility: proper heading hierarchy, alt text, focus states
- [ ] Conventional commit messages (feat:, fix:, chore:)

## Test Plan
<!-- How did you verify this works? -->
```

### Bug Report Template (`.github/ISSUE_TEMPLATE/bug_report.yml`)

```yaml
name: Bug Report
description: Report a bug
labels: ["bug"]
body:
  - type: textarea
    id: description
    attributes:
      label: What happened?
    validations:
      required: true
  - type: textarea
    id: expected
    attributes:
      label: Expected behavior
    validations:
      required: true
  - type: input
    id: page
    attributes:
      label: Page/Route
      placeholder: /dashboard, /changes, etc.
  - type: dropdown
    id: device
    attributes:
      label: Device
      options: [Desktop, Mobile, Tablet]
  - type: dropdown
    id: browser
    attributes:
      label: Browser
      options: [Chrome, Safari, Firefox, Edge, Other]
  - type: textarea
    id: screenshots
    attributes:
      label: Screenshots
```

### Feature Request Template (`.github/ISSUE_TEMPLATE/feature_request.yml`)

```yaml
name: Feature Request
description: Suggest a new feature
labels: ["enhancement"]
body:
  - type: textarea
    id: description
    attributes:
      label: Feature Description
    validations:
      required: true
  - type: textarea
    id: use_case
    attributes:
      label: Use Case
    validations:
      required: true
  - type: dropdown
    id: area
    attributes:
      label: Area
      options: [Dashboard, Automations/Workflows, AI Agents, Approvals, Change Requests, Metrics, Authentication, API, Other]
  - type: dropdown
    id: priority
    attributes:
      label: Priority
      options: [Nice to have, Important, Critical]
  - type: textarea
    id: additional
    attributes:
      label: Additional Context
```

### Dependabot Config (`.github/dependabot.yml`)

```yaml
version: 2
updates:
  - package-ecosystem: npm
    directory: /
    schedule:
      interval: weekly
      day: monday
    open-pull-requests-limit: 5
    labels: [dependencies]
    groups:
      # Adapt group patterns to your repo's package ecosystem
      tailwind:
        patterns: ["tailwindcss", "@tailwindcss/*"]

  - package-ecosystem: github-actions
    directory: /
    schedule:
      interval: weekly
      day: monday
    open-pull-requests-limit: 3
    labels: [ci]
```

---

## Cross-Repo Setup Instructions

When setting up the website repo (or any new RelayLaunch repo) to match this configuration:

### 1. Copy Core Files

| Source (this doc) | Destination in target repo |
|-------------------|---------------------------|
| Brand Standards section | → `CLAUDE.md` (brand section) |
| Triggers + Agent Roster | → `docs/agents.md` |
| BMAD Prompt Files | → `.github/prompts/*.prompt.md` |
| PR Template | → `.github/PULL_REQUEST_TEMPLATE.md` |
| Issue Templates | → `.github/ISSUE_TEMPLATE/` |
| Dependabot Config | → `.github/dependabot.yml` |
| Copilot Instructions | → `.github/copilot-instructions.md` |

### 2. Adapt for Tech Stack

Replace tech-stack-specific references:
- **Control Center:** Next.js 14, Supabase, Vercel
- **Website:** Astro 5, Cloudflare, (adapt accordingly)

### 3. Install Frameworks

```bash
# BMAD Method
npx bmad-method install

# Agency Agents
git clone https://github.com/msitarzewski/agency-agents
cd agency-agents && ./scripts/install.sh

# Superpowers
# Install via plugin marketplace or manual setup
```

### 4. Verify Consistency

After setup, run `/audit` in both repos to confirm:
- Same brand colors enforced
- Same trigger commands available
- Same agent roster accessible
- PR templates match

---

## Multi-Repo Ecosystem

| Repo | Type | Stack | Deployment |
|------|------|-------|------------|
| `relaylaunch-control-center` | Private – Client dashboard & ops tools | Next.js 14 + Supabase | Vercel |
| `relaylaunch-website` | Public – Marketing site | Astro 5 | Cloudflare |

Both repos share:
- Brand standards (colors, fonts, voice)
- Service tier definitions
- The Relay Method™ agent framework
- BMAD prompt files (adapted per stack)
- GitHub templates and CI config

When features span both repos (API integrations, shared data models, webhook contracts), use `docs/blueprints/` in each repo for cross-repo specs.

---

*This document was generated from `relaylaunch-control-center` commit `4c20d48` (PR #3). Re-export when agent configurations change.*
