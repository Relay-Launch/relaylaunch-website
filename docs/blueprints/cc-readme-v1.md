# RelayLaunch Control Center

**The operational backbone behind RelayLaunch client delivery.**

A multi-tenant control center for client automations and AI agents, built and operated by **RelayLaunch LLC**.

This README is the entry point for humans and AI agents working on the `relaylaunch-control-center` monorepo.

---

## What It Does

RelayLaunch Control Center gives each client a single dashboard that surfaces:

- **Automation health** — what workflows and AI agents are running, their status, and recent activity
- **Business impact** — leads captured, automations run, estimated hours saved
- **Change governance** — a structured request-and-approval workflow for infrastructure changes

The Control Center underpins RelayLaunch's digital infrastructure consultancy and is built for SMB and mid-market B2B clients.

For product strategy and market context, see:

- `docs/cc-product-v1.md` — product one-pager
- `docs/relaylaunch-market-landscape-v1.md` — market research

---

## Architecture (Phase 1)

| Layer | Technology |
|-------|-----------|
| **API** | Node.js + TypeScript, Express, Prisma on **Vercel** serverless |
| **Database** | **Supabase Postgres** via Prisma |
| **Web app** | **Astro** (SSR) + **React** islands on Vercel |
| **Automations** | **n8n** and external tools feeding metrics into the API |

Future phases introduce an AWS migration path (RDS, Lambda/ECS, API Gateway) without changing the core domain model.

See:

- `docs/rl-control-center-options-v2.md` — tech stack decisions
- `docs/rl-control-center-prisma-schema.md` — database schema

---

## Repository Structure

```
control-center/
  apps/
    api/           # Node/TS API on Vercel
    web/           # Astro + React dashboard on Vercel
  packages/
    core-models/   # Shared TypeScript domain models
    client-sdk/    # Typed HTTP client for external consumers
  infra/
    terraform/     # Reserved for AWS migration
  docs/            # Architecture, data model, blueprint docs
  .gitignore
  package.json
  pnpm-workspace.yaml
  tsconfig.base.json
  turbo.json
  README.md
```

See `docs/rl-control-center-monorepo-setup-v1.md` for full configuration.

---

## Key Documents

All design and coordination docs live under `docs/`:

**Technology and architecture:**
- `rl-control-center-options-v2.md` — technology decisions, Phase 1-2
- `rl-control-center-monorepo-setup-v1.md` — monorepo tooling, package setup

**Data and API contracts:**
- `rl-control-center-data-model-v2.md` — canonical data model, API shapes
- `rl-control-center-prisma-schema.md` — Prisma schema mapping

**Implementation blueprints:**
- `rl-control-center-build-framework-v2.md` — 3-build plan, acceptance criteria
- `rl-control-center-api-layout-v1.md` — API folder layout, starter routes
- `rl-control-center-web-layout-v1.md` — Astro web layout, component plan

**Coordination:**
- `rl-control-center-agent-instructions-v1.md` — AI agent rules for this repo
- `relaylaunch-market-landscape-v1.md` — market data for strategy and sales

AI agents **must read** `rl-control-center-agent-instructions-v1.md` before making changes.

---

## Getting Started

### Prerequisites

- Node.js 20+
- pnpm 8+
- Git
- Supabase (or Postgres) instance for development

### Setup

```bash
# Install dependencies
pnpm install

# Configure environment (apps/api/.env from .env.example)
DATABASE_URL=postgresql://user:password@localhost:5432/control_center
NODE_ENV=development

# Configure web (apps/web/.env from .env.example)
PUBLIC_API_URL=http://localhost:3000/api

# Database setup (from apps/api)
pnpm prisma generate
pnpm prisma migrate dev --name init_control_center

# Run everything
pnpm dev
```

**API:** `http://localhost:3000/api/health`
**Web:** `http://localhost:4321/`

---

## Application Structure

### API (`apps/api`)

| File | Purpose |
|------|---------|
| `src/env.ts` | Environment variable loading and validation |
| `src/server.ts` | Express app creation and middleware |
| `api/index.ts` | Vercel serverless entry point |
| `src/routes/` | Route handlers grouped by feature |
| `prisma/schema.prisma` | Database schema (mirrors data model docs) |

**Key routes (Phase 1):**
- `GET /api/health` — health check
- `GET /api/me` — current admin user
- `GET /api/tenants/:id` — tenant details
- `GET /api/tenants/:id/snapshot` — read-only dashboard snapshot

### Web (`apps/web`)

| File | Purpose |
|------|---------|
| `src/pages/dashboard/[tenantId].astro` | Main dashboard route |
| `src/components/layout/*` | Header, Sidebar |
| `src/components/dashboard/*` | SnapshotOverview, WorkflowList, AgentList, ApprovalList |
| `src/components/ui/*` | Card, Button, Badge |
| `src/lib/api-client.ts` | API client wrapper |
| `src/styles/global.css` | Dark-mode design system |

---

## Scripts

```bash
pnpm dev         # Run all apps in dev mode
pnpm build       # Build all apps and packages
pnpm lint        # Lint all apps and packages
pnpm typecheck   # Type-check all TypeScript
pnpm test        # Run tests (future)
```

---

## Working with AI Agents

AI agents working in this repo must:

1. Read `docs/rl-control-center-agent-instructions-v1.md` first
2. Treat `docs/rl-control-center-data-model-v2.md` and the Prisma schema as canonical for data shapes
3. Propose new versioned docs (`*-v3.md`) instead of editing v2 directly
4. Summarize planned file changes before editing

This repo participates in **The Relay Method** — see `docs/agents.md` in the website repo for the full agent registry.

---

## Contributing

1. Open an issue describing the change
2. If the change impacts architecture or data model, start with a doc under `docs/`
3. Submit a PR linked to relevant docs
4. Ensure `pnpm lint` and `pnpm typecheck` pass

For AI-generated changes, a human reviews all diffs before merging.

---

## License

Proprietary to RelayLaunch LLC. Do not redistribute without explicit approval.

---

**RelayLaunch LLC** | Built by Victor David Medina, USMC Sergeant (E-5) | Watertown, MA
