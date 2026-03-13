# RelayLaunch Control Center – Build Framework & Implementation Plan (v2)

This v2 document updates the original build framework to align with **final Phase 1 decisions**:
- Node.js + TypeScript everywhere
- Astro UI + API both running on Vercel (serverless) for v1
- Supabase Postgres as the initial database

It remains organized around three major builds.

---

## 1. Monorepo & Project Layout (Build 1)

### 1.1 Repository Structure

Create a GitHub repo `relaylaunch/control-center` with the following layout:

```text
control-center/
  apps/
    web/              # Astro front-end (Control Center UI)
    api/              # Node/TS API (REST/JSON, Vercel serverless)
  packages/
    core-models/      # Shared TypeScript types & validation
    client-sdk/       # Lightweight TS client for the web app
  infra/
    terraform/        # Reserved for future AWS migration (Phase 2+)
  docs/
    rl-control-center-options-v2.md
    rl-control-center-data-model-v2.md
    rl-control-center-build-framework-v2.md
```

### 1.2 Core Tech Choices (Phase 1)

- **Language:** TypeScript across API and front‑end.
- **Frameworks:**
  - Astro for UI (`apps/web`).
  - Minimal Node/Express or Fastify for API (`apps/api`).
- **Database:** Supabase Postgres.
- **Deployment:**
  - Both `apps/web` and `apps/api` deployed to Vercel.
  - API exposed as Vercel serverless functions.

### 1.3 Initial Tasks (Build 1)

1. Initialize the monorepo with PNPM or Yarn workspaces.
2. Add `packages/core-models` and paste in the TS interfaces from `rl-control-center-data-model-v2.md` (Tenant, User, Workflows, Agents, Metrics, Approvals, ChangeRequests, TenantSnapshot).
3. Configure ESLint, Prettier, and TypeScript project references so apps can import from `core-models`.
4. In `apps/api`:
   - Set up a minimal Node/Express (or Fastify) app.
   - Implement `GET /health` returning `{ status: 'ok' }`.
5. In `apps/web`:
   - Scaffold an Astro app with a placeholder login page and simple dashboard shell.

**Acceptance criteria (Build 1):**
- Repo builds locally with `pnpm build`.
- `GET /health` returns `200 OK` in local dev.
- Web app runs locally and shows a “RelayLaunch Control Center” shell.

---

## 2. Data Model, Supabase, & API Shell (Build 2)

### 2.1 Database Setup – Supabase

1. Create a new Supabase project for the Control Center.
2. Use either:
   - The Prisma schema document (separate), or
   - Raw SQL migrations
   to create tables matching `rl-control-center-data-model-v2.md`:

   - `tenants`
   - `users`
   - `workflow_templates`
   - `tenant_workflows`
   - `agent_templates`
   - `tenant_agents`
   - `tenant_daily_metrics`
   - `workflow_daily_metrics`
   - `approvals`
   - `change_requests`

3. Configure Supabase connection URL as an environment variable in Vercel for the API.

### 2.2 Seed Script

Add a Node script in `apps/api/scripts/seed.ts` to:
- Create one **RelayLaunch** tenant.
- Insert initial `workflow_templates` (Lead Capture, Invoice Automation, Email Sequences, Social Scheduling, Report Generation).
- Insert initial `agent_templates` (Social Content Agent, Invoice Chaser Agent, DevOps Engineer Agent, UX Designer Agent, Operations Summary Agent).
- Create a single admin `User` tied to RelayLaunch with role `admin`.

Run this script locally first, then via a one‑off `pnpm seed` on Vercel if desired.

### 2.3 API Endpoints (Read‑Only)

Implement in `apps/api` (Express/Fastify routes mapped to Vercel functions):

- `GET /me`
  - Returns a hard‑coded admin user for now (later tied to real auth).
- `GET /tenants/:id`
  - Fetch tenant by ID from Supabase.
