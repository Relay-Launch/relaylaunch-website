# RelayLaunch Control Center – Data Model & API Spec (v2)

This v2 document keeps the same logical data model as v1 and adds **Phase 1 tech context** (Node.js + TypeScript API on Vercel, Supabase Postgres). It should be treated as the canonical contract between API and front‑end.

Where possible, names are chosen to map cleanly to both **TypeScript interfaces** and a future **Prisma schema**.

---

## 0. Phase 1 Tech Context (for Agents)

- **Language:** Node.js + TypeScript
- **API Hosting (Phase 1):** Vercel serverless functions
- **Database (Phase 1):** Supabase Postgres
- **Front‑end:** Astro app calling the API from the browser

All examples in this document assume:
- A REST/JSON API implemented in Node/TypeScript.
- Prisma or similar ORM mapping these entities to Postgres tables.

---

## 1. Core Concepts

- **Tenant** – a client organization (clinic, agency, SaaS, etc.).
- **User** – a person logging into the Control Center (client users + RelayLaunch admins).
- **Workflow Template** – reusable automation patterns (lead capture, invoice automation, etc.).
- **Tenant Workflow** – an instance of a workflow template wired to a tenant.
- **Agent Template** – reusable AI agent patterns (e.g., Social Content Agent).
- **Tenant Agent** – an instance of an agent template for a tenant.
- **Metrics** – aggregated, per‑day metrics for tenants and workflows.
- **Approvals** – queued items requiring human approval.
- **Change Requests** – client‑requested changes and new automations.

These concepts are stable across hosting environments (Vercel vs AWS).

---

## 2. Entity Schemas (Logical)

### 2.1 Tenant

```ts
interface Tenant {
  id: string;
  slug: string;
  name: string;
  primaryContact: {
    name: string;
    email: string;
    phone?: string | null;
  };
  plan: 'launch' | 'run' | 'scale';
  status: 'active' | 'paused' | 'prospect' | 'offboarded';
  branding?: {
    logoUrl?: string | null;
    accentColor?: string | null;
  };
  n8n: {
    instanceUrl: string;
    tenantIdentifier?: string | null;
  };
  aws?: {
    accountId?: string | null;
    region?: string | null;
  };
  metricsConfig: {
    hoursSavedPerRunDefault: number;
    hoursSavedOverrides?: Record<string, number>;
  };
  changeAllowances: {
    smallPerMonth: number;
    mediumPerMonth: number;
    newPerMonth: number;
    newPerQuarter: number;
  };
  featureFlags: {
    marketingMetrics: boolean;
    advancedDashboards: boolean;
    experimentsArea: boolean;
  };
  createdAt: string;
  updatedAt: string;
}
```

**Postgres mapping (Phase 1):**
- Table `tenants`
- JSONB columns: `primary_contact`, `branding`, `n8n`, `aws`, `metrics_config`, `change_allowances`, `feature_flags`

---

### 2.2 User

```ts
interface User {
  id: string;
  tenantId?: string | null; // null = RelayLaunch internal admin
  email: string;
  name: string;
  role: 'owner' | 'member' | 'admin';
  status: 'active' | 'invited' | 'disabled';
  lastLoginAt?: string | null;
  createdAt: string;
  updatedAt: string;
}
```

**Postgres mapping:**
- Table `users`
- Foreign key `tenant_id` → `tenants.id` (nullable for internal admins)

---

### 2.3 WorkflowTemplate & TenantWorkflow

```ts
type WorkflowCategory =
  | 'leads'
  | 'sales'
  | 'billing'
  | 'operations'
  | 'marketing'
  | 'admin';

interface WorkflowTemplate {
  id: string;
  key: string; // e.g. 'lead_capture_crm'
  name: string;
  category: WorkflowCategory;
  shortDescription: string;
  longDescription: string;
  n8nTemplateId?: string | null;
  docsUrl?: string | null;
  defaultHoursSavedPerRun: number;
  createdAt: string;
  updatedAt: string;
}

interface TenantWorkflow {
  id: string;
  tenantId: string;
  workflowTemplateId: string;
  displayName: string;
  status: 'on' | 'off' | 'draft';
  n8nWorkflowId: string;
  lastRunAt?: string | null;
  config: Record<string, unknown>;
  createdAt: string;
  updatedAt: string;
}
```

**Postgres mapping:**
- Table `workflow_templates`
- Table `tenant_workflows` with FKs to `tenants` and `workflow_templates`, `config` as JSONB.

---

### 2.4 AgentTemplate & TenantAgent

