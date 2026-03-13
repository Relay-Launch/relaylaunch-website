# RelayLaunch Service Playbook – Digital Infrastructure & Control Center (v1)

This document is an **internal service playbook** for RelayLaunch LLC.

It explains **how we deliver work** to clients from first contact through long‑term operation of the RelayLaunch Control Center and related infrastructure/automation services.

It is written for:
- Victor (founder) and any future team members.
- AI agents helping with delivery, documentation, or process design.

---

## 1. Service Overview

RelayLaunch offers **digital infrastructure and automation services** centered around the RelayLaunch Control Center:

1. **Discovery & Architecture** – clarify goals, audit current stack, and design the target system.
2. **Implementation** – build or improve infrastructure, automations, and the Control Center for the client.
3. **Operation & Optimization** – run and refine the system month‑over‑month using the Control Center.

The Control Center is both:
- A **product**: a multi‑tenant dashboard and control plane.
- A **delivery tool**: how we monitor our work, justify ROI, and manage change.

---

## 2. Standard Service Packages

We frame work in three main packages, each leveraging the same stack and docs.

### 2.1 Control Center Foundations (Project)

**Goal:** Stand up a production‑ready Control Center instance for one client tenant and connect it to a few high‑value workflows/agents.

**Typical scope:**
- Implement the Phase 1 architecture from `rl-control-center-options-v2.md`.
- Configure at least 2–3 key workflows and 1–2 AI agents.
- Set up the approvals + change request flow and metrics dashboard.

**Duration:** 4–6 weeks.

### 2.2 Automation Design & Build (Project)

**Goal:** Design and implement one or more automation/AI initiatives that plug into the client’s Control Center.

**Examples:**
- Lead‑capture and routing workflows (web → CRM → follow‑up sequences).
- AI agents for lead follow‑up, customer support, or internal knowledge retrieval.

**Duration:** 2–8 weeks depending on complexity.

### 2.3 Managed Digital Infrastructure & AIOps (Retainer)

**Goal:** Provide ongoing operation, monitoring, and improvement of the client’s infrastructure and automations.

**Includes:**
- Monthly change allowance (small/medium/new changes).
- Monitoring of Control Center metrics and alerts.
- Quarterly strategy/roadmap sessions.

**Cadence:** Monthly retainer with quarterly reviews.

---

## 3. Client Lifecycle

We follow a four‑stage lifecycle that mirrors the build framework and product docs:

1. **Discover** – fit check and initial architecture thinking.
2. **Design** – detailed architecture + Control Center plan.
3. **Build** – implementation using Builds 1–3.
4. **Run** – ongoing operations and optimization.

Each stage has inputs, outputs, and artifacts.

### 3.1 Stage 1 – Discover

**Objective:** Ensure the client is a good fit and clarify goals at a high level.

**Inputs:**
- Intro call notes.
- Any existing system diagrams or vendor lists.

**Key questions:**
- What are your most important processes (lead gen, onboarding, support, etc.)?
- Where are you currently using automations or AI?
- What’s breaking or slowing you down today?
- Who are the decision‑makers and day‑to‑day contacts?

**Activities:**
- 30–60 minute fit call.
- Light stack inventory (cloud providers, CRMs, automation tools).

**Outputs:**
- Short written summary: problems, opportunities, and whether RelayLaunch is a fit.
- Rough indication of which package(s) apply.

### 3.2 Stage 2 – Design (Sprint 0)

**Objective:** Turn discovery into a concrete plan and artifacts.

**Inputs:**
- Discovery summary.
- Access to basic systems (read‑only where possible).

**Activities:**
- Deep‑dive workshop (1–2 sessions) to map:
  - Systems and data flows.
  - Existing workflows and agents.
  - Desired metrics and KPIs (see `cc-metrics-kpis-v1.md`).
- Draft Control Center design:
  - Which workflows and agents to onboard first.
  - How the approvals/change process will look.
  - What metrics will show up in the first dashboard.

**Outputs:**
- One‑page architecture diagram.
- Initial tenant plan (Starter/Professional/Enterprise style bundle).
- High‑level project plan referencing `rl-control-center-build-framework-v2.md`.

---

## 4. Build Stages (Control Center Foundations)

We align the implementation with the three builds defined in the build framework doc.

### 4.1 Build 1 – Shell & Monorepo

**Goal:** Get the core repo and scaffolding running locally and in a dev environment.

**Activities:**
- Clone the `relaylaunch-control-center` monorepo skeleton.
- Ensure `apps/api`, `apps/web`, and `packages/*` match:
  - `rl-control-center-monorepo-setup-v1.md`
  - `rl-control-center-api-layout-v1.md`
  - `rl-control-center-web-layout-v1.md`
