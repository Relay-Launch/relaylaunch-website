# RelayLaunch Control Center – Database Seeding & Sample Data (v1)

This document describes how to **seed the database** for the RelayLaunch Control Center using Prisma and Supabase Postgres. The goal is to create realistic demo data for:

- Internal development and testing
- Live demos and screenshots
- Quick onboarding of the first real tenant

It assumes the Prisma schema defined in `rl-control-center-prisma-schema.md` and the entities from `rl-control-center-data-model-v2.md` (Tenant, User, WorkflowTemplate, TenantWorkflow, AgentTemplate, TenantAgent, Approval, ChangeRequest, metrics tables if present).

---

## 1. Seeding Approach

We will use Prisma’s built-in seeding mechanism:

- A **TypeScript seed script** (`prisma/seed.ts`) that:
  - Connects to the database via Prisma Client
  - Upserts a **RelayLaunch demo tenant**
  - Creates one or more **admin users**
  - Inserts **workflow templates** and **agent templates**
  - Creates **tenant-specific workflows and agents**
  - Adds **sample approvals and change requests**
  - Optionally populates **metrics / activity** for the dashboard
- Configure the seed command in `apps/api/package.json`.

This keeps sample data close to the schema and easy to adjust as the data model evolves.

---

## 2. File Locations

Within `apps/api`:

```text
apps/api/
  prisma/
    schema.prisma
    seed.ts        # Prisma seed script
  package.json
```

Make sure `schema.prisma` already matches the models in your Prisma schema doc.

---

## 3. Package Configuration

In `apps/api/package.json`, add a `prisma:seed` script and tell Prisma to use `tsx` to run the seed:

```json
{
  "scripts": {
    "prisma:generate": "prisma generate",
    "prisma:migrate": "prisma migrate dev",
    "prisma:studio": "prisma studio",
    "prisma:seed": "prisma db seed",
    "dev": "tsx watch src/server.ts",
    "build": "tsc && tsc-alias",
    "start": "node dist/server.js"
  },
  "prisma": {
    "seed": "tsx prisma/seed.ts"
  }
}
```

This configuration tells Prisma how to run the seed script.

---

## 4. Seed Script Structure (`prisma/seed.ts`)

Below is a detailed example seed script. Adjust field names to match your actual Prisma models.

```ts
// apps/api/prisma/seed.ts

import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient();

async function main() {
  console.log('Seeding RelayLaunch Control Center demo data...');

  // 1) Create or update the demo tenant
  const tenant = await prisma.tenant.upsert({
    where: { domain: 'demo.relaylaunch.com' },
    update: {},
    create: {
      name: 'RelayLaunch Demo Tenant',
      domain: 'demo.relaylaunch.com',
      plan: 'PROFESSIONAL',
      status: 'ACTIVE',
      subscriptionEndsAt: null,
    },
  });

  // 2) Admin user
  const adminUser = await prisma.user.upsert({
    where: { email: 'admin@relaylaunch-demo.com' },
    update: {},
    create: {
      tenantId: tenant.id,
      email: 'admin@relaylaunch-demo.com',
      name: 'Demo Admin',
      role: 'ADMIN',
    },
  });

  // 3) Workflow templates
  const leadCaptureTemplate = await prisma.workflowTemplate.upsert({
    where: { name: 'Inbound Lead Capture Funnel' },
    update: {},
    create: {
      name: 'Inbound Lead Capture Funnel',
      description: 'Captures leads from web forms and routes them into the CRM.',
      category: 'LEAD_FUNNEL',
      n8nWorkflowId: 'n8n-workflow-lead-capture',
      configSchema: {
        type: 'object',
        properties: {
          webhookUrl: { type: 'string' },
          crmEndpoint: { type: 'string' },
        },
      },
    },
  });

  const onboardingTemplate = await prisma.workflowTemplate.upsert({
    where: { name: 'New Customer Onboarding' },
    update: {},
    create: {
      name: 'New Customer Onboarding',
      description: 'Automated onboarding emails and tasks for new customers.',
      category: 'CUSTOMER_SUCCESS',
      n8nWorkflowId: 'n8n-workflow-onboarding',
      configSchema: {
        type: 'object',
        properties: {
          welcomeSequenceId: { type: 'string' },
        },
      },
    },
  });

  // 4) Tenant workflows based on templates
  const leadCaptureWorkflow = await prisma.tenantWorkflow.create({
    data: {
      tenantId: tenant.id,
      templateId: leadCaptureTemplate.id,
      customName: 'Website → CRM Lead Capture',
      status: 'ACTIVE',
      n8nInstanceId: 'n8n-instance-lead-capture-demo',
      config: {
        webhookUrl: 'https://hooks.demo.relaylaunch.com/leads',
        crmEndpoint: 'https://example-crm.com/api/leads',
      },
    },
  });

  const onboardingWorkflow = await prisma.tenantWorkflow.create({
    data: {
      tenantId: tenant.id,
      templateId: onboardingTemplate.id,
      customName: 'New Customer Onboarding',
      status: 'ACTIVE',
      n8nInstanceId: 'n8n-instance-onboarding-demo',
      config: {
        welcomeSequenceId: 'welcome-seq-01',
      },
    },
  });

  // 5) Agent templates
  const followUpAgentTemplate = await prisma.agentTemplate.upsert({
    where: { name: 'Lead Follow-up AI Agent' },
    update: {},
    create: {
      name: 'Lead Follow-up AI Agent',
      description: 'Follows up with leads via email and routes replies to sales.',
      category: 'OUTREACH',
      capabilities: ['email_follow_up', 'lead_scoring'],
      configSchema: {
        type: 'object',
        properties: {
          model: { type: 'string' },
          tone: { type: 'string' },
        },
      },
    },
  });

  // 6) Tenant agents
  const followUpAgent = await prisma.tenantAgent.create({
    data: {
      tenantId: tenant.id,
      templateId: followUpAgentTemplate.id,
      customName: 'Demo Lead Follow-up Bot',
      status: 'ACTIVE',
      config: {
        model: 'gpt-4.5',
        tone: 'helpful and concise',
      },
    },
  });

  // 7) Sample approvals
  const approval = await prisma.approval.create({
    data: {
      tenantId: tenant.id,
      requestedById: adminUser.id,
      type: 'AGENT_DEPLOYMENT',
      targetEntityId: followUpAgent.id,
      description: 'Deploy lead follow-up AI agent for inbound demo leads.',
      status: 'PENDING',
    },
  });

  // 8) Sample change requests
  await prisma.changeRequest.createMany({
    data: [
      {
        tenantId: tenant.id,
        requestedById: adminUser.id,
        category: 'SMALL',
        title: 'Adjust lead scoring threshold',
        description: 'Lower score threshold for MQL from 80 to 70.',
        status: 'IN_PROGRESS',
        approvalId: approval.id,
      },
      {
        tenantId: tenant.id,
        requestedById: adminUser.id,
        category: 'MEDIUM',
        title: 'Add new lead source from LinkedIn ads',
        description: 'Integrate LinkedIn Lead Gen forms into the capture workflow.',
        status: 'PENDING',
        approvalId: null,
      },
    ],
  });

  // 9) Optional: metrics & activity
  // Adjust if you have dedicated metrics/activity tables in your schema.

  console.log('Seeding complete.');
}

main()
  .catch((e) => {
    console.error(e);
    process.exit(1);
  })
  .finally(async () => {
    await prisma.$disconnect();
  });
```

