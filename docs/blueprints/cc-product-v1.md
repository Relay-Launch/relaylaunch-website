# RelayLaunch Control Center – Product One‑Pager (v1)

This document summarizes the **product, positioning, and value proposition** for the RelayLaunch Control Center. It is intended for use in decks, sales conversations, the marketing site, and as context for collaborators.

---

## 1. Elevator Pitch

RelayLaunch Control Center is a **multi‑tenant dashboard and control plane** for client automations and AI agents.

It gives growing B2B companies a single place to:

- See what their automations and AI agents are doing.
- Understand the impact on leads, revenue, and operational efficiency.
- Safely request and approve changes to their digital infrastructure.

Built and operated by **RelayLaunch LLC**, the Control Center combines **a product** (the dashboard) with **expert digital infrastructure consulting** behind the scenes.

---

## 2. Target Customers

Primary target segments for the first 12–24 months:

1. **B2B SaaS companies (5–50 engineers)**
   - Already running on modern cloud stacks (Vercel, AWS, Supabase, etc.).
   - Experiencing rapid growth in automations (n8n, Zapier, custom workflows).
   - Need a clearer picture of "what’s running where" and a safer way to manage changes.

2. **Digital agencies / service firms**
   - Building automations and AI agents for their own clients.
   - Want a branded or white‑labeled control center to show value and manage change requests.

3. **High‑margin professional services (legal, consulting, boutique finance)**
   - Undergoing digital transformation.
   - Don’t want to build an internal DevOps/SRE team but still need reliability and governance.

See `relaylaunch-market-landscape-v1.md` for market size and growth data behind these segments.

---

## 3. Problem

As companies adopt more automations and AI agents:

- **No single source of truth.** Workflows, bots, and integrations live across tools (n8n, Zapier, custom lambdas, CRMs), making it hard to see the full picture.
- **Opaque value.** Leadership can’t easily answer: "How many leads are we capturing from automations?" or "How many hours is this saving us each month?"
- **Risky changes.** Requests like "connect a new lead source" or "launch an AI follow‑up agent" turn into ad‑hoc Slack threads and Jira tickets with unclear approvals.
- **Expensive DevOps teams.** Hiring full‑time SRE/DevOps staff is overkill for many SMB/mid‑market companies, but they still need reliability and governance.

---

## 4. Solution

RelayLaunch Control Center provides:

1. **Unified dashboard per tenant**
   - High‑level metrics (leads captured, automations run, estimated hours saved).
   - Status of workflows and AI agents (active/paused/error).
   - Recent activity stream (workflow runs, agent actions, approvals, change requests).

2. **Change request & approval workflow**
   - Simple UI for stakeholders to request changes:
     - Small tweaks (copy, timing, routing).
     - Medium changes (new workflow branch, new data source).
     - New builds (entirely new automation or agent).
   - Clearly defined approval types (workflow activation, agent deployment, config change).
   - Track status from request to completion and see usage against the monthly/quarterly change budget.

3. **Lightweight AIOps for SMB/mid‑market**
   - Opinionated metrics and alerts instead of a sprawling observability tool.
   - Integration with n8n and other automation platforms for event ingestion.
   - Designed for Phase 1 on Vercel + Supabase, with a clear upgrade path to AWS.

The product is deliberately **opinionated and narrow** to keep implementation fast while providing meaningful governance and insight.

---

## 5. Key Features (Phase 1)

### 5.1 Tenant Dashboard

- Tenant overview with:
  - Plan, status (ACTIVE/TRIAL/SUSPENDED), key dates.
  - Last 30‑day metrics for leads, automations, and estimated hours saved.
  - Change budget usage (small/medium/new changes).
- Lists of:
  - Active workflows (with last run and health status).
  - Active AI agents (with category and status).
  - Pending approvals.

### 5.2 Approvals & Change Requests

- Request types:
  - Workflow activation or deactivation.
  - AI agent deployment or pause.
  - Configuration change (e.g., routing, thresholds).
- Change request categories:
  - Small, Medium, New (for quarterly budgeting).
- Status tracking from **PENDING → IN_PROGRESS → COMPLETED/REJECTED**.

### 5.3 Integrations & Data Ingestion

- n8n workflows emit metrics and events into the Control Center API.
- Future phases can extend to other tools (Zapier, Make, custom webhook emitters).

---

## 6. Architecture Snapshot (Phase 1)

- **Front‑end:** Astro 4 + React islands (dashboard components) on Vercel.
- **API:** Node.js + TypeScript + Express on Vercel serverless functions.
- **Database:** Supabase Postgres with Prisma for data access.
- **Automations:** n8n (hosted or self‑hosted), sending events and metrics to the API.

This stack is documented in:

- `rl-control-center-options-v2.md`
- `rl-control-center-api-layout-v1.md`
- `rl-control-center-web-layout-v1.md`
- `rl-control-center-prisma-schema.md`

---

## 7. Pricing & Packaging (Draft)

**Note:** Exact numbers are intentionally left for later; this section defines structure.

Suggested tiers for SMB/mid‑market:

1. **Starter**
   - 1 tenant (single business unit).
   - Fixed number of workflows and agents.
   - Limited monthly change budget (e.g., 6 small, 1 medium per month).
   - Email support.

2. **Professional**
   - Multiple tenants (e.g., multi‑brand or agency with several clients).
   - Higher automation/agent limits.
   - Larger change budget.
   - Slack support and quarterly infrastructure review.

3. **Enterprise / Custom**
   - Custom SLAs.
   - Extended monitoring and incident response.
   - Deeper integration work and AWS migration planning.

Each tier bundles **access to the Control Center** + **consulting time** for design, implementation, and continuous improvement.

---

## 8. Onboarding Flow (Client Journey)

1. **Discovery & Fit Check**
   - Short call to understand current stack, automations, and pain points.
   - Determine if Control Center + consulting is appropriate.

2. **Audit & Design (Sprint 0)**
   - Catalog existing workflows, agents, and data sources.
   - Define priority metrics and change categories.
   - Produce a small diagram + change budget proposal.

3. **Implementation (Build 1–3)**
   - Build 1: Baseline dashboard and snapshot driven by static or stubbed data.
   - Build 2: Wire Supabase and n8n for real metrics.
   - Build 3: Activate approvals and change requests, plus first live tenant.

4. **Operate & Optimize**
   - Monthly or quarterly reviews.
   - Adjust limits and metrics, add new automations.
   - Iterate on reporting and dashboards as needs evolve.

---

## 9. Why RelayLaunch (Differentiation)

- **Infrastructure‑first mindset:** Built by an infrastructure engineer with hands‑on experience in AWS, Terraform, and cloud‑native architectures.
- **SMB‑friendly AIOps:** Brings AIOps‑style visibility and governance to companies that can’t (or don’t want to) run full observability platforms.
- **Productized consulting:** Clear phases and deliverables instead of open‑ended hourly engagements.
- **Future‑proofing:** Phase 1 on Vercel + Supabase; Phase 2 migration path to AWS and more advanced observability, using the same domain model.

---

## 10. How to Use This One‑Pager

- As the **top‑level description** in the GitHub README and in internal docs.
- As material for:
  - A pitch deck (Problem, Solution, Product, Architecture, Pricing slides).
  - The "Product" or "Solutions" section of the RelayLaunch marketing site.
  - Context for AI agents (along with `rl-control-center-agent-instructions-v1.md`) so they understand business intent, not just code.

For deeper market and strategy context, pair this with `relaylaunch-market-landscape-v1.md`.
