# Agent Frameworks Integration Guide — v1

> How to extend The Relay Method from prompt-based agent orchestration to
> code-executable, repeatable, client-facing automation.

**Status:** Planning
**Owner:** Victor David Medina
**Last Updated:** 2026-03-14

---

## Overview

The Relay Method already has 3 installed frameworks (BMAD, Agency,
Superpowers) and 16 prompt files. This blueprint covers the next layer:
turning those prompts into executable workflows using 5 additional
frameworks. Each section covers what it is, why it fits RelayLaunch,
how to install and use it, and when it is best used.

---

## 1. LangGraph — Executable Ship Gate and Stateful Workflows

### What It Is
Graph-based agent orchestration framework from LangChain. Lets you build
stateful, multi-step, multi-agent workflows as directed graphs with
nodes, edges, conditional routing, retries, and memory.

- **Source:** https://github.com/langchain-ai/langgraph
- **Docs:** https://docs.langchain.com/oss/langgraph/overview
- **Languages:** Python (`pip install langgraph langchain`) and
  TypeScript (`npm install @langchain/langgraph`)

### Why It Fits RelayLaunch
Your Ship Gate (Build > Security > Brand > QA > Prose > Infra > GitHub)
maps naturally to LangGraph nodes and edges. Each node calls the
appropriate BMAD/default agent prompt and returns pass/fail. The graph
only proceeds to `push_and_pr` when all checks pass.

### How to Install and Use

**Directory:** `infra/langgraph/`

```bash
# Python setup
mkdir -p infra/langgraph
cd infra/langgraph
python -m venv .venv
source .venv/bin/activate
pip install langgraph langchain anthropic
```

**Ship Gate Graph (conceptual):**
```python
# infra/langgraph/ship_gate.py
from langgraph.graph import StateGraph, END

class ShipGateState(TypedDict):
    files_changed: list[str]
    build_result: str    # pass | fail
    security_result: str
    brand_result: str
    qa_result: str
    prose_result: str
    infra_result: str
    github_result: str
    all_passed: bool

def build_check(state): ...   # calls bmad-build rules
def security_check(state): ... # calls bmad-security rules
def brand_check(state): ...    # calls bmad-audit rules
def qa_check(state): ...       # calls bmad-qa rules
def prose_check(state): ...    # calls bmad-prose rules
def infra_check(state): ...    # calls bmad-infra rules (if config changed)
def github_check(state): ...   # calls bmad-github rules (if workflows changed)

graph = StateGraph(ShipGateState)
graph.add_node("build", build_check)
graph.add_node("security", security_check)
graph.add_node("brand", brand_check)
graph.add_node("qa", qa_check)
graph.add_node("prose", prose_check)
graph.add_node("infra", infra_check)
graph.add_node("github", github_check)

# Sequential edges matching Ship Gate order
graph.set_entry_point("build")
graph.add_edge("build", "security")
graph.add_edge("security", "brand")
graph.add_edge("brand", "qa")
graph.add_edge("qa", "prose")
graph.add_edge("prose", "infra")
graph.add_edge("infra", "github")
graph.add_edge("github", END)
```

**GitHub Actions integration:**
Trigger on `/ship` comment or `ship/*` branch push. Block merge unless
the graph returns PASS for all nodes.

### When to Use
- On every production deploy (`/ship`)
- On PRs that touch infra, UI, or content
- For complex runbooks (HRC build QA pipeline, integration projects)
- When you want consistent, auditable gate checks across repos

### Business Impact
"Every change passes a 7-agent graph-based gate before deploy" becomes
a selling point in proposals. Clients see structured, automated quality
assurance, not manual review.

---

## 2. CrewAI — Productized Service-Tier Crews

### What It Is
Production-grade multi-agent framework where you define Agents, Tasks,
and Crews with sequential or hierarchical processes. Very close to
the BMAD lineup — a "Crew" is your Analyst > PM > Architect > Dev > QA team.

- **Source:** https://github.com/crewAIInc/crewAI
- **Examples:** https://github.com/crewAIInc/crewAI-examples
- **Docs:** https://docs.crewai.com
- **Install:** `pip install crewai crewai-tools`

### Why It Fits RelayLaunch
Your service tiers (Complete Analysis, Launch, Run, Scale) are
repeatable multi-agent jobs. CrewAI turns them into code-backed,
consistent, scalable workflows instead of ad-hoc prompting.

### How to Install and Use

**Directory:** `crews/`

```bash
mkdir -p crews
cd crews
pip install crewai crewai-tools anthropic
```

**Service-Tier Crews:**

