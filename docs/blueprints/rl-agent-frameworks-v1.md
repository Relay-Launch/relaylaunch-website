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
- **Behavioral Design & CRO** (4 agents: Conversion Architect, Behavioral Designer, Buyer Psychologist, Neuromarketer)
  - Spec: `relay-behavioral-design.prompt.md`
  - Triggers: `/cro`, `/behavioral`, `/buyer`, `/neuro`
- **Council & Deep Research** (2 meta-agents: The Council, Deep Research)
  - Spec: `relay-council.prompt.md`
  - Triggers: `/council`, `/deep-research`
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
| `/cro` | — | — | — | — (Relay native) |
| `/behavioral` | — | — | — | — (Relay native) |
| `/buyer` | — | — | — | — (Relay native) |
| `/neuro` | — | — | — | — (Relay native) |
| `/council` | All relevant | All relevant | All relevant | — (orchestration) |
| `/deep-research` | *analyst + *pm | Multiple | Multiple | Analysis Crew |

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

## 8. Founder-Only Finance Agents (Internal Only)

### 8.1 Purpose and Scope

RelayLaunch has three **founder-only finance agents** designed to help Victor
reason about:

- Business structure and high-level finance questions
- Tool and subscription costs
- Which metrics matter at the current stage

These agents:

- Are **internal only** (we do not market them on relaylaunch.com or use them in client repos).
- Operate under the **biz** and **plan** domains from `rl-trigger-system-v1.md`.
- Provide **education, reflection, and organization**, not legal, tax, or investment advice.

### 8.2 Agent: Founder Finance Navigator

**File:** `.github/prompts/finance-founder-navigator.prompt.md`
**Trigger:** `~biz-finance` or `think finance` (Mode: think, Domain: biz)

- Acts as a **concept explainer and planning partner** for entity type questions
  (sole prop vs LLC vs S-corp etc.), cashflow ideas, and tax/logistics considerations.
- Converts vague worries ("Am I set up correctly?") into clear concepts, scenarios,
  and checklists.
- Always includes disclaimer: "Not legal or tax advice."

**Novel RelayLaunch use:** Before changing public pricing or service tiers, run
`~biz-finance` to produce a private "Decision Note" that you can then summarize
into a founder blog post without exposing internal numbers.

### 8.3 Agent: Small Biz Expense & Tools Coach

**File:** `.github/prompts/finance-tools-coach.prompt.md`
**Trigger:** `?biz-tools` or `check tools` (Mode: check, Domain: biz)

- Acts as a **tool stack auditor** for RelayLaunch and similar small businesses.
- Takes a list of SaaS, infra, and subscription tools and classifies each as
  **keep**, **monitor**, **downgrade**, **replace**, or **cancel**.
- Suggests alternatives from the free-for-dev catalog while respecting the
  canonical Relay stack (Astro + Cloudflare, Supabase, n8n, Mailchimp, Buffer).

**Novel RelayLaunch use:** Run quarterly and pull findings into anonymous "How we
trimmed $X/mo from our own stack" blog posts for content marketing.

### 8.4 Agent: Founder KPI Explainer

**File:** `.github/prompts/finance-kpi-explainer.prompt.md`
**Trigger:** `~plan-kpi` or `think kpi` (Mode: think, Domain: plan)

- Serves as a **metric translator** for a small AI services + platform business.
- Explains metrics (MRR, average project size, retainer mix, runway, utilization)
  in plain language tailored to a solo or tiny team studio.
- Suggests 3-5 metrics to track and simple tracking systems (spreadsheet, Notion,
  eventual Control Center dashboards).

**Novel RelayLaunch use:** Before writing or updating service playbooks or price
tables, run `~plan-kpi` on your latest numbers and sync the narrative: "We designed
these tiers to support a healthy, sustainable solo studio."

### 8.5 Integration

- **Domains & Modes** - `?` / `check` for review-only, `~` / `think` for brainstorming.
- **Repos** - Live in `relaylaunch-website` alongside other prompts but operate on
  RelayLaunch as a business, not on website or Control Center code.
- **Client boundary** - If you reuse insights for clients (blog posts, guides),
  rewrite for general audiences. Strip personal numbers and check with Brand +
  Prose agents for voice alignment.

---

## 9. Meta-Role Overlays (Internal Only)

### 9.1 Purpose