---

## 5. Running the Seed Script

From `apps/api`:

```bash
pnpm prisma:seed
```

Or from the repo root (if you add a root-level script that delegates to `apps/api`):

```bash
pnpm --filter @control-center/api prisma:seed
```

Verify that:

- `prisma migrate dev` has been run at least once.
- `DATABASE_URL` in `.env` points to the correct database (local or Supabase).

---

## 6. Using Seed Data in the UI

Once seeding succeeds, you should have at least:

- One tenant with domain `demo.relaylaunch.com`.
- One admin user `admin@relaylaunch-demo.com`.
- Several workflows and an AI agent.
- Pending approvals and change requests.

In the UI:

- Use the seeded tenant ID in the dashboard URL: `/dashboard/<tenantId>`.
- `GET /api/me` can return the seeded admin user (for now, you can implement `getMe` as `findFirst({ where: { role: 'ADMIN' } })`).
- The dashboard snapshot endpoint (`/api/tenants/:id/snapshot`) should aggregate data from these seeded records to display realistic metrics and activity.

---

## 7. Seeding Strategies for Different Environments

### 7.1 Local Development

- Run `pnpm prisma:migrate` + `pnpm prisma:seed` whenever you reset your local DB.
- It’s fine to wipe and reseed frequently.

### 7.2 Staging / Demo Environment

- Use the same seed script against a dedicated staging database.
- Optionally parameterize seed data with environment variables (e.g., `DEMO_TENANT_DOMAIN`).
- Avoid using real customer data here; stick to sanitized/demo data.

### 7.3 Production

- Seed only **minimal** data needed to onboard the first tenant (e.g., base templates) or use one-time migration scripts.
- Do **not** seed fake demo tenants in production unless you explicitly want a demo tenant.

---

## 8. Evolving the Seed Script

As the schema evolves:

- Keep the seed script updated alongside migrations.
- When adding new required fields to Prisma models:
  - Update `schema.prisma` and run a migration.
  - Update `seed.ts` to provide default values.
- When introducing new entities (e.g., Metrics tables):
  - Extend the seed script with a helper that inserts realistic monthly/weekly data.

Always test the seed script locally before running it against shared environments.

---

## 9. Checklist

Before using seed data in demos or screenshots:

- [ ] `pnpm prisma:migrate` applied successfully.
- [ ] `pnpm prisma:seed` ran without errors.
- [ ] `/api/tenants/:id` returns the demo tenant and its workflows/agents.
- [ ] `/api/tenants/:id/snapshot` returns non-empty metrics and recent activity.
- [ ] `/api/me` returns the expected admin user.
- [ ] Dashboard UI (`/dashboard/<tenantId>`) renders populated cards and lists.

This seeding strategy gives you a consistent, realistic environment to build, demo, and iterate on the RelayLaunch Control Center.