#### Complete Analysis Crew (`crews/relay_complete_analysis.py`)
- **Agents:** BMAD *analyst, *pm, Agency UX Researcher
- **Input:** Client URLs, tool stack inventory, uploaded docs
- **Process:**
  1. *analyst researches client's tech stack, digital presence, competitors
  2. UX Researcher evaluates user experience across all touchpoints
  3. *pm prioritizes findings into 20-30 page report with 30/90-day roadmap
- **Output:** Blueprint deliverable (markdown report in `docs/client-reports/`)
- **Maps to:** Signal / Blueprint public packages

#### Launch Crew (`crews/relay_launch.py`)
- **Agents:** BMAD *architect, *dev, Agency Frontend Developer, DevOps Automator
- **Input:** Requirements doc, brand assets, architecture decisions
- **Process:**
  1. *architect designs system and component structure
  2. Frontend Developer and *dev implement the build
  3. DevOps Automator sets up CI/CD, hosting, monitoring
- **Output:** Architecture docs, build plan, ticket breakdown
- **Maps to:** Relay public package

#### Run Crew (`crews/relay_run.py`)
- **Agents:** BMAD *pm, *qa, Agency Content Creator, BMAD *pm (SEO)
- **Input:** Monthly goals, content calendar, analytics data
- **Process:**
  1. *pm plans monthly deliverables and priorities
  2. Content Creator produces blog posts, social content, copy
  3. SEO *pm audits and optimizes search performance
  4. *qa audits brand compliance on all new content
- **Output:** Monthly report, content assets, SEO fixes
- **Maps to:** Sustain public package

#### Scale Crew (`crews/relay_scale.py`)
- **Agents:** BMAD *pm, Agency Growth Hacker, PPC Strategist, Content Creator
- **Input:** Quarterly OKRs, growth targets, budget
- **Process:**
  1. *pm sets quarterly growth OKRs and sprint plans
  2. Growth Hacker designs experiments and conversion funnels
  3. PPC Strategist manages paid acquisition channels
  4. Content Creator produces high-volume content assets
- **Output:** Quarterly growth plan, experiment results, campaign reports

### When to Use
- Kicking off a new paid engagement (any service tier)
- Generating proposals and SOWs from crew outputs
- Monthly retainer deliverables (consistent level of analysis every time)
- Client onboarding (run the Complete Analysis Crew for every new client)

### Business Impact
Repeatable, code-backed versions of your high-ticket workflows. Every
client gets the same depth of analysis. Scale without hiring.

---

## 3. Dotprompt — Typed, Versioned Prompt Templates

### What It Is
Google's framework for executable prompt templates with input/output
schemas, versioning, and CI/CD tooling. Turns your BMAD prompts into
typed templates that tools and pipelines can call directly.

- **Source:** https://github.com/google/dotprompt
- **Install:** `pip install dotprompt` or `npm install @google/dotprompt`

### Why It Fits RelayLaunch
Your 16 BMAD prompt files already follow a pattern. Dotprompt adds:
- Input schemas (what data the prompt needs)
- Output schemas (structured JSON responses)
- Versioning (track prompt changes over time)
- CI/CD integration (call prompts from GitHub Actions or n8n)

### How to Install and Use

**Convert BMAD prompts to Dotprompt format:**

Example for `bmad-qa` (QA Agent):
```yaml
# .github/prompts/bmad-qa.prompt
name: relay_qa_audit
model: claude-opus-4-6
input:
  schema:
    files_changed:
      type: array
      items: { type: string }
    brand_rules:
      type: object
    a11y_targets:
      type: string
      default: "WCAG AA"
output:
  schema:
    violations:
      type: array
      items:
        type: object
        properties:
          file: { type: string }
          line: { type: number }
          severity: { type: string, enum: [P0, P1, P2] }
          category: { type: string }
          suggested_fix: { type: string }
    summary:
      type: object
      properties:
        total_issues: { type: number }
        p0_count: { type: number }
        passed_checks: { type: array, items: { type: string } }
---
You are the BMAD *qa agent...
```

**Priority templates to convert:**
1. `bmad-qa` — PR comments with structured QA results
2. `bmad-seo` — SEO audit reports for client deliverables
3. `bmad-security` — Security scan results for CI pipeline
4. `bmad-audit` — Brand compliance checks for automated gatekeeping
5. `bmad-prose` — Prose violations for content pipelines

### When to Use
- In CI (GitHub Actions): automated PR comments with structured QA/security results
- In n8n workflows: trigger prompt runs on schedule for monthly client reports
- For consistent, machine-readable outputs: Slack summaries, PDF reports
- When you need prompt version tracking and behavior stability

