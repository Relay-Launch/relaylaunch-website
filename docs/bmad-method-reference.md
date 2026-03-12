# BMAD Method Reference Guide for Claude Code

A practical reference for using the [BMAD Method](https://github.com/bmad-code-org/BMAD-METHOD) (Breakthrough Method for Agile AI-Driven Development) with Claude Code. A structured, phase-based methodology that orchestrates specialized AI agent personas through the full software development lifecycle — from brainstorming to deployment.

## Installation

```bash
# Requires Node.js v20+
npx bmad-method install

# Non-interactive (CI/CD)
npx bmad-method install --directory /path/to/project --modules bmm --tools claude-code --yes

# Install prerelease
npx bmad-method@next install
```

The installer provisions three artifact directories in your project:
- **Planning artifacts** — Phase 1-3 outputs (briefs, PRDs, architecture docs)
- **Implementation artifacts** — Phase 4 outputs (sprints, stories, reviews)
- **Project knowledge** — Persistent research, documentation, and context

---

## Quick Reference: When to Use What

| Scenario | Agent | Workflow Trigger |
|----------|-------|-----------------|
| Brainstorm a new product idea | Mary (Analyst) | `BP` — Brainstorm Project |
| Research market/competitors | Mary (Analyst) | `MR` — Market Research |
| Write a Product Requirements Doc | John (PM) | `CP` — Create PRD |
| Design user experience flows | Sally (UX Designer) | `CU` — Create UX |
| Design system architecture | Winston (Architect) | `CA` — Create Architecture |
| Break PRD into epics/stories | John (PM) | `CE` — Create Epics and Stories |
| Plan a sprint | Bob (Scrum Master) | `SP` — Sprint Planning |
| Implement a user story | Amelia (Developer) | `DS` — Dev Story |
| Run code review | Amelia (Developer) | `CR` — Code Review |
| Generate automated tests | Quinn (QA) | `QA` — QA Automate |
| Write project documentation | Paige (Tech Writer) | `DP` — Document Project |
| Quick solo build (skip ceremony) | Barry (Quick Flow) | `QS` → `QD` — Quick Spec → Quick Dev |
| Check if ready to build | Winston (Architect) | `IR` — Implementation Readiness |
| Mid-project course correction | Bob (Scrum Master) | `CC` — Course Correction |
| Sprint retrospective | Bob (Scrum Master) | `ER` — Epic Retrospective |

---

## Core Philosophy

BMAD positions AI agents as **expert collaborators who guide you through a structured process** — not tools that do the thinking for you. Key principles:

- **Phase-gated delivery** — Work flows through Analysis → Planning → Solutioning → Implementation
- **Agent personas** — Each agent has a name, personality, expertise, and communication style
- **Adaptive scaling** — Planning depth adjusts by project complexity (user skill level: Beginner/Intermediate/Expert)
- **Party Mode** — Multiple agent personas collaborate in a single session
- **Zero paywalls** — 100% free and open source (MIT license)

---

## The Four Phases

### Phase 1: Analysis
**Lead agent:** Mary (Business Analyst)

| Workflow | Trigger | Purpose |
|----------|---------|---------|
| Brainstorm Project | `BP` | Expert-guided ideation with final report |
| Market Research | `MR` | Competitive landscape, customer needs analysis |
| Domain Research | `DR` | Industry deep dive, subject matter expertise |
| Technical Research | `TR` | Feasibility assessment, architecture options |
| Create Brief | `CB` | Transform ideas into executive product brief |

**Example prompt:**
```
"As the Analyst agent (Mary), run a Brainstorm Project session for a
veteran-owned digital consultancy website. Focus on differentiators,
target market, and service positioning."
```

### Phase 2: Planning
**Lead agents:** John (PM) + Sally (UX Designer)

| Workflow | Trigger | Agent | Purpose |
|----------|---------|-------|---------|
| Create PRD | `CP` | John (PM) | Facilitated PRD creation through user interviews |
| Validate PRD | `VP` | John (PM) | Comprehensiveness and coherence review |
| Edit PRD | `EP` | John (PM) | Update existing PRD |
| Create UX Design | `CU` | Sally (UX) | UX plan to inform architecture and implementation |

**Example prompt:**
```
"As the PM agent (John), create a PRD for a services page rebuild.
The target audience is small business owners who need managed IT
infrastructure. Include user personas and success metrics."
```

### Phase 3: Solutioning
**Lead agents:** Winston (Architect) + John (PM) + Bob (Scrum Master)

| Workflow | Trigger | Agent | Purpose |
|----------|---------|-------|---------|
| Create Architecture | `CA` | Winston | Document technical decisions, stack, patterns |
| Create Epics and Stories | `CE` | John (PM) | Break PRD into development specifications |
| Implementation Readiness | `IR` | Winston | Verify PRD + UX + Architecture + Stories alignment |

**Example prompt:**
```
"As the Architect agent (Winston), create the architecture for an
Astro 5 + Tailwind CSS site deployed to Cloudflare Workers. Include
content collections for blog posts, static output, and SEO strategy."
```

### Phase 4: Implementation
**Lead agents:** Bob (Scrum Master) + Amelia (Developer) + Quinn (QA)

| Workflow | Trigger | Agent | Purpose |
|----------|---------|-------|---------|
| Sprint Planning | `SP` | Bob (SM) | Generate task sequencing for developer execution |
| Create Story | `CS` | Bob (SM) | Prepare implementation-ready stories with context |
| Dev Story | `DS` | Amelia (Dev) | Implement tests and code for a story |
| Code Review | `CR` | Amelia (Dev) | Multi-faceted quality review |
| QA Automate | `QA` | Quinn (QA) | Generate API and E2E tests |
| Course Correction | `CC` | Bob (SM) | Mid-implementation pivot guidance |
| Sprint Status | — | Bob (SM) | Status tracking and reporting |
| Retrospective | `ER` | Bob (SM) | Post-epic reflection and learnings |

**Example prompt:**
```
"As the Developer agent (Amelia), implement story DS-003: Add responsive
navigation component. Read the full story file before starting. Run all
tests after each task."
```

---

## Agent Roster

### BMM Module Agents (8 agents)

| Agent Name | Title | Specialty | Communication Style |
|------------|-------|-----------|-------------------|
| **Mary** | Business Analyst | Market research, requirements elicitation, competitive analysis, domain expertise | Enthusiastic, methodical, engaging discovery |
| **John** | Product Manager | PRD creation, user interviews, stakeholder alignment, 8+ yrs B2B/consumer | Detective-like, asks "WHY?" relentlessly, data-driven |
| **Sally** | UX Designer | User research, interaction design, UI patterns, 7+ yrs web/mobile | Empathetic advocate, vivid storytelling, creative |
| **Winston** | Architect | Distributed systems, cloud infra, API design, scalable patterns | Pragmatic, measured, weighs possibilities vs. realities |
| **Bob** | Scrum Master | Sprint planning, story prep, agile ceremonies, backlog management | Crisp, checklist-driven, servant leadership |
| **Amelia** | Developer | Story execution, TDD, sequential task implementation | Ultra-succinct, file paths and requirement IDs only |
| **Quinn** | QA Engineer | Test automation, API testing, E2E testing, coverage analysis | Practical, "ship it and iterate," coverage-first |
| **Paige** | Technical Writer | CommonMark, DITA, OpenAPI, Mermaid diagrams, concept explanation | Patient educator, analogies, simplifies complexity |

### Specialized Agents

| Agent Name | Title | Specialty |
|------------|-------|-----------|
| **Barry** | Quick Flow Solo Dev | Rapid spec + implementation with minimal ceremony |
| **BMad Master** | Orchestrator | Runtime resource management, workflow orchestration, platform expert |

---

## Quick Flow: The Fast Path

For smaller projects or when you want to skip full ceremony, Barry (Quick Flow Solo Dev) combines planning and execution:

```
# Step 1: Quick Spec — generates complete technical spec with stories
"As Barry (Quick Flow Solo Dev), run Quick Spec for adding a contact
form with email validation and Cloudflare Turnstile captcha."

# Step 2: Quick Dev — implements end-to-end
"As Barry, run Quick Dev on the spec we just created."

# Step 3 (experimental): Quick Dev New — unified flow
"As Barry, run QQ for a blog RSS feed feature. Handle everything
from intent to implementation in one pass."
```

**Barry's principles:**
- "Planning and execution are two sides of the same coin"
- "Code that ships is better than perfect code that doesn't"
- Ruthless efficiency, minimal overhead

---

## Party Mode: Multi-Agent Collaboration

Party Mode lets multiple agent personas collaborate in a single session. Configured via team files:

- `default-party.csv` — Default multi-agent team composition
- `team-fullstack.yaml` — Full-stack development team

**Example prompt:**
```
"Enter Party Mode with the fullstack team. I need Mary to analyze
requirements, Winston to design architecture, and Bob to create
the sprint plan — all in this session."
```

---

## Core Platform Features

### BMad Master (Orchestrator)
The meta-agent that manages the entire BMAD platform:
- Lists available tasks, workflows, and agents
- Routes requests to the correct specialist
- Loads resources dynamically at runtime
- Provides `bmad-help` skill for contextual guidance

### Core Tasks (Built-in Quality Gates)

| Task | Purpose |
|------|---------|
| Editorial Review (Prose) | Review document prose quality and clarity |
| Editorial Review (Structure) | Review document structural integrity |
| Adversarial Review (General) | Challenge assumptions, find weaknesses |
| Edge Case Hunter | Identify overlooked edge cases and failure modes |
| Document Sharding | Break large documents into manageable sections |
| Documentation Indexing | Generate indexes for project documentation |
| BMad Help | Contextual guidance and platform navigation |

### Core Workflows

| Workflow | Purpose |
|----------|---------|
| Advanced Elicitation | Deep requirement extraction through structured questioning |
| Brainstorming | Facilitated ideation sessions |
| Party Mode | Multi-agent collaborative sessions |

---

## Module Ecosystem

BMAD is extensible through official modules:

| Module | Code | Purpose | Agents/Capabilities |
|--------|------|---------|-------------------|
| **BMad Method** | BMM | Core framework | 8 agents, 34+ workflows, full SDLC |
| **BMad Builder** | BMB | Custom agent/workflow creation | Build your own agents and workflows |
| **Test Architect** | TEA | Risk-based test strategy | Automated test planning and generation |
| **Game Dev Studio** | BMGD | Game development | Unity, Unreal, Godot specializations |
| **Creative Intelligence Suite** | CIS | Innovation and design thinking | Creative processes and ideation |

---

## Workflow Patterns for RelayLaunch

### Pattern 1: Full Client Engagement (Complete Analysis → Launch)
```
Phase 1: Mary (Analyst)
  → BP: Brainstorm Project — understand client needs
  → MR: Market Research — competitive landscape
  → CB: Create Brief — executive summary

Phase 2: John (PM) + Sally (UX)
  → CP: Create PRD — requirements document
  → CU: Create UX — user experience design

Phase 3: Winston (Architect) + Bob (SM)
  → CA: Create Architecture — technical design
  → CE: Create Epics and Stories — development tasks
  → IR: Implementation Readiness — verify alignment

Phase 4: Amelia (Dev) + Quinn (QA) + Bob (SM)
  → SP: Sprint Planning — task sequencing
  → DS: Dev Story — build each story
  → CR: Code Review — quality check
  → QA: Generate tests — automated coverage
  → ER: Retrospective — learnings
```

### Pattern 2: Quick Feature Add (Run/Scale Retainer)
```
Barry (Quick Flow Solo Dev)
  → QS: Quick Spec — rapid requirements + stories
  → QD: Quick Dev — implement immediately
  → CR: Code Review — quality gate
```

### Pattern 3: Website Audit & Improvement
```
Mary (Analyst) → DR: Domain Research on current site
Quinn (QA) → QA: Generate test coverage
Winston (Architect) → CA: Architecture review
Amelia (Dev) → DS: Implement improvements
```

### Pattern 4: Content & Documentation Sprint
```
Mary (Analyst) → MR: Market Research for content topics
John (PM) → CP: Create content PRD
Paige (Tech Writer) → DP: Document Project
Bob (SM) → SP: Sprint plan the content pipeline
```

### Pattern 5: Party Mode Full Build
```
"Enter Party Mode with the fullstack team. We're building a new
services page for RelayLaunch. Mary analyzes the market positioning,
Sally designs the UX flow, Winston specs the Astro component
architecture, Bob creates the sprint plan, and Amelia implements."
```

---

## Combining BMAD with Agency Agents

BMAD provides **methodology and process** (how to build). Agency Agents provide **specialist expertise** (deep domain skills). They complement each other:

| Need | BMAD Agent | Agency Agent | Why Both |
|------|-----------|-------------|---------|
| Requirements | John (PM) creates the PRD | Sprint Prioritizer scores features | Structured doc + data-driven prioritization |
| Architecture | Winston designs the system | Backend Architect reviews decisions | Process-driven design + deep technical review |
| Development | Amelia implements stories | Frontend Developer builds components | Story discipline + framework expertise |
| Testing | Quinn generates test suites | Evidence Collector does visual QA | Automated coverage + screenshot verification |
| Brand review | — | Brand Guardian audits consistency | BMAD doesn't cover brand — Agency fills the gap |
| Security | — | Security Engineer + Threat Detection | BMAD doesn't cover security — Agency fills the gap |
| SEO/Marketing | — | SEO Specialist, Growth Hacker | BMAD is dev-focused — Agency covers marketing |

**Workflow integration:**
1. Use BMAD phases (Analysis → Planning → Solutioning → Implementation) as the process backbone
2. Invoke Agency Agents for specialized reviews at quality gates
3. Use BMAD's Party Mode + Agency's Orchestrator for complex multi-agent coordination

---

## Configuration Options

### User Skill Level
Set during installation — affects how agents communicate:

| Level | Behavior |
|-------|----------|
| **Beginner** | More explanation, guided steps, simpler language |
| **Intermediate** | Balanced guidance, assumes some familiarity |
| **Expert** | Minimal explanation, direct execution, technical shorthand |

### Project Context Template
BMAD generates a `project-context-template.md` in your data directory — fill this in to give all agents persistent knowledge about your project, stack, and constraints.

---

## Tips for Using BMAD with Claude Code

1. **Use workflow triggers**: Start prompts with the 2-letter trigger code (e.g., "Run `CP` to create a PRD") for direct workflow activation.

2. **Name the agent**: Address agents by name — "Winston, create the architecture" — to activate their full persona and communication style.

3. **Follow the phases**: BMAD works best when you flow through phases sequentially. Each phase's output feeds the next.

4. **Use Quick Flow for small tasks**: Don't run the full 4-phase process for a bug fix. Use Barry's `QS` → `QD` for anything that doesn't need full ceremony.

5. **Leverage Party Mode for kickoffs**: When starting a new engagement, Party Mode gets multiple perspectives in one session.

6. **Fill in the project context template**: This gives every agent shared knowledge about your project without repeating yourself.

7. **Combine with Agency Agents**: Use BMAD for process discipline and Agency Agents for domain expertise. They're complementary, not competing.

8. **Trust the agent personalities**: John will ask "why" relentlessly. Amelia will be terse and citation-heavy. Winston will be measured. This is by design — it produces better artifacts.

---

## File Structure Reference

```
src/
├── bmm/                          # BMad Method module
│   ├── agents/
│   │   ├── analyst.agent.yaml        # Mary — Business Analyst
│   │   ├── architect.agent.yaml      # Winston — Architect
│   │   ├── dev.agent.yaml            # Amelia — Developer
│   │   ├── pm.agent.yaml             # John — Product Manager
│   │   ├── qa.agent.yaml             # Quinn — QA Engineer
│   │   ├── sm.agent.yaml             # Bob — Scrum Master
│   │   ├── ux-designer.agent.yaml    # Sally — UX Designer
│   │   ├── quick-flow-solo-dev.agent.yaml  # Barry — Quick Flow
│   │   ├── tech-writer/
│   │   │   ├── tech-writer.agent.yaml      # Paige — Tech Writer
│   │   │   └── tech-writer-sidecar/        # Supporting resources
│   │   └── bmad-skill-manifest.yaml
│   ├── data/
│   │   └── project-context-template.md
│   ├── teams/
│   │   ├── default-party.csv
│   │   └── team-fullstack.yaml
│   ├── workflows/
│   │   ├── 1-analysis/
│   │   │   ├── create-product-brief/
│   │   │   └── research/
│   │   ├── 2-plan-workflows/
│   │   │   ├── create-prd/
│   │   │   └── create-ux-design/
│   │   ├── 3-solutioning/
│   │   │   ├── check-implementation-readiness/
│   │   │   ├── create-architecture/
│   │   │   └── create-epics-and-stories/
│   │   ├── 4-implementation/
│   │   │   ├── code-review/
│   │   │   ├── correct-course/
│   │   │   ├── create-story/
│   │   │   ├── dev-story/
│   │   │   ├── retrospective/
│   │   │   ├── sprint-planning/
│   │   │   └── sprint-status/
│   │   ├── bmad-quick-flow/
│   │   │   ├── bmad-quick-dev-new-preview/
│   │   │   ├── quick-dev/
│   │   │   └── quick-spec/
│   │   ├── document-project/
│   │   ├── generate-project-context/
│   │   └── qa-generate-e2e-tests/
│   ├── module-help.csv
│   └── module.yaml
├── core/                         # BMAD Core Platform
│   ├── agents/
│   │   ├── bmad-master.agent.yaml    # Master Orchestrator
│   │   └── bmad-skill-manifest.yaml
│   ├── tasks/
│   │   ├── bmad-editorial-review-prose/
│   │   ├── bmad-editorial-review-structure/
│   │   ├── bmad-help/
│   │   ├── bmad-index-docs/
│   │   ├── bmad-review-adversarial-general/
│   │   ├── bmad-review-edge-case-hunter/
│   │   └── bmad-shard-doc/
│   ├── workflows/
│   │   ├── advanced-elicitation/
│   │   ├── brainstorming/
│   │   └── party-mode/
│   ├── module-help.csv
│   └── module.yaml
└── utility/
    └── agent-components/
        ├── activation-rules.txt
        ├── activation-steps.txt
        ├── agent-command-header.md
        ├── agent.customize.template.yaml
        ├── handler-action.txt
        ├── handler-data.txt
        ├── handler-exec.txt
        ├── handler-multi.txt
        ├── handler-tmpl.txt
        └── menu-handlers.txt
```

---

*Source: [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) — Breakthrough Method for Agile AI-Driven Development (MIT License)*