Meta-roles add a **strategic review layer** on top of existing Relay Method agents.
Inspired by [gstack](https://github.com/garrytan/gstack) executive role patterns.

### 9.2 Available Overlays

| Overlay | Trigger | What It Does |
|---------|---------|--------------|
| CEO / Vision Review | `~plan-ceo-review` | Challenge assumptions, ask hard questions, find blind spots |
| Eng Manager Review | `~plan-eng-review` | Evaluate architecture for solo-founder maintainability |
| Code Review (Pre-Ship) | `?code-review` or `/review` | Senior review before `/ship`, catch what linters miss |
| Retrospective | `~retro` | Structured post-project reflection with actionable improvements |

**File:** `.github/prompts/relay-meta-roles.prompt.md`

### 9.3 Novel RelayLaunch Uses

- **Founder Review for clients:** Run `~plan-ceo-review` on client project direction
  and include a "Strategic Review" section in Blueprint reports.
- **Monthly retro habit:** Run `~retro` at end of each month to continuously improve
  the Relay Method itself.
- **Pre-ship quality gate:** Run `?code-review` before every `/ship` to catch things
  automated checks miss.

---

## 10. LangGraph - Ship Gate & Build Graphs

### 10.1 Repos

- LangGraph (main): [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) (v1.2.2)
- LangGraph examples: [langgraph/examples](https://github.com/langchain-ai/langgraph/tree/main/examples)
- LangGraph project template: [langchain-ai/langgraph-example](https://github.com/langchain-ai/langgraph-example)

### 10.2 Role in RelayLaunch

LangGraph turns textual blueprints into **executable graphs**:

- The **Ship Gate** from `rl-trigger-system-v1.md` (Build > Security > Brand > QA > Prose > Infra > GitHub)
- The **Website Build Framework** from `rl-website-build-framework-v1.md`
- Future Control Center build flows

Instead of static checklists, LangGraph encodes them as stateful workflows you can
run in CI, from `/ship`, or on demand.

### 10.3 Ship Gate Graph

**File:** `infra/langgraph/ship-gate.ts` (in separate `relaylaunch-agents` repo)

**State:**
- `branch` (string)
- `changed_files` (list of file paths)
- `repo_type` ("website" or "control-center")
- `results` (aggregated gate results)

**Nodes (7, matching Ship Gate order):**

1. `build_check_node` - runs `npm run build` and records pass/fail
2. `security_check_node` - scans for secrets, injection vectors, CVEs
3. `brand_check_node` - enforces 4-color system, font stack, voice
4. `qa_check_node` - runs accessibility and Lighthouse audits
5. `prose_check_node` - runs AI-ism detection from Prose Agent rules
6. `infra_check_node` - validates Cloudflare config / deployment config
7. `github_check_node` - checks workflow syntax and branch rules

**Edges:** `START > build > security > brand > qa > prose > infra > github > END`

**Outputs:**
- JSON: `infra/reports/ship_gate-{branch}.json`
- Markdown: `infra/reports/ship_gate-{branch}.md` (used in PR comments)

### 10.4 Integration Points

- **GitHub Actions** - workflow runs Ship Gate graph on PRs to `main`
- **`/ship` trigger** - runs the graph locally before push + PR
- **Claude Code** - command palette action for local pre-PR validation

### 10.5 Novel RelayLaunch Use

Create a **public "Safety Badge"** for your marketing site. Add a small element
on case studies that says "This feature passed 7 agent checks at launch." This
turns an internal LangGraph pipeline into a visible trust signal.

**Phase:** 3

---

## 11. CrewAI - Service-Tier Crews

### 11.1 Repos

- CrewAI main: [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)
- CrewAI examples: [crewAIInc/crewAI-examples](https://github.com/crewAIInc/crewAI-examples)
- CrewAI quickstart: [alexfazio/crewAI-quickstart](https://github.com/alexfazio/crewAI-quickstart)

### 11.2 Role in RelayLaunch

CrewAI orchestrates **small teams of agents** (BMAD + Agency + Contains Studio) to
deliver the four core service tiers:

- **Complete Analysis** (Signal/Blueprint) - diagnostic + roadmap
- **Launch** - build & connect
- **Run** - standard retainer
- **Scale** - premium growth retainer

Each tier becomes a defined Crew with agents, tasks, and outputs that map directly
to existing documents and website promises.

### 11.3 Project Structure

**Location:** `crews/relay/` (in separate `relaylaunch-agents` repo)

```
crews/
  relay/
    complete_analysis/
      crew.py
      config/
        agents.yaml
        tasks.yaml
    launch/
      crew.py
      config/
        agents.yaml
        tasks.yaml
    run/
      crew.py
      config/
        agents.yaml
        tasks.yaml
    scale/
      crew.py
      config/
        agents.yaml
        tasks.yaml
```

### 11.4 Complete Analysis Crew (Signal/Blueprint)

**Agents:**
- `analyst` - BMAD *analyst + research skill; uses Perplexity Pro + NotebookLM
- `ux_researcher` - Agency UX + Contains Studio UX agent
- `pm` - BMAD *pm; synthesizes into roadmap and tier recommendation
- Optional `infra_reviewer` - BMAD architect/ops for infra-heavy clients

**Tasks:**
- `discover_stack` - inventory web, tools, automations using intake + exports
- `ux_messaging_review` - evaluate website and messaging vs Relay standards
- `ops_automation_review` - map automations and gaps
- `synthesize_report` - produce markdown/PDF Blueprint report
- `draft_roadmap` - 30/90-day plan with suggested entry tier

### 11.5 Launch Crew

**Agents:**
- `architect` - BMAD architect + Contains architecture agent
- `dev` - BMAD dev + Superpowers coding workflow
- `devops` - DevOps Automator (Contains) + BMAD ops
- `brand_guardian` - Agency Brand + Contains Brand Guardian
- `qa` - BMAD QA + website/Control Center QA specs

**Tasks:**
- `design_architecture` - produce architecture doc
- `implement_site` - follow website build framework to build pages and quality gates
- `run_ship_gate` - call LangGraph Ship Gate before handoff
- `prepare_case_study_notes` - capture before/after snapshots

### 11.6 Run & Scale Crews

**Agents:**
- `pm` - orchestrates monthly work
- `content_creator` - Agency/Contains content agent
- `seo_pm` - BMAD PM/SEO
- `growth_hacker` - Agency/Contains growth
- `analytics_reporter` - Contains analytics agent + Gemini data agent

**Tasks:**
- `collect_metrics` - call Gemini for SEO/traffic and Lighthouse performance
- `plan_content` - propose posts/updates supporting client goals
- `plan_optimizations` - technical SEO and automation tweaks
- `generate_report` - monthly/quarterly report and next actions

### 11.7 Integration Points

- **n8n:** intake form > trigger Complete Analysis Crew with client metadata
- **GitHub Actions / CI:** CLI wrappers to trigger crews for test/demo runs
- **Control Center:** store Crew run outputs and status in Supabase as client history

### 11.8 Novel RelayLaunch Uses

1. **"RelayLaunch On RelayLaunch"** - periodically run Complete Analysis and Launch
   crews on your own business. Store results as "dogfooding reports" and selectively
   anonymize into public content.

2. **Crew-powered productized audits** - offer a tiny, low-priced "Signal Mini"
   product that reuses the Complete Analysis crew but only runs 1-2 tasks (website +
   tooling snapshot).

**Phase:** 2

---

## 12. Dotprompt - Typed Templates for Audits & Reports

### 12.1 Repos

- Dotprompt main: [google/dotprompt](https://github.com/google/dotprompt)
- Dotprompt spec: [google.github.io/dotprompt](https://google.github.io/dotprompt)

### 12.2 Role in RelayLaunch

Dotprompt acts as the **schema layer** underneath LangGraph nodes, CrewAI tasks,
and CI workflows. Instead of ad-hoc prompts, we define structured templates for:

- QA audits (website, Control Center)
- SEO audits and growth diagnostics
- Complete Analysis report skeletons
- Control Center API reviews

### 12.3 Project Structure

**Location:** `dotprompts/` (in separate `relaylaunch-agents` repo)

Files to create:
- `qa-audit.prompt` - for Ship Gate QA node
- `seo-audit.prompt` - for `?growth` / `do growth` and Run/Scale crews
- `complete-analysis.prompt` - for Complete Analysis Crew synthesis step
- `cc-api-review.prompt` - for Control Center API/Data Model checks

### 12.4 Integration Points

- **LangGraph:** nodes call Dotprompt templates instead of raw prompts
- **CrewAI:** tasks use Dotprompt for consistent structured outputs
- **n8n / CLI:** small scripts run templates for ad-hoc audits

### 12.5 Novel RelayLaunch Use

Create a **"Blueprint to Metrics" bridge.** For each client, run the same
`complete-analysis.prompt` every 6-12 months and store results in Control Center.
Show a timeline of "what the system looked like at each milestone." This turns
Dotprompt outputs into a living client health history.

**Phase:** 2

---

## 13. Contains Studio Agents - Ported Specialists

### 13.1 Repos

- Contains Studio main: [contains-studio/agents](https://github.com/contains-studio/agents) (12,242 stars)
- Contains Studio org: [github.com/contains-studio](https://github.com/contains-studio)

**Directory layout:**
- `design/` - brand-guardian, ui-designer, ux-researcher, etc.
- `engineering/` - backend-architect, devops-automator, frontend-developer, etc.
- `marketing/` - content-creator, growth-hacker, social agents
- `product/`, `project-management/`, `studio-operations/`, `testing/`, `bonus/`

### 13.2 Integration Plan

**Location:** `external/studio-agents/` (submodule, pinned SHA)

For each chosen agent, create a wrapper prompt:
- `docs/agents/relay-brand-guardian.prompt.md` wrapping `design/brand-guardian.md`
- `docs/agents/relay-devops-automator.prompt.md` wrapping `engineering/devops-automator.md`
- `docs/agents/relay-content-creator.prompt.md` wrapping `marketing/content-creator.md`
- `docs/agents/relay-growth-hacker.prompt.md` wrapping `marketing/growth-hacker.md`
- `docs/agents/relay-analytics-reporter.prompt.md` wrapping `studio-operations/analytics-reporter.md`

**Wrapper rules:**
- Keep core responsibilities and strengths
- Replace stack/tools with Relay preferred stack (Astro, Cloudflare, Supabase, n8n)
- Enforce brand and voice from CLAUDE.md (4-color system, voice guidelines)
- Document new triggers in `docs/agents.md` and `rl-trigger-system-v1.md`

### 13.3 Suggested Domain Mappings

| Relay Wrapper | Source | Domain | Triggers |
|---------------|--------|--------|----------|
| relay-brand-guardian | design/brand-guardian.md | brand | `?brand`, `!brand` |
| relay-devops-automator | engineering/devops-automator.md | ops | `?ops`, `!ops` |
| relay-content-creator | marketing/content-creator.md | growth | `!growth` |
| relay-growth-hacker | marketing/growth-hacker.md | growth | `~growth` |
| relay-analytics-reporter | studio-operations/analytics-reporter.md | ops + growth | monthly reports |

### 13.4 Novel RelayLaunch Uses

1. **"Studio Shadow Team"** - run a monthly retro where Project Shipper, Experiment
   Tracker, and Studio Coach review how RelayLaunch itself is operating.

2. **Silent co-pilot for client retainers** - for Run/Scale clients, quietly run
   Analytics Reporter + Growth Hacker + DevOps Automator monthly and use their output
   to enhance your human-written reports.

**Phase:** 1

---

## 14. External Resources & Future Verticals

| Resource | GitHub | Status | Relay Use | Novel Application |
|----------|--------|--------|-----------|-------------------|
| gstack | [garrytan/gstack](https://github.com/garrytan/gstack) | Active | Meta-role overlays | "Founder Review" page in Blueprint reports |
| claude-skills | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | Phase 1 | Atomic micro-skills | Monthly "Skill Sprint" for self-improvement |
| free-for-dev | [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev) | Research | Tools Coach + Analysis | "Frugal Stack" appendix in Blueprints |
| OpenBB | [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | Future | Founder finance data | Internal business health dashboards |
| MindsDB | [mindsdb/mindsdb](https://github.com/mindsdb/mindsdb) | Future | Control Center data agents | "3 things worth looking at this week" Slack bot |
| GLM-5 | [docs.z.ai](https://docs.z.ai/guides/llm/glm-5) | Future | Infra super-architect | "Red Team Architect" second opinion on big bets |
| http.zig | [karlseguin/http.zig](https://github.com/karlseguin/http.zig) | Future | Ultra-lean edge services | "Performance Lab" portfolio example |
| public-apis | [public-apis/public-apis](https://github.com/public-apis/public-apis) | Research | API discovery for clients | Enrich Complete Analysis with integration options |

---

## 15. Links & Resources

### Core Frameworks (4)
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

### Meta-Roles & Skills
- [gstack](https://github.com/garrytan/gstack) — Executive role overlays (CEO, Eng Manager)
- [claude-skills](https://github.com/alirezarezvani/claude-skills) — Micro-skills library

### Research & Data
- [free-for-dev](https://github.com/ripienaar/free-for-dev) — Free tier SaaS/tool catalog
- [public-apis](https://github.com/public-apis/public-apis) — API discovery catalog
- [OpenBB](https://github.com/OpenBB-finance/OpenBB) — Finance data platform
- [MindsDB](https://github.com/mindsdb/mindsdb) — AI data agents platform

### Future Infrastructure
- [GLM-5](https://docs.z.ai/guides/llm/glm-5) — Infra super-architect model
- [http.zig](https://github.com/karlseguin/http.zig) — Ultra-lean HTTP server
