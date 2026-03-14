# The Relay Method™ — Mode + Domain Trigger System v1

> **Status:** Active (implemented)
> **Source of truth:** `relaylaunch-website` repo
> **Applies to:** Claude Code, GitHub Copilot, Cursor, and any AI tool reading
> `CLAUDE.md`, `docs/agents.md`, or `.github/copilot-instructions.md`

---

## Problem Statement

RelayLaunch has 40+ AI agent triggers across three frameworks (BMAD, The
Agency, Superpowers). The current system is flat — every trigger is a
one-word slash command with no inherent structure. This causes:

1. **Trigger overload** — Hard to remember which of 40+ triggers to use
2. **Mode confusion** — Agents execute code changes when the user just
   wanted a review, or brainstorm ideas when the user wanted implementation
3. **Race conditions** — Multiple agents finish at different times, causing
   premature commits or duplicate PRs when one agent pushes while another
   is still working
4. **No review loop** — No easy way to ask an expert agent to "check my
   work" without it rewriting everything
5. **AI writing artifacts** — Em dashes, "leverage," "robust," and other
   AI-isms slip into content without a dedicated guardrail

---

## Solution: Mode + Domain + Gate

Three new concepts layered on top of the existing trigger system:

### 1. Operation Modes (How the Agent Behaves)

Every agent interaction starts with a **mode** that tells the agent what
kind of output you expect. Modes are expressed as either a symbol prefix
or a word prefix — both are equivalent.

| Symbol | Word | Mode Name | Behavior |
|--------|------|-----------|----------|
| `?` | `check` | **Check** | Read-only. Audit, review, report. No code changes. Returns findings only. |
| `!` | `do` | **Do** | Execute. Write code, fix issues, make changes. Produces commits. |
| `~` | `think` | **Think** | Brainstorm. Workshop ideas, research, explore options. No code changes, no final decisions. |

**Rules:**
- If no mode is specified, the agent infers from context (but explicit is
  always better)
- `check` mode agents must NEVER modify files — only read, analyze, report
- `think` mode agents must NEVER modify files or commit — only discuss,
  propose, and explore
- `do` mode is the only mode that produces code changes
- Modes apply to ALL triggers (one-word, contextual, and service-tier)

### 2. Domain Families (What Expertise to Use)

Agents are grouped into seven memorable domain families. Each family maps
to multiple existing triggers and specialists.

| Domain | Covers | Existing Triggers Mapped |
|--------|--------|--------------------------|
| **code** | Engineering, architecture, build, frontend, backend, data models, APIs | `/architect`, `/build`, `/frontend`, `/backend`, `/datamodel`, `/api`, `/devops`, `?code-review`, `/review` |
| **brand** | Colors, fonts, voice, design, UI/UX, aesthetics | `/audit`, `/brandfix`, `/prettify`, `/brand`, `/ui`, `/ux` |
| **growth** | Marketing, SEO, content, social media, ads, email | `/seo`, `/content`, `/growth`, `/social`, `/ads` |
| **ops** | Infrastructure, CI/CD, deployment, security, GitHub workflows | `/infra`, `/security`, `/github`, `/devops` |
| **biz** | Sales, deals, proposals, pipeline, outbound, accounts, founder finance | `/outbound`, `/deals`, `/proposal`, `/coach`, `/pipeline`, `/accounts`, `/discovery`, `~biz-finance`, `?biz-tools` |
| **plan** | Strategy, research, sprint planning, roadmap, KPIs, retrospectives | `/plan`, `/research`, `/sprint`, `~plan-kpi`, `~plan-ceo-review`, `~plan-eng-review`, `~retro` |
| **qa** | Testing, accessibility, Lighthouse, compliance, full workflow | `/qa`, `/superpowers` |

### 3. Combined Usage

Mode + Domain creates a clear, memorable two-part trigger:

| What You Type | What Happens |
|---------------|--------------|
| `?brand` or `check brand` | Review brand compliance across the site. Report only, no changes. |
| `!brand` or `do brand` | Find and fix all brand violations. Produces code changes. |
| `~brand` or `think brand` | Brainstorm brand direction, positioning ideas, messaging options. |
| `?code` or `check code` | Architecture review, code quality audit. Report issues only. |
| `!code` or `do code` | Implement features, fix bugs, write code. |
| `~code` or `think code` | Explore technical approaches, discuss trade-offs. |
| `?growth` or `check growth` | SEO audit, content gap analysis, conversion review. Report only. |
| `!growth` or `do growth` | Write blog posts, optimize meta tags, create social content. |
| `~growth` or `think growth` | Brainstorm marketing strategy, campaign ideas, growth experiments. |
| `?ops` or `check ops` | Review infra config, scan for vulnerabilities, validate CI/CD. |
| `!ops` or `do ops` | Fix deployment issues, update workflows, patch security. |
| `?biz` or `check biz` | Review pipeline health, audit deal strategy, check proposals. |
| `~biz` or `think biz` | Workshop deal approach, explore pricing, brainstorm outreach. |
| `?qa` or `check qa` | Run full QA audit — accessibility, Lighthouse, responsive. |
| `!qa` or `do qa` | Fix QA issues found in audit. |
| `?plan` or `check plan` | Review current roadmap, sprint backlog, priorities. |
| `~plan` or `think plan` | Workshop requirements, explore feature ideas, plan sprints. |

### 4. Drilling Into Specific Agents

The domain families are shortcuts. You can still use specific triggers when
you need a particular specialist. The mode prefix works with any trigger:

| What You Type | What Happens |
|---------------|--------------|
| `?seo` | SEO audit only, no changes |
| `!brandfix` | Fix brand color violations |
| `~architect` | Discuss architecture options |
| `?security` | Security scan, report only |
| `!frontend` | Build UI components |
| `~deals` | Workshop deal strategy |

### 5. Compatibility

The new system is **additive** — all existing triggers continue to work
exactly as before. The Mode + Domain layer is an optional enhancement:

- Old way: `/seo` (still works, behavior inferred from context)
- New way: `?seo` (explicit check mode) or `!seo` (explicit do mode)
- Domain shortcut: `?growth` (activates SEO + content + social agents)

---

## The Ship Gate — Coordinating Multi-Agent Work

### Problem

When multiple agents work in parallel on a branch, they sometimes:
- Create commits at different times, resulting in messy history
- Try to create a PR while another agent is still working
- Push to remote before all work is reviewed

### Solution: Hold Until Ship

**Default behavior:** Agents may commit locally but must NOT push to
remote until the user explicitly signals completion.

**The `/ship` command:**

When the user types `/ship`, the following sequence executes:

1. **Freeze** — All agents stop making changes
2. **Gate check** — The 7 default agents (including Prose Agent) run a
   final review:
   - Build Agent: `npm run build` passes
   - Security Agent: No secrets, no injection vectors
   - Brand Agent: 4-color system, font stack, voice compliance
   - QA Agent: Accessibility, heading hierarchy, Lighthouse targets
   - Prose Agent: No AI-isms in text content
   - Infra Agent: Config files valid (if changed)
   - GitHub Agent: Workflow syntax valid (if changed)
3. **Report** — Results presented to the user
4. **Push** — If all gates pass (or user overrides), push to remote
5. **PR** — Create PR with consolidated summary of all changes

### Rules

- Agents CAN commit locally at any time (allows incremental saves)
- Agents must NOT push to remote without `/ship`
- Agents must NOT create PRs without `/ship`
- `/ship` is the ONLY command that triggers a push + PR
- If a gate check fails, the user is notified and can fix or override
- `/ship --force` bypasses gate checks (use sparingly)

### Emergency Override

If you need to push without the full gate:
- `/ship --force` — Push immediately, skip gate checks
- This should be rare — the gate exists to catch issues

---

## The Prose Agent — 7th Default Agent

### Problem

AI-generated content contains telltale artifacts: em dashes everywhere,
"leverage," "robust," "comprehensive," "streamline," "cutting-edge," and
other words humans rarely use in casual business writing. Currently this
requires manual cleanup in separate commits.

### Solution

Add a **Prose Agent** as the 7th always-on default agent. It activates
on any text or content change and enforces human-sounding language.

### Prose Agent Specification

**Name:** Prose Agent
**Role:** Human language enforcement, AI-ism detection, voice compliance
**Auto-Triggers On:** Any change to `.astro`, `.mdx`, `.md`, or `.json`
files containing visible text content
**Prompt File:** `.github/prompts/bmad-prose.prompt.md`

**What It Catches:**

