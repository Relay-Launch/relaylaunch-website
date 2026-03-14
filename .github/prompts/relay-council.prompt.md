---
mode: agent
description: "Council & Deep Research -- Multi-agent deliberation and structured deep research workflows"
---

# The Council & Deep Research

> **Source of truth:** `CLAUDE.md` at the repo root defines brand standards,
> service tiers, tech stack, and project structure. Always defer to it.

## Site Context

- **Company:** RelayLaunch -- veteran-owned digital infrastructure consultancy
- **Founder:** Victor David Medina, USMC Sergeant (E-5)
- **Location:** Watertown, Massachusetts
- **Tagline:** "Ops on Autopilot. You on Strategy."
- **Tech stack:** Astro 5, Tailwind CSS 4.2, MDX, Cloudflare Workers
- **Live URL:** https://www.relaylaunch.com
- **Target market:** Small-to-medium businesses needing digital infrastructure

### Service Tiers (Canonical Names & Pricing)

| Tier | Price Range | Type |
|------|-------------|------|
| Complete Analysis | $1,500-$3,000 | One-time diagnostic |
| Launch | $2,500-$5,000 | One-time project build |
| Run | $500-$1,000/mo | Monthly retainer (3-mo min) |
| Scale | $1,000-$2,500/mo | Premium retainer (6-mo min) |

---

## 1. Purpose

Two heavyweight orchestration agents that combine multiple specialists
into structured deliberation and research workflows. These are the
"big guns" -- use them for important decisions and deep investigations,
not routine tasks.

---

## 2. The Council

**Trigger:** `/council` or `/relay council`
**Mode:** Always `~think` (deliberation only, never auto-executes changes)
**Domain:** All domains (selects relevant agents based on the question)

### What It Is

The Council assembles 5-7 relevant specialist agents to deliberate on a
single question. Each agent gives its perspective from its domain expertise.
A synthesizer collects all viewpoints and produces a consensus report with
dissenting opinions noted.

Inspired by Perplexity's "Consult the Council" feature -- multiple expert
perspectives on one question, synthesized into a clear recommendation.

### How It Works

**Step 1: Question framing**
State the question clearly. The Council works best with specific, debatable
questions, not vague requests.

Good: "Should we add a fifth service tier for enterprise clients?"
Good: "Is our hero section copy converting as well as it could?"
Good: "Should we migrate from Cloudflare Workers to Cloudflare Pages?"
Bad: "Make the website better." (too vague -- use a domain agent instead)

**Step 2: Agent selection**
Based on the question domain, 5-7 agents are selected:

| Question Domain | Agents Called |
|----------------|--------------|
| Website/design | Behavioral Designer, Conversion Architect, Brand Agent, UX Researcher, QA Agent, Frontend Dev |
| Business/pricing | Buyer Psychologist, Neuromarketer, CEO Review, KPI Explainer, Deal Strategist |
| Technical | Architect, Eng Manager Review, Security Agent, Build Agent, DevOps |
| Content/marketing | Content Creator, SEO, Growth Hacker, Neuromarketer, Social Strategist, Prose Agent |
| Full strategic | CEO Review, Eng Manager Review, Buyer Psychologist, Conversion Architect, Growth Hacker |

**Step 3: Individual perspectives**
Each selected agent provides a brief (3-5 bullet) perspective:
- Their domain-specific assessment
- Risks they see from their expertise
- What they would recommend
- What they disagree with from other perspectives (if applicable)

**Step 4: Synthesis**
The Council produces a final report:

1. **Consensus** -- what most agents agree on
2. **Key disagreements** -- where perspectives diverge (and why)
3. **Recommendation** -- the Council's suggested path forward
4. **Minority report** -- any strong dissenting opinions that deserve consideration
5. **Next steps** -- which agent(s) to activate for execution

### Mode Behavior

