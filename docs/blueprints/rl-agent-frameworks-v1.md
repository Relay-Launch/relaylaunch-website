# RelayLaunch Agent Frameworks (v1)

Status: Active
Source of truth: relaylaunch-website → `docs/blueprints/`
Last updated: 2026-03-14

---

## 0. Purpose

RelayLaunch uses multiple AI frameworks, agent libraries, and orchestration
tools as part of The Relay Method. This document is the master map of:

- What each framework/tool does in the Relay stack
- Current installation status and version
- How to install and configure each
- When to use each framework
- How they connect to existing blueprints and triggers

Use this file before creating new agents, workflows, or client offerings.

---

## 1. Current Stack (Installed & Active)

### 1.1 BMAD Method (Custom Implementation)

- **Source:** [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) (4,957 stars)
- **Status:** 16 custom prompt files in `.github/prompts/bmad-*.prompt.md`
- **Version:** Custom RelayLaunch implementation (based on BMAD concepts)
- **Latest upstream:** v6 (March 2026) with CLI installer, skills architecture, dev loop automation
- **Roles:** Analyst, PM, Architect, SM, Dev, QA
- **Triggers:** `/architect`, `/audit`, `/build`, `/plan`, `/research`, `/sprint`, `/qa`, `/seo`

### 1.2 The Agency (Persona Layer)

- **Source:** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)
- **Status:** Referenced in `docs/agents.md`, personas map to BMAD prompts
- **Roles:** Brand Guardian, Content Creator, Growth Hacker, Frontend Dev, DevOps, Sales, UX Researcher
- **Triggers:** `/brand`, `/content`, `/growth`, `/frontend`, `/devops`, `/social`, `/ads`

### 1.3 Superpowers (Coding Workflow)