1. **Em dashes** — Replace with commas, periods, or "and"/"or"
2. **AI vocabulary** — Flag and suggest replacements for:
   - "leverage" -> "use" or "build on"
   - "robust" -> "strong" or "reliable"
   - "comprehensive" -> "full" or "complete"
   - "streamline" -> "simplify" or "speed up"
   - "cutting-edge" -> "modern" or "new"
   - "utilize" -> "use"
   - "facilitate" -> "help" or "make easier"
   - "ecosystem" -> "system" or "setup" (unless literally about tech)
   - "synergy" -> (just delete it)
   - "paradigm" -> "approach" or "model"
   - "scalable" -> "grows with you" or "handles more"
   - "innovative" -> "new" or specific description of what's new
   - "world-class" -> specific claim or delete
   - "best-in-class" -> specific claim or delete
   - "holistic" -> "full" or "complete"
   - "empower" -> "help" or "let"
   - "transform" -> "change" or "improve"
   - "unlock" -> "open" or "get"
   - "drive" (as in "drive results") -> "get" or "deliver"
   - "seamless" -> "smooth" or "easy"
   - "elevate" -> "improve" or "raise"
3. **Passive voice** — Flag sentences where active voice would be clearer
4. **Sentence length** — Flag sentences over 25 words
5. **Jargon density** — Flag paragraphs with 3+ industry buzzwords

**What It Preserves:**
- Technical terms that are genuinely needed (API, CI/CD, DNS, etc.)
- Brand-specific language from `rl-slogan-system-v1.md`
- Code comments and documentation (lighter touch)
- Third-party content (quotes, testimonials)

**Voice Standard (from CLAUDE.md):**
- Direct, confident, accessible, action-oriented
- Team-first ("we" not "I")
- Veteran precision — say what you mean, no fluff
- Short sentences preferred
- Active voice preferred

---

## Agent Self-Optimization — `/relay optimize`

### Concept

Use the agents themselves to review and improve their own instructions
and workflows. Each agent audits its own prompt file, cross-references
with the others, and proposes upgrades.

### Trigger: `/relay optimize`

**Agents involved:** All BMAD lifecycle agents + default agents
**Output:** New versioned prompt files (e.g., `bmad-seo-v2.prompt.md`)
proposed as a PR for human review

### Workflow

1. **Self-audit** — Each agent reads its own prompt file and identifies:
   - Missing coverage areas
   - Outdated instructions
   - Conflicts with other agents
   - Missing cross-references to related agents
2. **Cross-audit** — Each agent reads adjacent agents' prompt files to find:
   - Overlap/duplication
   - Gaps between agents (things nobody covers)
   - Opportunities for better handoffs
3. **Propose** — Generate new versioned prompt files with improvements
4. **Human review** — All proposals go through PR review before becoming
   canonical (respects the versioning convention in `docs/blueprints/`)

### Rules

- Self-optimization NEVER auto-deploys — always a PR for human review
- New versions follow the `-v2`, `-v3` convention
- The human decides which proposals to accept
- Run `/relay optimize` quarterly or when adding new agents

---

## Default Agent Gate Order

When `/ship` runs the gate check, agents execute in this order to
ensure each layer validates before the next:

1. **Build Agent** — Code compiles, no errors (foundation)
2. **Security Agent** — No vulnerabilities, no secrets (safety)
3. **Brand Agent** — Colors, fonts, visual identity (standards)
4. **QA Agent** — Accessibility, responsive, Lighthouse (quality)
5. **Prose Agent** — Human language, no AI-isms (voice)
6. **Infra Agent** — Config valid, deployment ready (infrastructure)
7. **GitHub Agent** — Workflows valid, CI/CD clean (pipeline)

This order ensures code correctness first, then safety, then quality,
then language, then deployment readiness.

---

## Migration Plan

This system is **additive** — no existing triggers are removed or renamed.
The new features layer on top:

### Phase 1 (This PR)
- Add Mode + Domain documentation to `docs/agents.md`
- Add Prose Agent prompt file and default agent entry
- Add Ship Gate documentation and rules
- Add `/relay optimize` trigger documentation
- Update `CLAUDE.md` and `.github/copilot-instructions.md`