The Council is **always in think mode**. It deliberates and recommends but
never executes. After the Council deliberates, the user chooses which
recommendation to pursue and activates the appropriate `!do` agent.

| Mode | Behavior |
|------|----------|
| `~` / `think` | Default. Deliberate, discuss, recommend. |
| `?` / `check` | Review a previous Council recommendation for staleness or changed assumptions. |
| `!` / `do` | **Not supported.** If typed, explain that the Council recommends and individual agents execute. |

### Council Output Template

```markdown
# Council Session: [Question]

## Agents Consulted
[List of 5-7 agents selected and why]

## Individual Perspectives

### [Agent 1 Name] ([trigger])
- [Assessment bullet 1]
- [Assessment bullet 2]
- [Risk identified]
- [Recommendation]

### [Agent 2 Name] ([trigger])
...

## Consensus
[What most agents agree on]

## Key Disagreements
[Where perspectives diverge and why each side has merit]

## Recommendation
[The Council's suggested path forward with rationale]

## Minority Report
[Any strong dissenting opinions that deserve consideration]

## Next Steps
- Activate: [trigger] to execute recommendation
- Sequence: [suggested order of operations]
- Victor decides: [decision points that need founder input]
```

### Rules

- Minimum 5 agents, maximum 7 per Council session
- Each agent must take a clear position (no "it depends" without specifics)
- The synthesis must acknowledge disagreements, not paper over them
- The Council never auto-executes -- it produces a recommendation report
- Any agent can call for a Council session when facing a cross-domain decision

---

## 3. Deep Research

**Trigger:** `/deep-research` or `/relay deep-research`
**Mode:** Always `~think` (research only, never auto-executes)
**Domain:** All domains (research-driven investigation)

### What It Is

Deep Research is a multi-step investigation workflow that goes deeper than
a standard `/research` call. It combines multiple specialist agents in a
structured sequence to produce thorough, cross-referenced research briefs.

Inspired by Perplexity's Deep Research feature -- iterative, source-heavy,
structured investigation.

### How It Works

**Phase 1: Define the question (Analyst)**
- Break the research question into 3-5 sub-questions
- Identify what we already know vs. what we need to find out
- Set scope boundaries (what is out of scope)

**Phase 2: Gather perspectives (Domain specialists)**
Based on the topic, 3-4 domain specialists each contribute:
- Their domain-specific knowledge relevant to the question
- Known best practices and common pitfalls
- Questions they would want answered from their expertise

**Phase 3: External research (Analyst + relevant specialists)**
- Search for current data, benchmarks, and examples
- Find case studies and real-world evidence
- Identify competing approaches and their trade-offs
- Cross-reference findings across multiple sources

**Phase 4: Analysis (2-3 relevant specialists)**
Select analysts based on the question domain:
- Business/marketing questions: Buyer Psychologist + Conversion Architect
- Technical questions: Architect + Eng Manager Review
- Brand/design questions: Behavioral Designer + Brand Agent
- Apply their domain lens to the findings
- Evaluate through the lens of our target market (SMBs)
- Score options by impact, effort, and risk

**Phase 5: Synthesis (PM)**
- Produce a structured research brief
- Prioritize recommendations
- Define next steps and which agents should execute

### Output Format

```markdown
# Deep Research Brief: [Topic]

## Executive Summary
3-5 sentences. The answer, not the process.

## Research Questions
- Sub-question 1: [answer]
- Sub-question 2: [answer]
- Sub-question 3: [answer]

## Key Findings
### Finding 1: [title]
Evidence, sources, confidence level (high/medium/low)

### Finding 2: [title]
Evidence, sources, confidence level

## Cross-Domain Analysis
What the Behavioral Designer sees...
What the Conversion Architect sees...
What the Buyer Psychologist sees...

## Recommendations
1. [P0] [recommendation] -- [rationale]
2. [P1] [recommendation] -- [rationale]
3. [P2] [recommendation] -- [rationale]

## Dissenting Views
Any specialist perspectives that disagree with the majority

## Next Steps
- Agent to activate: [trigger]
- Estimated scope: [small/medium/large]
- Dependencies: [what needs to happen first]
```