### Business Impact
Consistent, machine-readable outputs that feed into client reports.
Prompt behavior stays stable as you iterate. Monthly Sustain reports
become automated instead of manual.

---

## 4. Contains Studio Agents — Extended Agent Library

### What It Is
Large library of markdown agent definitions for engineering, design,
marketing, product, ops, and PM. Many map nearly 1:1 to your existing
Relay Method categories.

- **Source:** https://github.com/contains-studio/agents

### Why It Fits RelayLaunch
Their agents (DevOps Automator, Brand Guardian, Content Creator, Growth
Hacker, Project Shipper, Analytics Reporter) enrich your existing
triggers with deeper, more nuanced behavior. Think of them as "v2"
personalities for your Agency agents.

### How to Install and Use

```bash
# Add as submodule for reference
git submodule add https://github.com/contains-studio/agents.git external/studio-agents
```

**Integration process:**
1. Read selected agents from `external/studio-agents/`
2. Convert to `.github/prompts/relay-*.prompt.md` format
3. Replace tool/stack references with Astro + Cloudflare + n8n + Mailchimp + Buffer
4. Enforce RelayLaunch voice, tiers, and brand rules from CLAUDE.md
5. Register in agents.md under existing triggers

**Priority agents to port:**
| Studio Agent | Maps To | Enhances |
|-------------|---------|----------|
| DevOps Automator | `/devops` | CI/CD, pipeline, infrastructure |
| Brand Guardian | `/brand` | Brand identity, visual consistency |
| Content Creator | `/content` | Blog, copywriting, editorial |
| Growth Hacker | `/growth` | Acquisition, conversion, experiments |
| Analytics Reporter | `/relay run` | Monthly metrics and reporting |
| Project Shipper | `/ship` | Delivery coordination, release mgmt |

### When to Use
- When calling `/devops`, `/brand`, `/content`, `/growth` for client work
  and you want richer, more nuanced behavior
- When existing Agency agent descriptions feel too brief for complex tasks
- When onboarding new agents to the Relay Method

### Business Impact
Deeper, battle-tested agent behaviors without writing from scratch.
Faster, better outputs for client deliverables.

---

## 5. NotebookLM — Per-Client Knowledge Vault

### What It Is
Google's AI research tool for building notebooks from PDFs, docs, links.
Has emerging APIs, CLIs, and MCP integrations for programmatic access.

- **Product:** https://notebooklm.google
- **MCP Integration:** https://github.com/PleasePrompto/notebooklm-mcp
- **CLI:** https://github.com/K-dash/nblm-rs

### Why It Fits RelayLaunch
Perfect as the "vault" for client documents: exports, call notes, prior
reports, runbooks, analytics snapshots. Your agents can query the vault
for grounded, cited answers instead of re-parsing docs every time.

### How to Use

**Per-client notebook structure:**
```
NotebookLM Notebook: "[Client Name] — RelayLaunch"
├── Discovery docs (intake forms, call notes)
├── Tool stack inventory
├── Analytics exports (GA4, Search Console, Mailchimp)
├── Prior deliverables (Complete Analysis reports, roadmaps)
├── Integration runbooks (n8n workflows, API configs)
└── Monthly reports (Sustain tier deliverables)
```

**Integration with Relay Method:**
1. BMAD *analyst queries NotebookLM during `/relay analysis` for client
   docs, prior reports, and competitive data
2. CrewAI "Researcher" agent uses NotebookLM MCP to pull facts and
   citations instead of re-parsing raw docs
3. Monthly `/relay run` crews reference NotebookLM for historical context
   and deliverable continuity

### When to Use
- During diagnostics and roadmap creation (doc-heavy tasks)
- When updating a client's system months later and you need instant context
- For cross-referencing findings across multiple client documents
- When building proposals that reference prior work and results

### Business Impact
Instant context for any client, any time. No more "let me re-read
those docs." Proposals cite specific prior findings. Sustain retainer
reports build on historical context automatically.

---

## 6. BMAD Expansions and Community Templates

### What They Are
Community-created extensions to the BMAD Method with additional team
templates, architecture agents, and workflow patterns.

- **my-bmad-method:** https://github.com/menidi/my-bmad-method
- **team-fullstack.txt:** https://github.com/bmadcode/BMAD-METHOD/blob/main/dist/teams/team-fullstack.txt
- **bmad-architecture-agent:** https://github.com/Ricoledan/bmad-architecture-agent
- **BMAD by Evolution:** https://github.com/EvolutionAPI/BMAD-METHOD-BY-EVOLUTION

