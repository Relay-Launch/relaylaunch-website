# RelayLaunch Console

**Ops on Autopilot. You on Strategy.**

A multi-tenant control center for digital operations, automations, and AI agents. Built for SMB and mid-market teams that need visibility, governance, and metrics across all their infrastructure and workflows.  
---

## What is this?

RelayLaunch Control Center is a **production-ready SaaS product** that turns scattered AI experiments and automations into a governed, measurable operations platform. Think:

- Single dashboard showing leads captured, automations run, hours saved, and budget usage  
- Approval workflow for every change before it goes live  
- Inventory of all workflows and AI agents with health status  
- Activity stream logging every significant action  
- Snapshot reports you can share with stakeholders

The repo implements a **turborepo monorepo** with:

- **API** (Node \+ Express \+ Prisma \+ Vercel)  
- **Web UI** (Astro \+ React \+ Vercel)  
- **Shared packages** (TypeScript models \+ optional client SDK)  
- **Infrastructure as code** (Terraform stubs for AWS/Vercel)  
- **Complete documentation** (7 internal specs covering data model, service playbook, agent instructions, and market landscape)

---

## Why this exists

Small and mid-sized businesses are racing to adopt AI and automation, but most end up with:

- Shadow scripts and bots no one fully owns  
- Ad-hoc experiments living in notebooks or Zapier  
- No single place that shows which automations are live, what they touch, and what value they create  
- Risk of breaking customer-facing flows with unreviewed changes

RelayLaunch Control Center solves this by providing the same operational discipline that large enterprises have, packaged for teams of 5 to 50\.

**Market context:**

- Global digital consulting services: \~$500B in 2025, heading to \~$1.2T by 2033 (12% CAGR)  
- Cloud managed services: $130–160B mid-2020s, growing to $300–480B early 2030s (11–15% CAGR)  
- AIOps market: high-teens to low-20s CAGR into the 2030s

See `docs/relaylaunch-market-landscape-v1.md` for full data and citations.

---

## Quick start

### Prerequisites

- Node.js 18+ and pnpm 8+  
- PostgreSQL 14+ (local or hosted)  
- Vercel account (for deployment)  
- (Optional) AWS account (for Terraform infra)

### Local development

1. **Clone and install:**  
     
   git clone git@github.com:\<your-org\>/relaylaunch-control-center.git  
     
   cd relaylaunch-control-center  
     
   pnpm install  
     
2. **Set up the database:**  
     
   cd apps/api  
     
   cp .env.example .env  
     
   \# Edit .env with your DATABASE\_URL  
     
   pnpm prisma generate  
     
   pnpm prisma migrate dev \--name init\_control\_center  
     
   cd ../..  
     
3. **Configure the web app:**  
     
   cd apps/web  
     
   cp .env.example .env  
     
   \# Set PUBLIC\_API\_URL=http://localhost:3000/api  
     
   cd ../..  
     
4. **Start all services:**  
     
   pnpm dev  
     
   Turbo will start:  
     
   - API server on `http://localhost:3000`  
   - Web UI on `http://localhost:4321`

   

5. **Seed demo data (optional):**  
     
   cd apps/api  
     
   pnpm prisma db seed

---

## Repository structure

relaylaunch-control-center/

├── apps/

│   ├── api/              \# Express \+ Prisma API (Vercel Functions)

│   │   ├── src/

│   │   │   ├── routes/   \# /tenants, /me, /health endpoints

│   │   │   ├── env.ts    \# Environment validation

│   │   │   └── server.ts \# Express app

│   │   ├── api/index.ts  \# Vercel entry point

│   │   ├── prisma/

│   │   │   └── schema.prisma

│   │   ├── package.json

│   │   ├── tsconfig.json

│   │   └── vercel.json

│   │

│   └── web/              \# Astro \+ React UI (Vercel)

│       ├── src/

│       │   ├── pages/    \# Astro pages (index, dashboard/\[tenantId\])

│       │   ├── components/

│       │   │   ├── layout/    \# Header, Sidebar, Footer

│       │   │   ├── dashboard/ \# SnapshotOverview, WorkflowList, AgentList

│       │   │   └── ui/        \# Card, Button, Badge primitives

│       │   ├── lib/

│       │   │   ├── api-client.ts  \# Fetch wrapper

│       │   │   └── types.ts       \# TypeScript interfaces

│       │   └── styles/

│       │       └── global.css