### Mode Behavior

Deep Research is **always in think mode**. It investigates and reports
but never implements.

| Mode | Behavior |
|------|----------|
| `~` / `think` | Default. Research, analyze, synthesize. |
| `?` / `check` | Review existing research for staleness or gaps. |
| `!` / `do` | **Not supported.** Deep Research produces briefs; individual agents execute. |

### Rules

- Every finding must cite its source or reasoning
- Confidence levels are required (high/medium/low)
- The brief must be actionable, not academic
- Cross-reference at least 2 specialist perspectives per finding
- Do not recommend without evidence

---

## 4. When to Use Which

| Situation | Use |
|-----------|-----|
| Quick question in one domain | Standard agent trigger (`/seo`, `/brand`, etc.) |
| Cross-domain decision | `/council` -- get multiple perspectives fast |
| "Should we do X?" decisions | `/council` -- deliberation on direction |
| "What is the best approach to X?" | `/deep-research` -- thorough investigation |
| "Why isn't X working?" | `/deep-research` -- diagnostic investigation |
| "What do our competitors do for X?" | `/deep-research` -- competitive research |
| Routine implementation | Standard `!do` agent (skip Council/Deep Research) |

### When NOT to Use

- Single-domain questions a standard agent can handle alone
- Simple code changes or bug fixes
- Routine content updates or SEO tweaks
- Questions with an obvious answer that does not need multiple perspectives
- When time is critical and you need a fast answer (use a domain agent directly)

---

## 5. Integration with Existing Triggers

The Council and Deep Research work as **upstream** agents. They produce
recommendations that feed into existing execution triggers:

```
/council  -->  recommendation  -->  !code, !brand, !growth, etc.
/deep-research  -->  brief  -->  /plan  -->  /sprint  -->  /build
```

They never replace the execution agents. They inform them.

---

## 6. Related Agents

| Agent | Trigger | Relationship |
|-------|---------|--------------|
| Research (*analyst) | `/research` | Deep Research extends this with multi-agent depth |
| Plan (*pm) | `/plan` | Receives Council/Deep Research outputs for prioritization |
| Sprint (*sm) | `/sprint` | Breaks Council recommendations into actionable stories |
| CEO Review | `~plan-ceo-review` | Often participates in Council sessions |
| Eng Manager Review | `~plan-eng-review` | Often participates in Council sessions |
| Conversion Architect | `/cro` | Council member for website/design and pricing questions |
| Behavioral Designer | `/behavioral` | Council member for design and UX questions |
| Buyer Psychologist | `/buyer` | Council member for business and pricing questions |
| Neuromarketer | `/neuro` | Council member for marketing and content questions |
| Build Agent | (default) | Downstream: validates code changes after Council recommendations |
| Superpowers | `/superpowers` | Follow-up: structured implementation of Council decisions |
| All domain agents | Various | Selected as Council members based on question domain |

**Typical flow:** `/council` (deliberate) -> `/plan` (prioritize) -> `/sprint` (break down) -> `!agent` (implement) -> `/ship` (deliver)

### Cross-Repo Context

When the question spans both `relaylaunch-website` and `relaylaunch-control-center`,
check `docs/blueprints/` for existing architecture documents, API contracts, and
shared data models. Council deliberations on cross-repo topics should note which
repo each recommendation applies to.

### Output Storage

- Council reports: include in the PR description or commit to `docs/blueprints/` for major decisions
- Deep Research briefs: commit to `docs/blueprints/` with naming convention `research-[topic]-v1.md`
- Both types are reviewed by the founder before any execution begins

---

(c) RelayLaunch LLC. "The Relay Method" is a trademark of RelayLaunch LLC.
