# RelayLaunch Control Center – AI Agent Instructions (v1)

This document tells **AI agents (e.g., Claude, Perplexity)** exactly how to work on the RelayLaunch Control Center repo without breaking core assumptions.

Agents should treat this as the **system guide** when editing or generating code/content for the project.

---

## 1. Project Context

- Project: **RelayLaunch Control Center** – a multi‑tenant dashboard for client automations and AI agents.
- Phase: **Phase 1 (Vercel stack)**.
- Owner: Victor David Medina, RelayLaunch LLC.

### 1.1 Phase 1 Technology Decisions

Agents must assume the following unless a newer document explicitly changes them:

- **Language:** Node.js + TypeScript.
- **API hosting:** Vercel serverless functions (`apps/api`).
- **Front‑end:** Astro app on Vercel (`apps/web`).
- **Database:** Supabase Postgres accessed via Prisma.

Reference docs:
- `rl-control-center-options-v2.md` – tech decisions and future AWS plan.
- `rl-control-center-data-model-v2.md` – entities and API shapes.
- `rl-control-center-build-framework-v2.md` – build phases and acceptance criteria.
- `rl-control-center-prisma-schema.md` – `schema.prisma` mapping.
- `rl-control-center-api-layout-v1.md` – API project layout and starter patterns.

Agents must **not** change these decisions unless a human requests a new version of the options document.

---

## 2. Repository Layout (Expected)

Agents should assume the monorepo structure described in `build-framework-v2` and `api-layout-v1`:

```text
control-center/
  apps/
    web/                 # Astro front-end
    api/                 # Node/TS API on Vercel
  packages/
    core-models/         # Shared TS interfaces
    client-sdk/          # (optional) HTTP client helpers for web app
  infra/
    terraform/           # Reserved for future AWS migration
  docs/
    rl-control-center-options-v2.md
    rl-control-center-data-model-v2.md
    rl-control-center-build-framework-v2.md
    rl-control-center-prisma-schema.md
    rl-control-center-api-layout-v1.md
```

When writing file paths, follow this layout unless the repo shows otherwise.

---

## 3. Rules for Agents

### 3.1 Do not change canonical specs casually

- Treat the following as **source of truth**:
  - Data shapes and endpoints: `rl-control-center-data-model-v2.md`.
  - Prisma models/enums: `rl-control-center-prisma-schema.md`.
  - Phase 1 architecture: `rl-control-center-options-v2.md`.
- If you believe a change is needed, propose it in a **new versioned doc** (e.g., `rl-control-center-data-model-v3.md`) rather than silently editing v2.

### 3.2 Maintain compatibility

- Any new route, DB field, or feature must:
  - **Not break** existing interfaces used by `apps/web`.
  - Maintain backward compatibility where possible or be clearly documented as breaking.
- When altering Prisma models:
  - Update `schema.prisma`.
  - Generate a migration name that explains intent (e.g., `add_approvals_comment_field`).

### 3.3 Respect build phases

- Phase 1 is defined as three builds:
  - **Build 1:** Monorepo + basic API & UI shell.
  - **Build 2:** Real data from Supabase + read‑only snapshot API.
  - **Build 3:** Metrics ingestion from n8n + first live tenant.
- Before suggesting work beyond the current build, confirm that previous build acceptance criteria are met.

---

## 4. How to Generate or Edit Code Safely

### 4.1 When adding API endpoints

1. Check `rl-control-center-data-model-v2.md` for the desired entity and expected payload.
2. Add or update:
   - Prisma calls in `apps/api` using the models from `schema.prisma`.
   - Route handler modules under `apps/api/src/routes/**`.
3. Keep responses JSON and typed using the shared `core-models` interfaces where possible.
4. Ensure error handling returns structured `{ error: string }` objects with appropriate HTTP status codes.

### 4.2 When modifying the Prisma schema

1. Confirm the change belongs to the current build and plan.
2. Edit `prisma/schema.prisma` in line with `rl-control-center-prisma-schema.md`.
3. Generate a migration (locally) and avoid destructive operations unless explicitly requested.
4. Update any TypeScript types that reference the changed model.

### 4.3 When updating the front‑end

1. Read the snapshot structure in `rl-control-center-data-model-v2.md`.
2. Consume the `/api/tenants/:id/snapshot` response in Astro/React components.
3. Avoid introducing tight coupling to Vercel-specific APIs in the front‑end; only the API layer should know about serverless.

---

## 5. What Not to Do

Agents should **not**:

- Change the **Phase 1 hosting choice** (Vercel API + Supabase) unless creating a new v3+ options document requested by Victor.
- Introduce additional runtime languages (no Python, Go, etc.) without explicit sign‑off.
- Modify brand language, pricing, or tier names from the core RelayLaunch documents when working inside this repo; those live elsewhere.
- Create hidden magic or undocumented behavior in routes; everything should be discoverable from the docs and type definitions.

---

## 6. Logging, Secrets, and Security

When generating code that touches logs or secrets:

- Never log entire environment objects or full JWTs.
- Do not print database URLs, API keys, or client tokens.
- Use structured logs at an appropriate level (`info`, `warn`, `error`).
- Assume that Phase 1 uses Supabase’s default security, but design so that moving to AWS RDS later does **not** require conceptual changes.

---

## 7. When in Doubt

If an agent is unsure about a change:

1. Prefer **proposing** a new `.md` design document under `docs/` that explains:
   - The problem.
   - The proposed change.
   - Impact on existing models/routes.
2. Wait for human confirmation before editing schema or critical routes.

This keeps the Control Center coherent as multiple agents and humans work on it over time.
