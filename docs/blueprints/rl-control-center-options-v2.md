# RelayLaunch Control Center – Technology Options & Decisions (v2)

## Purpose
This document summarizes the **final technology decisions for Phase 1** of the RelayLaunch Control Center build and keeps the future Hybrid/AWS path documented for later. It replaces the earlier v1 options overview.

---

## Phase 1 Decisions (Locked)

**Language & runtime**
- **Primary language:** Node.js + TypeScript
- **Runtime:** Node 20+ (LTS)

**Hosting (Phase 1)**
- **Web app (Astro UI):** Vercel
- **API:** Vercel serverless functions (Node.js/TypeScript)
- **Database:** Managed Postgres (Supabase) reachable from Vercel

**Architecture goals for Phase 1**
- Ship a working v1 Control Center quickly with:
  - Multi-tenant data model
  - Read-only dashboard across Overview, Workflows, Agents
  - Real metrics for at least one tenant once Build 3 is complete
- Minimize DevOps overhead while you validate the product and client experience.

These decisions are considered **authoritative for any agents or collaborators** until a future v3+ document explicitly changes them.

---

## Future Direction (Phase 2+ – Not Yet Implemented)

When v1 is stable and you have active clients, you plan to:

- Migrate the **API and database** to AWS (ECS/Fargate or EC2 + RDS Postgres) using Terraform.
- Keep the **Astro UI on Vercel** for DX and previews.
- Point `api.relaylaunch.com` to AWS and `app.relaylaunch.com` to Vercel.

This Hybrid model will provide:
- Private networking around RDS
- Enterprise-grade patterns that mirror client infrastructure
- Continued fast iteration on the UI

Until that migration is executed, all implementation work should target the Phase 1 Vercel-based architecture.

---

## Option 1 (Chosen for Phase 1) – Node.js/TypeScript API on Vercel

### Stack
- **Language:** TypeScript
- **Runtime:** Node.js
- **API Hosting:** Vercel serverless functions
- **Database:** Supabase Postgres (or equivalent Postgres reachable from Vercel)

### Pros
- **Developer experience:**
  - First‑class TypeScript support, fast local dev, easy hot‑reload.
  - Vercel has strong DX, preview deployments per pull request.
- **Scalability:**
  - Serverless functions scale automatically based on traffic, no capacity planning.
- **Simplicity:**
  - No server management; focus on code, schema, and product features.
  - Fits naturally with the existing Astro marketing site and future Control Center UI.
- **Integrations:**
  - Excellent ecosystem for REST/GraphQL APIs, webhooks, and third‑party services.
  - Easy to connect to n8n, Stripe, Cloudflare, Apollo, etc. via REST SDKs and webhooks.
- **Cost:**
  - Free/low‑cost tiers are usually enough for early traffic and internal dog‑fooding.

### Cons
- **Cold starts & time limits:**
  - Long‑running operations can hit serverless execution limits.
  - Occasional cold‑start latency, usually acceptable for internal dashboards.
- **Vendor coupling:**
  - Vercel‑specific build and function routing adds some lock‑in.
- **Networking to private resources:**
  - If Postgres is moved into a private VPC in future, Vercel will require a secure public entry point or managed proxy.

### When to reconsider
- When you consistently hit execution time limits or need tighter control around networking and compliance.
- When you have enough recurring revenue and operational load to justify AWS complexity.

---

## Option 2 – Node.js/TypeScript API on AWS (ECS/Fargate or EC2)

This option is **documented for Phase 2+** and should not be implemented yet.

### Stack
- **Language:** TypeScript
- **Runtime:** Node.js
- **API Hosting:**
  - ECS + Fargate (containerized service), or
  - A small EC2 instance running Node with PM2/systemd.
- **Database:** Postgres on AWS RDS.
- **Networking:** Private subnets, ALB, Cloudflare in front.

### Pros
- Full control over networking, IAM, and VPC layout.
- No cold starts; the API is a persistent service.
- Architecture matches what you will deploy for clients, especially in regulated industries.

### Cons
- Higher setup and ongoing maintenance cost (time and money).
- Requires VPC, RDS, ECS/EC2, ALB, monitoring, backups, etc.

Use this once the product is validated, not before.

---

## Option 3 – Hybrid: Vercel for Web, AWS for API (Target End‑State)

### Stack
- **Web (Astro UI):** Vercel
- **API:** AWS (ECS/Fargate or EC2) behind Cloudflare or ALB
- **Database:** RDS Postgres in private subnets

### Pros
- Best blend of DX (Vercel) and control/security (AWS).
- Realistic pattern for future client builds.

### Cons
- Two deploy pipelines and providers; more secrets, more routing complexity.

### Migration Plan (High Level)
1. Build and validate v1 completely on Vercel API + Supabase.
2. Provision AWS infra via Terraform and create an RDS Postgres.
3. Migrate data from Supabase → RDS.
4. Re-point the API base URL in the Astro app to AWS.
5. Gradually decommission the Vercel API while monitoring.

---

## Language & Framework Decision (Confirmed)

- **Language:** Node.js + TypeScript across API, any serverless functions, and shared libraries.
- **Front‑end:** Astro (with React islands where needed) for the Control Center UI.

All future architectural diagrams, code examples, and agent instructions should assume this stack by default unless a document explicitly states otherwise.