### Phase 2 (Future)
- Create prompt files for missing agents (`*analyst`, `*pm`, `*sm`)
- Run first `/relay optimize` cycle to improve existing prompt files
- Add domain-specific prompt files for each family (code, brand, etc.)

### Phase 3 (Current)
- Relay Forge Engine (Layer 11): Trend-aware build pipeline
- Relay Council (Layer 12): Multi-agent structured debate
- Deep Research (Layer 13): Free multi-source trend intelligence
- Business Sector Playbooks: 10 client verticals with pre-configured agent combos
- Free tool integrations: Perplexica, SearXNG, Serper, Brave, Tavily, Firecrawl

### Phase 4 (Future)
- Tooling: Shell aliases or Claude Code hooks for mode prefixes
- Analytics: Track which triggers are used most to optimize the system
- Cross-repo: Deploy to `relaylaunch-control-center`
- Perplexica n8n node for automated trend research in Relay Console
- CrewAI service-tier crews for multi-agent retainer delivery
- LangGraph Ship Gate graphs for executable workflow automation

---

## Quick Reference Card

```
MODE + DOMAIN = ACTION

Modes:          ? or check = review only
                ! or do    = make changes
                ~ or think = brainstorm

Domains:        code   = engineering
                brand  = design & identity
                growth = marketing & SEO
                ops    = infrastructure
                biz    = sales & deals
                plan   = strategy & roadmap
                qa     = testing & compliance

Ship Gate:      /ship         = push + PR with gate checks
                /ship --force = push without gate checks

Self-Optimize:  /relay optimize = agents improve their own prompts

Forge Engine:   /relay forge [client] = full 5-phase pipeline
                /deep-research        = multi-source trend intelligence
                /council              = multi-agent debate
                /council strategy     = business direction debate
                /council build        = technical architecture debate

Examples:       ?brand         check brand compliance
                !code          build a feature
                ~growth        brainstorm marketing ideas
                check security review security posture
                do brandfix    fix brand violations
                think deals    workshop deal strategy
                /relay forge spa-client  run full Forge for a client
                /council client          debate client delivery approach
                /deep-research           pull live trend intelligence
```

---

## Internal-Only Triggers (Founder Use)

These triggers are reserved for RelayLaunch internal use. They are not
client-facing and are not marketed on the website.

### Founder Finance Triggers

| Trigger | Mode | Domain | Agent | File |
|---------|------|--------|-------|------|
| `~biz-finance` or `think finance` | Think | biz | Founder Finance Navigator | `finance-founder-navigator.prompt.md` |
| `?biz-tools` or `check tools` | Check | biz | Small Biz Expense & Tools Coach | `finance-tools-coach.prompt.md` |
| `~plan-kpi` or `think kpi` | Think | plan | Founder KPI Explainer | `finance-kpi-explainer.prompt.md` |

### Meta-Role Overlay Triggers

| Trigger | Mode | Domain | Agent | File |
|---------|------|--------|-------|------|
| `~plan-ceo-review` | Think | plan | CEO / Vision Review | `relay-meta-roles.prompt.md` |
| `~plan-eng-review` | Think | code | Eng Manager / Staff Engineer Review | `relay-meta-roles.prompt.md` |
| `?code-review` or `/review` | Check | code | Pre-Ship Code Review | `relay-meta-roles.prompt.md` |
| `~retro` | Think | plan | Retrospective Facilitator | `relay-meta-roles.prompt.md` |

### Rules for Internal Triggers

- These triggers are for the founder only; other agents and repos must not
  call them automatically.
- We do not use them in client projects, proposals, or website copy.
- If you repurpose outputs for clients (blog posts, educational content),
  re-phrase and strip personal numbers before publishing.
- Finance agents always include a "not legal or tax advice" disclaimer.

---

## Acceptance Criteria

- [ ] All existing triggers continue to work unchanged
- [ ] Mode prefixes (?, !, ~) and word prefixes (check, do, think) both work
- [ ] Domain shortcuts route to the correct agent group
- [ ] Prose Agent activates on text/content changes as 7th default
- [ ] `/ship` gates push + PR behind explicit user command
- [ ] `/relay optimize` documented and available as a trigger
- [ ] `CLAUDE.md`, `docs/agents.md`, and `.github/copilot-instructions.md`
  all updated consistently

---

(c) RelayLaunch LLC. "The Relay Method" is a trademark of RelayLaunch LLC.