### How to Use
- Add repos into `external/` for reference
- Port selected agents into `.github/prompts/` with RelayLaunch branding
- Use team templates as "starter graphs" when defining LangGraph or
  CrewAI workflows for full web or integration projects

### When to Use
- Architecture reviews (`/sysdesign`, `/relay arch`)
- Complex infra planning needing battle-tested BMAD patterns
- Refining Ship Gate and QA flows beyond first iteration

---

## 7. Gemini Pro — Google Stack Data Agent

### What It Is
Google's model with strong tool-calling and Workspace integration.
Not a replacement for Claude — used as a specialized data retrieval
agent within your orchestration layer.

- **Docs:** https://ai.google.dev/gemini-api/docs/tools
- **Agent mode:** https://docs.cloud.google.com/gemini/docs/codeassist/agent-mode

### How to Use
Wrap Gemini as a "Google/SEO Data Agent" in CrewAI or LangGraph:
- Call Gemini tools to read Google Sheets, Search Console, PageSpeed, Analytics
- Return structured metrics (traffic, rankings, Core Web Vitals)
- Feed data into your growth/SEO agents and monthly reports

### When to Use
- For clients heavily invested in Google Workspace / SEO / analytics
- When you need fresh, quantitative SEO and performance data
- As data input for Sustain tier monthly reporting

---

## Implementation Roadmap

### Phase 1: Quick Wins (This Month)
- [ ] Add Contains Studio agents as submodule
- [ ] Port top 5 Studio agents to `.github/prompts/relay-*.prompt.md`
- [ ] Set up NotebookLM notebooks for active clients

### Phase 2: Orchestration (Next Month)
- [ ] Install LangGraph (Python) in `infra/langgraph/`
- [ ] Implement Ship Gate as LangGraph graph
- [ ] Wire Ship Gate to GitHub Actions on `/ship` comment

### Phase 3: Service Crews (Month 3)
- [ ] Install CrewAI in `crews/`
- [ ] Build Complete Analysis Crew
- [ ] Build Run (Sustain) Crew for monthly retainer automation

### Phase 4: Template System (Month 4)
- [ ] Convert top 5 BMAD prompts to Dotprompt format
- [ ] Wire Dotprompt to GitHub Actions for automated PR comments
- [ ] Connect Dotprompt outputs to n8n for client report generation

### Phase 5: Full Integration (Quarter 2)
- [ ] Connect NotebookLM to CrewAI crews via MCP
- [ ] Add Gemini as data agent in CrewAI for Google metrics
- [ ] Build end-to-end: lead intake > Complete Analysis Crew > proposal generation

---

## End-to-End Flow: Lead to Retainer

Here's how all frameworks work together in practice:

1. **Lead comes in via relaylaunch.com**
   - n8n captures form, creates NotebookLM notebook with uploaded docs
   - Opens CrewAI "Complete Analysis Crew" run using BMAD roles + Studio agents

2. **Signal/Blueprint diagnostic (CrewAI + NotebookLM)**
   - Analysts query NotebookLM for client docs
   - Crew outputs: Complete Analysis report + 30/90-day roadmap
   - Dotprompt templates ensure consistent report sections

3. **Relay build (CrewAI + BMAD + LangGraph)**
   - New client repo created from template (client CLAUDE.md, client agents.md)
   - CrewAI "Launch Crew" handles architecture, build, brand, DevOps
   - Every PR runs through LangGraph Ship Gate

4. **Sustain retainer (CrewAI + Dotprompt)**
   - Monthly CrewAI "Run Crew" runs content, SEO, automation checkups
   - Dotprompt templates generate structured reports
   - NotebookLM keeps full history for context continuity

5. **Internal improvements (/relay optimize)**
   - Quarterly: CrewAI/LangGraph review and refactor agent prompts
   - Pull in new ideas from BMAD expansions and Contains Studio agents

---

## Client-Facing Differentiation

These frameworks enable concrete selling points:

- **"Every deploy passes a 7-agent automated quality gate"** (LangGraph Ship Gate)
- **"Your project has named AI specialists assigned to it"** (CrewAI Crews)
- **"We track every optimization and its measured impact"** (Dotprompt + reporting)
- **"Your entire project history is instantly accessible"** (NotebookLM vault)
- **"Agent Playbook" PDF** for clients explaining the 3-5 agents on their account

This positions RelayLaunch as a structured, defensible AI-ops consultancy,
not just "another agency that uses ChatGPT."

---

*This blueprint is versioned. Create `-v2` for proposed changes.*
*See `docs/agents.md` for the full Relay Method agent registry.*
