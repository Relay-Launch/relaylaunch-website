# RelayLaunch Control Center

A multi-tenant control center for client automations and AI agents, built and operated by **RelayLaunch LLC**.

This README is the entry point for humans and AI agents working on the `relaylaunch-control-center` monorepo.

---

## 1. Project Overview

RelayLaunch Control Center provides:

- A **single dashboard** for each client (tenant) that surfaces key metrics about automations, lead capture, and AI agents.
- A **change/approval workflow** so client stakeholders can request, approve, and track infrastructure and automation changes.
- An opinionated **Phase 1 stack** that is fast to ship on Vercel + Supabase, with a future path to AWS.

The control center underpins RelayLaunch's "Digital Infrastructure Consultancy" offerings and is designed for SMB and mid-market B2B clients.

For background on product and strategy, see:

- `docs/relaylaunch-market-landscape-v1.md`
- `docs/rl-control-center-options-v2.md`
- `docs/rl-control-center-build-framework-v2.md`

---

## 2. Architecture (Phase 1)

Phase 1 uses the following stack:

- **API:** Node.js + TypeScript, Express, Prisma, deployed as serverless functions on **Vercel**.
- **Database:** **Supabase Postgres** accessed via Prisma.
- **Web app:** **Astro** (SSR) with **React islands** for interactive dashboard components, deployed on Vercel.
- **Automations & integrations:** **n8n** and other external tools, feeding metrics and events into the Control Center API.

Future phases introduce an AWS path (RDS, Lambda/ECS, API Gateway, etc.) without changing the core domain model.

See:

- `docs/rl-control-center-options-v2.md`
- `docs/rl-control-center-prisma-schema.md`

---

## 3. Repository Structure

```text
control-center/
  apps/
    api/           # Node/TS API on Vercel
    web/           # Astro + React dashboard on Vercel
  packages/
    core-models/   # Shared TypeScript domain models
    client-sdk/    # Optional typed HTTP client for external consumers
  infra/
    terraform/     # Reserved for future AWS migration
  docs/            # Architecture, data model, and blueprint docs
  .gitignore
  package.json
  pnpm-workspace.yaml
  tsconfig.base.json
  turbo.json
  README.md
```

See `docs/rl-control-center-monorepo-setup-v1.md` for exact file contents and configuration.

---

## 4. Key Documents

All core design and coordination docs live under `docs/`:

- **Technology & architecture**
  - `rl-control-center-options-v2.md` – technology options and Phase 1–2 decisions.
  - `rl-control-center-monorepo-setup-v1.md` – monorepo tooling and package setup.

- **Data & API contracts**
  - `rl-control-center-data-model-v2.md` – canonical data model and API shapes.
  - `rl-control-center-prisma-schema-v1.md` or `rl-control-center-prisma-schema.md` – Prisma `schema.prisma` mapping.

- **Implementation blueprints**
  - `rl-control-center-build-framework-v2.md` – 3-build plan and acceptance criteria.
  - `rl-control-center-api-layout-v1.md` – API folder layout & starter routes.
  - `rl-control-center-web-layout-v1.md` – Astro web layout & component plan.

- **Coordination & strategy**
  - `rl-control-center-agent-instructions-v1.md` – how AI agents should work in this repo.
  - `relaylaunch-market-landscape-v1.md` – market data for strategy & sales.

AI agents **must read** `rl-control-center-agent-instructions-v1.md` before making changes.

---

## 5. Getting Started (Developers)

### 5.1 Prerequisites

- Node.js 20+
- pnpm 8+
- Git
- Access to a Supabase (or Postgres) instance for development.

### 5.2 Install dependencies

From the repo root:

```bash
pnpm install
```

### 5.3 Configure environment variables

Create `apps/api/.env` based on `.env.example`:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/control_center
NODE_ENV=development
```

Create `apps/web/.env` based on `.env.example`:

```env
PUBLIC_API_URL=http://localhost:3000/api
```

### 5.4 Set up the database

From `apps/api`:

```bash
pnpm prisma generate
pnpm prisma migrate dev --name init_control_center
# Optional: seed script to create a tenant + admin user
```

### 5.5 Run the dev environment

From the repo root:

```bash
pnpm dev
```

This runs both API and web apps via Turbo. Visit:

- API: `http://localhost:3000/api/health`
- Web: `http://localhost:4321/`

---

## 6. Application Structure

### 6.1 API (`apps/api`)

- `src/env.ts` – central environment variable loading/validation.
- `src/server.ts` – Express app creation and middleware.
- `api/index.ts` – Vercel serverless entry adapting the Express app.
- `src/routes/` – route handlers, grouped by feature (e.g., `tenants`, `me`).
- `prisma/schema.prisma` – Prisma schema (mirrors the data model docs).

Key routes (Phase 1):

- `GET /api/health` – health check.
- `GET /api/me` – returns the current (stubbed) admin user.
- `GET /api/tenants/:id` – tenant details.
- `GET /api/tenants/:id/snapshot` – read-only dashboard snapshot.

See `docs/rl-control-center-api-layout-v1.md` for details.

### 6.2 Web (`apps/web`)

- `astro.config.mjs` – Astro config with React + Vercel adapter.
- `src/pages/dashboard/[tenantId].astro` – main dashboard route.
- `src/components/layout/*` – Header, Sidebar, etc.
- `src/components/dashboard/*` – SnapshotOverview, WorkflowList, AgentList, ApprovalList.
- `src/components/ui/*` – Card, Button, Badge, etc.
- `src/lib/api-client.ts` – API client wrapper.
- `src/lib/types.ts` – client-side types mirroring shared models.
- `src/styles/global.css` – dark-mode design system.

See `docs/rl-control-center-web-layout-v1.md` for details.

---

## 7. Scripts

Common commands from the repo root:

```bash
pnpm dev         # Run all apps in dev mode
pnpm build       # Build all apps/packages
pnpm lint        # Lint all apps/packages
pnpm typecheck   # Type-check all TypeScript projects
pnpm test        # (future) Run tests
```

Each app/package also exposes its own scripts (see their `package.json` files).

---

## 8. Working with AI Agents

AI agents (Claude, Perplexity, etc.) must:

1. Read `docs/rl-control-center-agent-instructions-v1.md`.
2. Treat `docs/rl-control-center-data-model-v2.md` and `docs/rl-control-center-prisma-schema.md` as **canonical** for data shapes.
3. Propose new versioned docs (`*-v3.md`) instead of editing v2 directly when changes to architecture or data contracts are required.
4. Summarize planned file changes before editing, when possible.

---

## 9. Contributing

For human collaborators:

1. Open an issue describing the change or enhancement.
2. If the change impacts architecture or data model, start by editing/adding a doc under `docs/`.
3. Submit a PR linked to the relevant docs.
4. Ensure `pnpm lint` and `pnpm typecheck` pass.

For AI-generated changes, ensure a human reviews diffs before merging.

---

## 10. License

This project is currently **proprietary** to RelayLaunch LLC. Do not redistribute or open-source without explicit approval.