│       ├── astro.config.mjs

│       ├── package.json

│       ├── tsconfig.json

│       └── vercel.json

│

├── packages/

│   ├── core-models/      \# Shared TypeScript types and interfaces

│   └── client-sdk/       \# (Optional) typed SDK for API consumers

│

├── infra/

│   └── terraform/        \# AWS resources (RDS, S3, CloudWatch)

│

├── docs/                 \# Internal specs and blueprints

│   ├── rl-control-center-options-v2.md

│   ├── rl-control-center-data-model-v2.md

│   ├── rl-control-center-build-framework-v2.md

│   ├── rl-control-center-prisma-schema.md

│   ├── rl-control-center-api-layout-v1.md

│   ├── rl-control-center-web-layout-v1.md

│   ├── rl-control-center-monorepo-setup-v1.md

│   ├── rl-control-center-agent-instructions-v1.md

│   └── relaylaunch-market-landscape-v1.md

│

├── .gitignore

├── package.json          \# Root package with Turbo scripts

├── pnpm-workspace.yaml   \# Workspace config

├── tsconfig.base.json    \# Shared TypeScript config

├── turbo.json            \# Turbo pipeline

└── README.md             \# You are here

---

## Key features

### 1\. Tenant Dashboards

Each client gets a dedicated dashboard showing:

- Leads captured (automated vs manual)  
- Automations run this month  
- Hours saved (calculated from workflow executions)  
- Change budget usage

### 2\. Approval Workflow

Before any workflow or agent change goes live:

- Submitter creates a change request with description and estimated impact  
- Approver reviews and approves/rejects  
- System logs approval and updates usage against budget  
- Change shows in activity stream

### 3\. Inventory Management

Centralized view of:

- All workflows (active/paused/failed state)  
- All AI agents (category, last run, error count)  
- Infrastructure components (APIs, databases, third-party services)

### 4\. Activity Stream

Real-time log of:

- Workflow executions  
- Agent actions  
- Configuration changes  
- User logins and permissions changes

### 5\. Snapshot Reports

Monthly or on-demand reports showing:

- KPI trends (leads, conversions, automations, hours saved)  
- Top-performing workflows  
- Budget consumption  
- Recommendations for next quarter

---

## Technology stack

| Layer | Technology | Why |
| :---- | :---- | :---- |
| **API** | Node.js \+ Express \+ Prisma | Fast iteration, type-safe DB access, Vercel-ready |
| **Database** | PostgreSQL | Relational data (tenants, workflows, agents, approvals) |
| **Web UI** | Astro \+ React | Server-first rendering, React for interactive components |
| **Deployment** | Vercel (app) \+ AWS (optional infra) | Zero-config deploy, global CDN, serverless functions |
| **Package mgmt** | pnpm \+ Turborepo | Efficient installs, parallel builds, shared caching |
| **Type safety** | TypeScript | End-to-end type checking from DB to UI |

---

## Documentation

All internal specs live in `docs/` and follow a versioning convention (`-v1`, `-v2`, etc.):

| Document | Purpose |
| :---- | :---- |
| `rl-control-center-options-v2.md` | Decision record: why we chose this architecture |
| `rl-control-center-data-model-v2.md` | Entity definitions and relationships |
| `rl-control-center-build-framework-v2.md` | Build phasing (Sprint 0, Build 1–3, Run) |
| `rl-control-center-prisma-schema.md` | Complete Prisma schema with comments |
| `rl-control-center-api-layout-v1.md` | API routes, middleware, and response formats |
| `rl-control-center-web-layout-v1.md` | Astro page structure and React component hierarchy |
| `rl-control-center-monorepo-setup-v1.md` | Root config files and workspace setup |
| `rl-control-center-agent-instructions-v1.md` | Guidelines for AI assistants editing this repo |
| `relaylaunch-market-landscape-v1.md` | Market data and competitive landscape |

### Agent instructions

If you're using Claude, Cursor, or another AI assistant to edit this repo:

1. Attach or reference `docs/rl-control-center-agent-instructions-v1.md` in your first prompt  
2. The agent will treat v2 docs as canonical and propose v3 docs for any structural changes  
3. This prevents scope creep and keeps the architecture stable

---

## Deployment

### Deploy to Vercel (recommended)

1. **API:**  
     
   cd apps/api  
     
   vercel \--prod  
     
   \# Set environment variables in Vercel dashboard:  
     
   \# DATABASE\_URL, JWT\_SECRET, etc.  
     