- Configure Supabase (or Postgres) and run initial migrations (`schema.prisma`).
- Implement stubbed `/api/tenants/:id/snapshot` returning static or seeded data.
- Verify the dashboard UI renders correctly for the demo tenant.

**Exit criteria:**
- Repo builds and runs with `pnpm dev`.
- Demo tenant dashboard loads using seeded data.
- Docs in `docs/` reflect actual implementation (v1 files).

### 4.2 Build 2 – Real Data & Read‑Only Control Center

**Goal:** Connect the client’s actual data/automations to the Control Center in a **read‑only** way.

**Activities:**
- Connect workflows (n8n, internal APIs) to send metrics/events into the Control Center DB.
- Implement snapshot generation according to `cc-metrics-kpis-v1.md`.
- Populate `ActivityItem` stream and ensure metrics cards show meaningful numbers.
- Expose `/api/tenants/:id` and `/api/tenants/:id/snapshot` with real data.

**Exit criteria:**
- For at least one client tenant, dashboard shows real metrics and recent activity.
- No write‑actions for end‑users yet (no change requests/approvals from UI).

### 4.3 Build 3 – Change Requests & Approvals

**Goal:** Enable safe modification of workflows and agents via approvals.

**Activities:**
- Implement `/api/approvals` and `/api/change-requests` endpoints per data spec.
- Add UI components for submitting change requests and resolving approvals.
- Connect approval decisions to underlying infrastructure/automation changes (n8n updates, config changes, etc.).
- Implement change budgeting logic for small/medium/new changes.

**Exit criteria:**
- Client can:
  - Submit change requests.
  - Approve or reject them.
  - See change usage reflected in the dashboard.
- All actions logged via the activity stream.

---

## 5. Operating Model (Retainer)

Once Builds 1–3 are live, the engagement shifts to an **Operate & Optimize** mode.

### 5.1 Monthly Rhythm

Each month:

1. **Review metrics**
   - Look at leads captured, automations run, hours saved, change usage.
   - Flag outliers and incidents (if implemented).

2. **Prioritize changes**
   - Use the change budget to decide which small/medium/new changes to tackle.
   - Capture them as `ChangeRequest` records and align with client stakeholders.

3. **Implement and validate**
   - Execute approved changes and validate impact.
   - Update assumptions in `estimatedMinutesSavedPerRun/Action` if needed.

4. **Communicate**
   - Send a short monthly summary (email or slide) using the Control Center screenshots.
   - Highlight wins and trade‑offs.

### 5.2 Quarterly Rhythm

Each quarter:

- Revisit the client’s business goals and metrics.
- Identify new automation/AI opportunities.
- Adjust plan tier and change budgets if needed.
- Refresh the roadmap and architecture diagram.

---

## 6. Roles & Responsibilities

In a minimal setup:

- **Victor (or Lead Consultant):**
  - Owns client relationship, architecture decisions, and final approvals.
  - Leads discovery, design, and quarterly reviews.
- **Implementation Engineer (you or an AI‑assisted role):**
  - Builds workflows, agents, and infrastructure changes.
  - Implements Control Center features using the docs.
- **AI Agents (Claude/Perplexity):**
  - Operate within `rl-control-center-agent-instructions-v1.md`.
  - Generate code, migrations, and documentation, but do not change v2 canonical specs without a new versioned doc.

---

## 7. Quality & Safety Guidelines

- **Version control:** All code work happens via PRs reviewed by a human.
- **Schema changes:**
  - Always update `rl-control-center-prisma-schema.md` (or create v2) before migrations.
  - Run migrations in dev/staging before production.
- **Secrets:**
  - Store API keys and DB URLs in environment variables, never in git.
- **Rollbacks:**
  - Keep previous versions of critical workflows and configurations.
  - For risky changes, design explicit rollback steps.

---

## 8. Using the Playbook with AI Agents

When engaging AI tools (Claude Code, etc.):

1. Provide this playbook plus:
   - `rl-control-center-options-v2.md`
   - `rl-control-center-data-model-v2.md`
   - `rl-control-center-prisma-schema.md`
   - `rl-control-center-api-layout-v1.md`
   - `rl-control-center-web-layout-v1.md`
   - `rl-control-center-agent-instructions-v1.md`
2. Clearly state the stage you are in (Discover, Design, Build 1–3, Run).
3. Ask for:
   - Specific artifacts (migrations, route handlers, Astro components).
   - Drafts of client‑facing materials (monthly reports, architecture notes).

---

## 9. Future Enhancements

As the business grows, this playbook can be extended with:

- Detailed runbooks for incident response and on‑call.
- More formal SLAs for response times and availability.
- Vertical‑specific playbooks (e.g., SaaS, agencies, healthcare).

For now, this v1 version provides enough structure to deliver consistent, high‑quality Control Center and infrastructure engagements while staying flexible.