- `GET /tenants/:id/snapshot`
  - Returns a `TenantSnapshot` object, populating:
    - `tenant` from `tenants`.
    - `overview.metrics` from stubbed metrics (temporary constants or basic aggregates).
    - `workflows` from joins of `tenant_workflows` and `workflow_templates`.
    - `agents` from `tenant_agents` and `agent_templates`.
    - `approvalsPending` as an empty array for now.

### 2.4 Web App Wiring

In `apps/web`:
- Implement a simple auth stub that sets a fixed `tenantId`.
- Call `/api/tenants/:id/snapshot` on page load.
- Render:
  - Overview metrics (leads, automations, hours saved) as cards.
  - Workflows list as a table (name, status, runs last 7 days).
  - Agents grid (name, category, status).

**Acceptance criteria (Build 2):**
- Control Center UI displays real data from Supabase for a single tenant.
- No write operations yet – everything is read‑only.

---

## 3. Metrics & First Live Tenant (Build 3)

### 3.1 n8n Tagging Convention

In n8n, standardize tags on workflows:
- `client:<tenant_slug>` – e.g., `client:relaylaunch`.
- `cc:<workflow_key>` – e.g., `cc:lead_capture_crm`.

This provides a stable mapping from n8n executions → `tenant_workflows`.

### 3.2 Metrics Ingestion Job (Node Script or n8n)

Create either:
- A small Node script in `apps/api/scripts/ingest-metrics.ts`, scheduled via GitHub Actions/cron; or
- An n8n workflow that runs daily.

Daily steps:
1. Call the n8n API for executions in the last 24 hours.
2. Group executions by `client:<tenant_slug>` and `cc:<workflow_key>`.
3. Look up corresponding `tenant_workflows` in Supabase.
4. For each `tenant_workflow`, compute:
   - `runsSuccess`
   - `runsFailed`
   - `hoursSaved` = `runsSuccess * minutes_per_run / 60` (from `metricsConfig` or workflow template).
5. Upsert into `workflow_daily_metrics` and aggregate into `tenant_daily_metrics`.

### 3.3 UI Enhancements

Update the Overview and Workflows pages to:
- Show charts or spark‑lines for automation runs and hours saved (last 7/30 days).
- Surface “Top workflows by hours saved” on the Overview.
- Display error badges for workflows with recent failures.

### 3.4 Approvals & Requests (Skeleton, Read‑Only)

- Confirm DB tables `approvals` and `change_requests` exist.
- Implement:
  - `GET /tenants/:id/approvals?status=pending`
  - `GET /tenants/:id/change-requests`
- Build UI pages that:
  - List pending approvals.
  - List change requests.

During Build 3 keep POST/PATCH actions disabled or hidden until the flows are well‑defined.

**Acceptance criteria (Build 3):**
- At least one real n8n workflow for RelayLaunch operations is tagged and tracked.
- Daily metrics ingestion runs (manually or scheduled) and populates `tenant_daily_metrics` and `workflow_daily_metrics` in Supabase.
- The dashboard shows **real, time‑based metrics** for that tenant.

---

## 4. Phase 2 – AWS Migration Placeholder

Do **not** start this until:
- The Vercel/Supabase stack is stable.
- You have at least one active client using the Control Center.

At that point, follow the high‑level migration steps in `rl-control-center-options-v2.md` and move the API + DB to AWS while keeping the Astro UI on Vercel.

---

## 5. Working Style & Quality Gates

- Treat each build as a mini‑project with a clear demo.
- Maintain `/docs/changelog.md` capturing:
  - Date, build number, summary of changes.
- Before adding any new feature:
  - Confirm which **client plan** (Launch/Run/Scale) it supports and how it will appear in the UI.
- Keep the Control Center aligned with brand standards from your main RelayLaunch Brand Identity guide.

These practices keep v1 focused, shippable, and easy to reason about for any human or AI collaborator.