```ts
type AgentCategory =
  | 'marketing'
  | 'sales'
  | 'finance'
  | 'ops'
  | 'infra'
  | 'design'
  | 'dev';

interface AgentTemplate {
  id: string;
  key: string; // 'social_content_agent'
  name: string;
  category: AgentCategory;
  roleType: 'business' | 'job_helper';
  shortTagline: string;
  longDescription: string;
  iconRef: string;
  toolsUsed: string[];
  defaultInputs: string[];
  defaultOutputs: string[];
  estimatedHoursSavedPerMonth: number;
  docsUrl?: string | null;
  createdAt: string;
  updatedAt: string;
}

interface TenantAgent {
  id: string;
  tenantId: string;
  agentTemplateId: string;
  status: 'active' | 'paused' | 'planned';
  displayName: string;
  config: Record<string, unknown>;
  lastRunAt?: string | null;
  runsLast30Days: number;
  estimatedHoursSavedLast30Days: number;
  createdAt: string;
  updatedAt: string;
}
```

**Postgres mapping:**
- Tables `agent_templates` and `tenant_agents`
- `config` as JSONB on `tenant_agents`

---

### 2.5 Metrics

```ts
interface TenantDailyMetrics {
  id: string;
  tenantId: string;
  date: string; // YYYY-MM-DD
  leadsCaptured: number;
  automationsRun: number;
  hoursSaved: number;
  marketing?: {
    followersGained: number;
    campaignsRunning: number;
  };
  createdAt: string;
}

interface WorkflowDailyMetrics {
  id: string;
  tenantWorkflowId: string;
  date: string;
  runsSuccess: number;
  runsFailed: number;
  hoursSaved: number;
  createdAt: string;
}
```

**Postgres mapping:**
- Tables `tenant_daily_metrics` and `workflow_daily_metrics`
- Composite uniqueness on `(tenant_id, date)` and `(tenant_workflow_id, date)`
- Optional `marketing` JSONB on `tenant_daily_metrics` if needed

---

### 2.6 Approvals

```ts
type ApprovalType =
  | 'email'
  | 'social_post'
  | 'offer'
  | 'automation_action';

interface ApprovalPayload {
  subject?: string | null;
  body?: string | null;
  channel?: 'instagram' | 'facebook' | 'linkedin' | 'email' | 'other';
  scheduledTime?: string | null;
  metadata?: Record<string, unknown>;
}

interface Approval {
  id: string;
  tenantId: string;
  agentOrWorkflowId?: string | null;
  type: ApprovalType;
  status: 'pending' | 'approved' | 'rejected' | 'executed';
  payload: ApprovalPayload;
  requestedAt: string;
  approvedAt?: string | null;
  approvedByUserId?: string | null;
  rejectionReason?: string | null;
  createdAt: string;
  updatedAt: string;
}
```

**Postgres mapping:**
- Table `approvals`
- JSONB column `payload`
- FKs to `tenants` and optionally `users` via `approved_by_user_id`

---

### 2.7 Change Requests

```ts
type ChangeType = 'small' | 'medium' | 'new';

type ChangeStatus =
  | 'open'
  | 'in_progress'
  | 'completed'
  | 'deferred'
  | 'rejected';

interface ChangeRequest {
  id: string;
  tenantId: string;
  createdByUserId?: string | null;
  type: ChangeType;
  status: ChangeStatus;
  affectedWorkflowId?: string | null; // tenant_workflow_id
  affectedAgentId?: string | null;    // tenant_agent_id
  title: string;
  description: string;
  priority: 'normal' | 'high';
  internalEstimatedHours: number;
  countsAgainstAllowance: boolean;
  createdAt: string;
  updatedAt: string;
  completedAt?: string | null;
}
```

**Postgres mapping:**
- Table `change_requests`
- FKs `tenant_id`, `created_by_user_id`, `affected_workflow_id`, `affected_agent_id`

---

## 3. API Surface (v1, unchanged)

All endpoints are JSON over HTTPS. Auth uses a bearer token that encodes `userId` and `tenantId`.

### 3.1 Auth & Context

- `GET /me`
  - Returns current user and tenant context.
- `GET /tenants` (admin only)
  - List tenants for RelayLaunch internal users.
- `GET /tenants/:id`
  - Return full tenant record.

---

### 3.2 Tenant Snapshot

- `GET /tenants/:id/snapshot`
  - Returns a `TenantSnapshot` object aggregating tenant info, metrics, workflows, agents, and pending approvals.

### 3.3 Workflows

- `GET /tenants/:id/workflows`
- `PATCH /tenants/:id/workflows/:workflowId` (limited fields: `status`, `displayName`)

### 3.4 Agents

- `GET /tenants/:id/agents`
- `GET /agent-templates` (admin)

### 3.5 Approvals

- `GET /tenants/:id/approvals?status=pending`
- `POST /tenants/:id/approvals/:approvalId/decision`

### 3.6 Change Requests

- `GET /tenants/:id/change-requests`
- `POST /tenants/:id/change-requests`
- `PATCH /tenants/:id/change-requests/:id` (admin)

This surface remains the same whether the API runs on Vercel or AWS; only the deployment changes.