- **Source:** [obra/superpowers](https://github.com/obra/superpowers) (79,700 stars)
- **Status:** Referenced in `docs/agents.md`, methodology documented
- **Workflow:** Brainstorm → Plan → Execute → Test → Review
- **Trigger:** `/superpowers`

### 1.4 Relay Method (Orchestration Layer)

- **Status:** Fully implemented
- **Components:**
  - Mode + Domain trigger system (`?`/`!`/`~` + `code`/`brand`/`growth`/`ops`/`biz`/`plan`/`qa`)
  - Ship Gate (7-agent gate: Build → Security → Brand → QA → Prose → Infra → GitHub)
  - Prose Agent (AI-ism detection)
  - Service-tier triggers (`/relay analysis`, `/relay launch`, `/relay run`, `/relay scale`)
  - 7 default agents (always-on)
- **Specs:** `rl-trigger-system-v1.md`, `rl-website-build-framework-v1.md`

---

## 2. Frameworks to Add (Phased Rollout)

### 2.1 Contains Studio Agents

- **Source:** [contains-studio/agents](https://github.com/contains-studio/agents) (12,242 stars)
- **What:** 30+ agent specs organized by department (design, engineering, marketing, product, PM, testing)
- **Install:**
  ```bash
  # Pin submodule to a specific commit SHA for supply chain safety
  git submodule add https://github.com/contains-studio/agents.git external/studio-agents
  cd external/studio-agents && git checkout <COMMIT_SHA> && cd ../..
  git add external/studio-agents && git commit -m "chore: pin studio-agents submodule"
  ```
- **Integration:** Port selected agents into `.github/prompts/relay-*.prompt.md` with RelayLaunch brand constraints
- **Key agents:** brand-guardian, devops-automator, frontend-developer, content-creator, growth-hacker, project-shipper, test-writer-fixer, ux-researcher
- **Phase:** 1 (immediate)

### 2.2 BMAD v6 Official

- **Source:** [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD)
- **What:** Official installer with skills architecture, dev loop automation, test architecture module
- **Install:**
  ```bash
  # Pin to a stable version -- run in a temp dir first to inspect output
  npx bmad-method install
  # WARNING: Do NOT run in website root without first testing in a
  # throwaway directory. The installer scaffolds files that may
  # conflict with existing .github/prompts/ and CLAUDE.md.
  ```
- **Integration:** Runs alongside custom prompt files. Adds skills and modules that complement existing setup
- **Caution:** Test installer output in a temp directory first. Your 16 custom prompt files take precedence -- only adopt new BMAD skills/modules that add value beyond what you already have.
- **New capabilities:** Root cause analysis, dev loop automation, creative intelligence suite, test architecture enterprise
- **Phase:** 1 (immediate)

### 2.3 Superpowers Plugin

- **Source:** [obra/superpowers](https://github.com/obra/superpowers) + [marketplace](https://github.com/obra/superpowers-marketplace)
- **What:** Official Claude Code plugin with automatic skill activation
- **Install (in Claude Code):**
  ```
  /plugin marketplace add obra/superpowers-marketplace
  /plugin install superpowers@superpowers-marketplace
  ```
- **Integration:** Handles coding workflow automatically; Relay agents handle domain expertise
- **New capabilities:** TDD skill activation, systematic debugging, verification before completion, Chrome browser control
- **Phase:** 1 (immediate)

### 2.4 CrewAI (Multi-Agent Crews)

- **Source:** [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)
- **What:** Python framework for orchestrating role-playing AI agent teams
- **Install:**
  ```bash
  # Pin to exact version in a separate repo or workspace
  pip install crewai==0.175.0
  pip install 'crewai[tools]'
  ```
- **Requires:** Python >=3.10, <3.14
- **Important:** Do NOT install Python deps in this Astro/Node.js repo. Use a separate `relaylaunch-agents` repo or a `tools/` workspace with its own `requirements.txt` and version pins. Cloudflare Workers cannot run Python.
- **Integration:** Create crew definitions matching service tiers
- **Crews to build:**
  - `relay_complete_analysis.py` — Analyst + PM + UX Researcher (Complete Analysis)
  - `relay_launch.py` — Architect + Dev + DevOps + Brand (Launch build)
  - `relay_run.py` — PM + Content + SEO + Growth (Run retainer)
  - `relay_scale.py` — PM + Growth + PPC + Analytics (Scale retainer)
- **Phase:** 2

### 2.5 Dotprompt (Typed Prompt Templates)

- **Source:** [google/dotprompt](https://github.com/google/dotprompt)
- **What:** Executable prompt templates with schema validation and Handlebars syntax
- **Install:**
  ```bash
  # Standalone Dotprompt (lightweight, no Genkit dependency)
  npm install @google/dotprompt
  # Or with full Genkit (heavier, includes Google AI SDK):
  # npm install genkit @genkit-ai/googleai
  ```
- **Note:** Prefer standalone `@google/dotprompt` to avoid pulling in the full Genkit framework. Only use Genkit if you need its runtime features beyond prompt templating.
- **Integration:** Convert BMAD prompts to `.prompt` files in `dotprompts/` with typed inputs/outputs
- **Templates to create:**
  - `qa-audit.prompt` — Input: files_changed[], brand_rules; Output: violations[]
  - `seo-audit.prompt` — Input: url, content, keywords; Output: issues[], actions[]
  - `complete-analysis.prompt` — Input: client properties; Output: structured report sections
  - `cc-api-review.prompt` — Input: endpoints; Output: issues[], recommendations[]
- **Phase:** 2

### 2.6 LangGraph JS (Executable Workflows)

- **Source:** [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) (v1.2.2)
- **What:** Graph-based agent orchestration for deterministic, stateful workflows
- **Install:**
  ```bash
  # Install in a separate workspace (infra/package.json), NOT in the
  # main Astro package.json -- avoids Vite/ESM conflicts
  npm install @langchain/langgraph@1.2.2 @langchain/core
  ```
- **Important:** Keep LangGraph deps separate from the Astro website build. Use `infra/package.json` or a separate repo to avoid dependency conflicts with Vite.
- **Integration:** Create `infra/langgraph/` with:
  - `ship-gate.ts` — 7-node StateGraph matching Ship Gate order
  - `website-build-flow.ts` — Build phases from rl-website-build-framework-v1
- **Phase:** 3

### 2.7 NotebookLM Integration

- **Source:** [PleasePrompto/notebooklm-mcp](https://github.com/PleasePrompto/notebooklm-mcp) and [ray-manaloto/notebooklm-claude-integration](https://github.com/ray-manaloto/notebooklm-claude-integration)
- **What:** MCP server and CLI for querying NotebookLM notebooks from Claude Code
- **Integration:** Per-client notebooks as knowledge vaults for analysis agents
- **Phase:** 3

### 2.8 Gemini Pro (Google Data Agent)

- **What:** Google model with tool-calling and Workspace integration
- **Integration:** SEO/analytics data agent inside CrewAI or LangGraph nodes
- **Use cases:** Search Console metrics, PageSpeed data, traffic snapshots for retainer reports
- **Phase:** 3

---

## 3. Agent Mapping: Framework → Trigger → Prompt

| Trigger | BMAD Role | Agency Persona | Contains Studio | CrewAI Crew |
|---------|-----------|---------------|----------------|-------------|
| `/architect` | *architect | Software Architect | — | Launch |
| `/build` | *dev | Frontend Developer | frontend-developer | Launch |
| `/qa` | *qa | — | test-writer-fixer | All (gate) |
| `/brand` | *qa (audit) | Brand Guardian | brand-guardian | All (gate) |
| `/content` | *pm | Content Creator | content-creator | Run/Scale |
| `/growth` | *pm (SEO) | Growth Hacker | growth-hacker | Scale |
| `/devops` | — | DevOps | devops-automator | Launch |
| `/research` | *analyst | — | ux-researcher | Analysis |
| `/ship` | All defaults | — | project-shipper | — (LangGraph) |
| `/relay analysis` | *analyst + *pm | UX Researcher | ux-researcher | Analysis Crew |
| `/relay launch` | *architect + *dev | Frontend + DevOps | multiple | Launch Crew |
| `/relay run` | *pm + *qa | Content + Growth | multiple | Run Crew |
| `/relay scale` | *pm + Growth | Growth + Analytics | multiple | Scale Crew |

---

## 4. Tool Stack: When to Use Which

| Task | Primary Tool | Supporting Tools |
|------|-------------|-----------------|
| Build / Code / Repo work | Claude Code + Relay Method | Superpowers, Copilot |
| External research | Perplexity Pro | — |
| Client knowledge & docs | NotebookLM | Gemini Pro |
| SEO & performance metrics | Gemini Pro | Perplexity |
| Inline edits & refactors | Copilot | Claude Code |
| Multi-agent workflows | CrewAI (Python) | LangGraph (CI) |
| Structured prompt execution | Dotprompt | — |
| Agent personas | BMAD + Agency + Contains Studio | — |

---

## 5. Implementation Phases

### Phase 1: Foundation (Current Sprint)

- [ ] Install Superpowers plugin in Claude Code
- [ ] Clone Contains Studio agents to `external/studio-agents`
- [ ] Clone Agency agents to `external/agency-agents`
- [ ] Run BMAD v6 installer (`npx bmad-method@next install`)
- [ ] Port top 6 Contains Studio agents to `.github/prompts/relay-*.prompt.md`
- [ ] Update `docs/agents.md` with new agent mappings

### Phase 2: Crews & Templates (Next Sprint)

- [ ] Set up Python environment with CrewAI
- [ ] Create `crews/relay_complete_analysis.py`
- [ ] Create `crews/relay_launch.py`
- [ ] Create `crews/relay_run.py`
- [ ] Create core Dotprompt templates in `dotprompts/`
- [ ] Wire CrewAI to n8n for intake form automation

### Phase 3: Graphs & Integrations (Following Sprint)

- [ ] Install LangGraph JS
- [ ] Create `infra/langgraph/ship-gate.ts`
- [ ] Wire Ship Gate to GitHub Actions on PR
- [ ] Configure NotebookLM MCP for Claude Code
- [ ] Set up Gemini data agent for SEO metrics
- [ ] Connect metrics to Control Center dashboards

### Phase 4: Productization

- [ ] Update website service pages to reference agent stack
- [ ] Create client-facing "Agent Playbook" template
- [ ] Add case studies showing agent-driven delivery
- [ ] Define agent-backed SLA for proposals

---

## 6. Directory Structure (Target)

```
relaylaunch-website/                    # Astro website (Node.js only)
├── .github/prompts/                    # BMAD + relay prompt files (existing)
│   ├── bmad-*.prompt.md                # Core BMAD agents (16 files)
│   └── relay-*.prompt.md              # Ported Contains Studio agents (new)
├── external/                           # External agent repos (new, reference only)
│   ├── studio-agents/                  # Contains Studio (submodule, pinned SHA)
│   └── agency-agents/                  # Agency (submodule, pinned SHA)
├── docs/
│   ├── agents.md                       # Relay Method agent registry (existing)
│   └── blueprints/
│       └── rl-agent-frameworks-v1.md   # This file
└── src/                                # Astro website source (existing)

relaylaunch-agents/ (SEPARATE REPO)     # Python + heavy Node deps
├── crews/                              # CrewAI crew definitions
│   ├── requirements.txt               # Pinned Python deps
│   ├── relay_complete_analysis.py
│   ├── relay_launch.py
│   └── relay_run.py
├── dotprompts/                         # Dotprompt typed templates
│   ├── qa-audit.prompt
│   ├── seo-audit.prompt
│   └── complete-analysis.prompt
├── infra/                              # LangGraph workflows
│   ├── package.json                   # Separate Node deps (LangGraph)
│   ├── langgraph/
│   │   └── ship-gate.ts
│   └── reports/
└── .env.example                        # Required API keys
```

**Why separate repos:** The Astro website deploys to Cloudflare Workers (V8 isolates).
Python (CrewAI) and heavy Node packages (LangGraph, Genkit) cannot run there and
would bloat the website's dependency tree. Keep the website lean; run agent
automation from a dedicated repo or workspace.

---

## 7. Secrets & API Key Management

Each phase introduces new API key requirements. Store all secrets in
GitHub Actions Secrets and local `.env.local` (gitignored).

| Phase | Framework | Keys Required | Storage |
|-------|-----------|--------------|---------|
| 1 | BMAD v6 | None (spec-only) | N/A |
| 1 | Superpowers | None (plugin) | N/A |
| 2 | CrewAI | `ANTHROPIC_API_KEY` or `OPENAI_API_KEY` | `.env.local`, GitHub Secrets |
| 2 | Dotprompt + Genkit | `GOOGLE_API_KEY` (if using Genkit) | `.env.local`, GitHub Secrets |
| 3 | LangGraph | LLM API key (depends on model) | `.env.local`, GitHub Secrets |
| 3 | NotebookLM MCP | Google auth token | Claude Code MCP config |
| 3 | Gemini Pro | `GOOGLE_API_KEY` | `.env.local`, GitHub Secrets |

**Rules:**
- Never commit API keys to the repo
- Rotate keys quarterly
- Use scoped/restricted keys where possible
- Document required keys in each workspace's `.env.example`

---

## 8. Links & Resources

### Core Frameworks
- [BMAD Method v6](https://github.com/bmad-code-org/BMAD-METHOD) — Agile AI development framework
- [Agency Agents](https://github.com/msitarzewski/agency-agents) — Domain specialist personas
- [Superpowers](https://github.com/obra/superpowers) — Coding workflow plugin
- [Contains Studio Agents](https://github.com/contains-studio/agents) — Department-organized agent specs

### Orchestration
- [LangGraph](https://github.com/langchain-ai/langgraph) — Graph-based agent workflows
- [CrewAI](https://github.com/crewAIInc/crewAI) — Multi-agent crew orchestration
- [Dotprompt](https://github.com/google/dotprompt) — Typed prompt templates

### Knowledge & Data
- [NotebookLM MCP](https://github.com/PleasePrompto/notebooklm-mcp) — Claude Code integration
- [NotebookLM CLI Integration](https://github.com/ray-manaloto/notebooklm-claude-integration)
- [Gemini API Tools](https://ai.google.dev/gemini-api/docs/tools)

### BMAD Expansions
- [BMAD Test Architecture Enterprise](https://github.com/bmad-code-org/bmad-method-test-architecture-enterprise)
- [BMAD Creative Intelligence Suite](https://github.com/bmad-code-org)
- [BMAD v5 (Legacy)](https://github.com/bmadcode/BMAD-METHOD-v5)

### Superpowers Ecosystem
- [Superpowers Lab](https://github.com/obra/superpowers-lab) — Experimental skills
- [Superpowers Chrome](https://github.com/obra/superpowers-chrome) — Browser control
- [Superpowers Skills](https://github.com/obra/superpowers-skills) — Community skills