2. **Web:**  
     
   cd apps/web  
     
   vercel \--prod  
     
   \# Set PUBLIC\_API\_URL to your API domain

### Deploy with Terraform (optional)

If you want AWS-managed RDS, S3, and monitoring:

cd infra/terraform

terraform init

terraform plan

terraform apply

See `docs/rl-control-center-options-v2.md` for the infrastructure decision rationale.

---

## Scripts

All scripts are defined in the root `package.json` and orchestrated by Turbo:

| Command | What it does |
| :---- | :---- |
| `pnpm dev` | Start all apps in dev mode (API \+ web) |
| `pnpm build` | Build all apps for production |
| `pnpm typecheck` | Run TypeScript compiler across workspace |
| `pnpm lint` | Run ESLint across all packages |
| `pnpm test` | Run all tests (when implemented) |
| `pnpm clean` | Remove all `node_modules` and build artifacts |

**Example: type-check everything before commit**

pnpm typecheck

---

## Contributing

### Internal contributors

This is a private product repo for RelayLaunch. If you're on the team:

1. Create a feature branch from `main`  
2. Make your changes, following the patterns in the docs  
3. Run `pnpm typecheck` and `pnpm lint` before pushing  
4. Open a PR and request review  
5. After approval, merge to `main` and deploy

### External contributors

Not currently accepting external PRs. If you're interested in collaborating, email \[[your-email@relaylaunch.com](mailto:your-email@relaylaunch.com)\].

---

## Testing

Unit and integration tests are planned for Q2 2026\. Current focus is on:

- API route tests (Vitest \+ Supertest)  
- Component tests (Vitest \+ Testing Library)  
- E2E tests (Playwright)

Placeholder test files are in `apps/api/src/__tests__` and `apps/web/src/__tests__`.

---

## Roadmap

### Phase 1: Core Control Center (Q1 2026\)

- ✅ Data model and Prisma schema  
- ✅ API routes for tenants, snapshots, approvals  
- ✅ Astro \+ React UI with dashboard pages  
- ✅ Manual seeding and demo tenant  
- 🚧 Authentication (JWT \+ sessions)  
- 🚧 Approval workflow UI

### Phase 2: Workflow Engine Integration (Q2 2026\)

- Webhook receivers for n8n, Zapier, Make  
- Auto-populate workflow inventory from third-party platforms  
- Real-time execution logs  
- Error alerting and retry logic

### Phase 3: AI Agent Orchestration (Q3 2026\)

- Agent registry and version control  
- Prompt versioning and A/B testing  
- Token usage tracking and budget alerts  
- Agent marketplace for reusable skills

### Phase 4: Advanced Analytics (Q4 2026\)

- Custom KPI builder  
- Forecasting and anomaly detection  
- Executive dashboard with board-level metrics  
- White-label options for agencies

---

## Security and compliance

- **Authentication:** JWT tokens \+ HTTP-only cookies (to be implemented)  
- **Authorization:** Role-based access control (Admin, Editor, Viewer per tenant)  
- **Database:** Row-level security planned for multi-tenancy  
- **Secrets:** All secrets in environment variables, never committed  
- **Dependencies:** Renovate bot for automated updates (to be configured)  
- **Logging:** Structured logs to CloudWatch or Datadog (optional)

---

## License

Proprietary. Copyright 2026 RelayLaunch LLC. All rights reserved.

This software is not open source. Unauthorized copying, modification, or distribution is prohibited.

---

## Support and contact

- **Issues:** Open an issue in this repo for bugs or feature requests  
- **Questions:** Email \[[your-email@relaylaunch.com](mailto:your-email@relaylaunch.com)\]  
- **Docs:** All internal specs in `docs/`  
- **Website:** [relaylaunch.com](https://relaylaunch.com)

---

## Acknowledgments

Built with:

- [Astro](https://astro.build) \- Web framework  
- [Prisma](https://prisma.io) \- Database ORM  
- [Turborepo](https://turbo.build) \- Monorepo tooling  
- [Vercel](https://vercel.com) \- Deployment platform  
- [shadcn/ui](https://ui.shadcn.com) \- UI component inspiration

Special thanks to the infrastructure and DevOps communities for sharing patterns and best practices.

---

**Ready to launch ops on autopilot?** Start with `pnpm dev` and explore the demo tenant dashboard.  
