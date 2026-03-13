# AI Agents & Tools Registry

This document lists every AI agent framework, agent persona, and tool
available across the RelayLaunch ecosystem. AI coding tools (Claude Code,
GitHub Copilot, Cursor) should consult this file to match tasks to the
right agent or workflow.

## How to Use

Reference an agent by name or trigger keyword in your prompt:

```
"Run bmad-audit on this page"
"Act as the frontend developer agent and build this component"
"I need help with SEO — which agent should I use?"
```

AI tools: when the user mentions a trigger keyword below, suggest the
matching agent and explain how to activate it.

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
- **Install:** Copy agents to `~/.claude/agents/` or use `./scripts/install.sh`
- **Used in:** Both repos (relaylaunch-website, relaylaunch-control-center)

---

## Agent Quick-Reference by Category

Use this table to find the right agent for any task. When the user mentions
a trigger keyword, suggest the matching agent.

### 🏗️ Architecture & Code Quality

| Trigger Keywords | Agent | Framework | How to Activate |
|------------------|-------|-----------|-----------------|
| architecture, structure, review, tech debt | BMAD *architect | BMAD | `.github/prompts/bmad-architect.prompt.md` |
| code review, PR review, maintainability | Agency Code Reviewer | Agency | Activate "Code Reviewer" persona |
| security, vulnerabilities, threat model | Agency Security Engineer | Agency | Activate "Security Engineer" persona |
| database, queries, schema, indexing | Agency Database Optimizer | Agency | Activate "Database Optimizer" persona |
| git, branching, commits, workflow | Agency Git Workflow Master | Agency | Activate "Git Workflow Master" persona |
| system design, DDD, patterns | Agency Software Architect | Agency | Activate "Software Architect" persona |
| reliability, SLOs, observability | Agency SRE | Agency | Activate "SRE" persona |

### 💻 Frontend & Development

| Trigger Keywords | Agent | Framework | How to Activate |
|------------------|-------|-----------|-----------------|
| implement, build, code, fix, component | BMAD *dev | BMAD | Ask to act as BMAD *dev agent |
| brand fix, color violations, CSS | BMAD *dev (brand) | BMAD | `.github/prompts/bmad-brand-fix.prompt.md` |
| prettify, polish, aesthetics, spacing | BMAD *dev + *qa | BMAD | `.github/prompts/bmad-prettify.prompt.md` |
| React, Vue, Angular, UI, frontend, CSS | Agency Frontend Developer | Agency | Activate "Frontend Developer" persona |
| API, backend, server, database, microservice | Agency Backend Architect | Agency | Activate "Backend Architect" persona |
| mobile, iOS, Android, React Native | Agency Mobile App Builder | Agency | Activate "Mobile App Builder" persona |
| prototype, MVP, hackathon, POC | Agency Rapid Prototyper | Agency | Activate "Rapid Prototyper" persona |
| CI/CD, pipeline, deploy, infrastructure | Agency DevOps Automator | Agency | Activate "DevOps Automator" persona |
| docs, documentation, API reference | Agency Technical Writer | Agency | Activate "Technical Writer" persona |

### 🎨 Design & Brand

| Trigger Keywords | Agent | Framework | How to Activate |
|------------------|-------|-----------|-----------------|
| brand audit, compliance, colors, fonts | BMAD *qa | BMAD | `.github/prompts/bmad-audit.prompt.md` |
| UI design, component library, design system | Agency UI Designer | Agency | Activate "UI Designer" persona |
| UX, user testing, usability, research | Agency UX Researcher | Agency | Activate "UX Researcher" persona |
| brand identity, consistency, positioning | Agency Brand Guardian | Agency | Activate "Brand Guardian" persona |
| visual story, multimedia, narrative | Agency Visual Storyteller | Agency | Activate "Visual Storyteller" persona |
| delight, micro-interactions, Easter eggs | Agency Whimsy Injector | Agency | Activate "Whimsy Injector" persona |
| AI images, prompts, Midjourney, DALL-E | Agency Image Prompt Engineer | Agency | Activate "Image Prompt Engineer" persona |

### 📈 SEO & Content

| Trigger Keywords | Agent | Framework | How to Activate |
|------------------|-------|-----------|-----------------|
| SEO, meta tags, schema, sitemap, rankings | BMAD *pm (SEO) | BMAD | `.github/prompts/bmad-seo.prompt.md` |
| content, blog, editorial, copywriting | Agency Content Creator | Agency | Activate "Content Creator" persona |
| growth, acquisition, viral, conversion | Agency Growth Hacker | Agency | Activate "Growth Hacker" persona |
| social media, cross-platform strategy | Agency Social Media Strategist | Agency | Activate "Social Media Strategist" persona |
| Twitter, LinkedIn, thought leadership | Agency Twitter Engager | Agency | Activate "Twitter Engager" persona |
| Instagram, visual content, aesthetic | Agency Instagram Curator | Agency | Activate "Instagram Curator" persona |
| TikTok, short-form video, viral | Agency TikTok Strategist | Agency | Activate "TikTok Strategist" persona |
| Reddit, community, authentic engagement | Agency Reddit Community Builder | Agency | Activate "Reddit Community Builder" persona |
| app store, ASO, discoverability | Agency App Store Optimizer | Agency | Activate "App Store Optimizer" persona |

### 📊 Planning & Project Management

| Trigger Keywords | Agent | Framework | How to Activate |
|------------------|-------|-----------|-----------------|
| requirements, prioritize, roadmap, backlog | BMAD *pm | BMAD | Ask to act as BMAD *pm agent |
| research, discovery, analysis | BMAD *analyst | BMAD | Ask to act as BMAD *analyst agent |
| sprint, stories, planning, scrum | BMAD *sm | BMAD | Ask to act as BMAD *sm agent |
| test, QA, audit, compliance | BMAD *qa | BMAD | Ask to act as BMAD *qa agent |

### 💰 Paid Media & Advertising

| Trigger Keywords | Agent | Framework | How to Activate |
|------------------|-------|-----------|-----------------|
| PPC, Google Ads, bidding, ad spend | Agency PPC Campaign Strategist | Agency | Activate "PPC Campaign Strategist" persona |
| search queries, negative keywords | Agency Search Query Analyst | Agency | Activate "Search Query Analyst" persona |
| ad audit, account review, competitive | Agency Paid Media Auditor | Agency | Activate "Paid Media Auditor" persona |
| tracking, GTM, GA4, conversions | Agency Tracking Specialist | Agency | Activate "Tracking & Measurement Specialist" persona |
| ad copy, creative, RSA, Performance Max | Agency Ad Creative Strategist | Agency | Activate "Ad Creative Strategist" persona |
| display, programmatic, DSP, ABM | Agency Programmatic Buyer | Agency | Activate "Programmatic & Display Buyer" persona |
| Meta Ads, LinkedIn Ads, TikTok Ads | Agency Paid Social Strategist | Agency | Activate "Paid Social Strategist" persona |

### 🤝 Sales & Business Development

| Trigger Keywords | Agent | Framework | How to Activate |
|------------------|-------|-----------|-----------------|
| outbound, prospecting, cold outreach | Agency Outbound Strategist | Agency | Activate "Outbound Strategist" persona |
| discovery calls, qualifying, SPIN | Agency Discovery Coach | Agency | Activate "Discovery Coach" persona |
| deal strategy, MEDDPICC, pipeline | Agency Deal Strategist | Agency | Activate "Deal Strategist" persona |
| demo, POC, pre-sales, battlecard | Agency Sales Engineer | Agency | Activate "Sales Engineer" persona |
| proposal, RFP, win themes | Agency Proposal Strategist | Agency | Activate "Proposal Strategist" persona |
| forecast, pipeline health, RevOps | Agency Pipeline Analyst | Agency | Activate "Pipeline Analyst" persona |
| account planning, expand, QBR, NRR | Agency Account Strategist | Agency | Activate "Account Strategist" persona |
| coaching, rep development, call review | Agency Sales Coach | Agency | Activate "Sales Coach" persona |

---

## BMAD Agents in This Repo

These agents are configured as Copilot prompt files in `.github/prompts/`
and as BMAD roles referenced in `CLAUDE.md`.

| Agent | Role | Prompt File | Purpose |
|-------|------|-------------|---------|
| *architect | Technical design | `bmad-architect.prompt.md` | Architecture review, structure validation |
| *qa | Testing & audit | `bmad-audit.prompt.md` | Full brand compliance audit |
| *dev | Implementation | `bmad-brand-fix.prompt.md` | Find and fix brand color violations |
| *dev + *qa | Polish | `bmad-prettify.prompt.md` | Aesthetic improvements with brand compliance |
| *pm | Requirements | `bmad-seo.prompt.md` | SEO audit with prioritized fixes |
| *analyst | Research | _(no prompt file yet)_ | Research and discovery |
| *sm | Scrum master | _(no prompt file yet)_ | Story creation and sprint planning |

### Adding New BMAD Prompts

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

## Cross-Repo Agent Setup

Both `relaylaunch-website` and `relaylaunch-control-center` should maintain
a copy of this file at `docs/agents.md` so AI tools in either repo know the
full agent roster. The website repo is the source of truth for this file.

When setting up a new repo in the RelayLaunch ecosystem:

1. Copy `docs/agents.md` into the new repo
2. Add BMAD prompt files to `.github/prompts/` as needed
3. Reference agents in `CLAUDE.md` and `.github/copilot-instructions.md`
4. Install frameworks: `npx bmad-method install` and copy Agency agents
