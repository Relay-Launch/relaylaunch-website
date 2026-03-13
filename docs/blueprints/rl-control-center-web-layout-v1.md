# RelayLaunch Control Center – Web App Layout & Component Plan (v1)

This document describes **how to structure and build the `apps/web` project** for the RelayLaunch Control Center, assuming:

- Astro 4.x as the UI framework
- React components for interactive islands
- Hosting on **Vercel** for Phase 1
- Consuming the API from `apps/api` (as defined in `rl-control-center-api-layout-v1.md`)

It is meant to be read alongside:
- `rl-control-center-options-v2.md`
- `rl-control-center-data-model-v2.md`
- `rl-control-center-build-framework-v2.md`
- `rl-control-center-prisma-schema.md`
- `rl-control-center-api-layout-v1.md`
- `rl-control-center-agent-instructions-v1.md`

---

## 1. Folder & File Structure for `apps/web`

Under the monorepo root:

```text
control-center/
  apps/
    web/
      src/
        pages/
          index.astro
          dashboard/
            [tenantId].astro
        components/
          layout/
            Header.astro
            Footer.astro
            Sidebar.astro
          dashboard/
            SnapshotOverview.tsx
            WorkflowList.tsx
            AgentList.tsx
            ApprovalList.tsx
            ChangeRequestList.tsx
          ui/
            Card.tsx
            Button.tsx
            Badge.tsx
            Modal.tsx
        lib/
          api-client.ts
          types.ts
        styles/
          global.css
      public/
        favicon.svg
        logo-rl.svg
      astro.config.mjs
      tsconfig.json
      package.json
      vercel.json
```

### 1.1 Purpose of key directories

- `src/pages/`
  - Astro routing layer; each `.astro` file is a route.
  - `/dashboard/[tenantId].astro` renders the main dashboard for a given tenant.
- `src/components/layout/`
  - Shared layout components (header, sidebar, footer) used across pages.
- `src/components/dashboard/`
  - React islands for interactive dashboard widgets (metrics, lists, charts).
- `src/components/ui/`
  - Reusable UI primitives (buttons, cards, badges, modals).
- `src/lib/`
  - Utilities, API client helpers, and shared TypeScript types.
- `src/styles/`
  - Global CSS or Tailwind config.
- `public/`
  - Static assets (logo, favicon, etc.).

---

## 2. Astro Configuration (`astro.config.mjs`)

A minimal Astro config for React islands and Vercel deployment:

```js
// apps/web/astro.config.mjs

import { defineConfig } from 'astro/config';
import react from '@astrojs/react';
import vercel from '@astrojs/vercel/serverless';

export default defineConfig({
  integrations: [react()],
  output: 'server', // SSR mode for dynamic tenant routes
  adapter: vercel(),
});
```

This enables:
- React components as Astro islands (client-side interactivity).
- Server-side rendering for dynamic routes (e.g., `/dashboard/[tenantId]`).
- Automatic Vercel deployment with SSR support.

---

## 3. TypeScript Configuration (`tsconfig.json`)

```json
{
  "extends": "../../tsconfig.base.json",
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "jsx": "react-jsx",
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "allowSyntheticDefaultImports": true,
    "esModuleInterop": true,
    "strict": true,
    "skipLibCheck": true,
    "baseUrl": ".",
    "paths": {
      "@components/*": ["src/components/*"],
      "@lib/*": ["src/lib/*"]
    }
  },
  "include": ["src"],
  "exclude": ["node_modules", "dist"]
}
```

This provides path aliases (`@components/`, `@lib/`) for cleaner imports.

---

## 4. API Client Utility (`lib/api-client.ts`)

A simple typed HTTP client for calling the Control Center API:

```ts
// apps/web/src/lib/api-client.ts

import type { Tenant, TenantSnapshot, User } from './types';

const API_BASE = import.meta.env.PUBLIC_API_URL || 'http://localhost:3000/api';

async function fetchJSON<T>(path: string): Promise<T> {
  const res = await fetch(`${API_BASE}${path}`);
  if (!res.ok) {
    const error = await res.json().catch(() => ({ error: 'Unknown error' }));
    throw new Error(error.error || `API error: ${res.status}`);
  }
  return res.json();
}

export const api = {
  async getMe(): Promise<{ user: User }> {
    return fetchJSON('/me');
  },

  async getTenant(id: string): Promise<{ tenant: Tenant }> {
    return fetchJSON(`/tenants/${id}`);
  },

  async getTenantSnapshot(id: string): Promise<TenantSnapshot> {
    return fetchJSON(`/tenants/${id}/snapshot`);
  },
};
```

### 4.1 Environment variable setup

In Vercel, set:
- `PUBLIC_API_URL` → `https://your-api.vercel.app/api` (or your deployed API domain).

For local dev, create `apps/web/.env`:

```env
PUBLIC_API_URL=http://localhost:3000/api
```

---

## 5. Shared Types (`lib/types.ts`)

Re-export or mirror the core types from `rl-control-center-data-model-v2.md`:

```ts
// apps/web/src/lib/types.ts

export type TenantPlan = 'STARTER' | 'PROFESSIONAL' | 'ENTERPRISE';
export type UserRole = 'ADMIN' | 'MEMBER';
export type WorkflowStatus = 'ACTIVE' | 'PAUSED' | 'ERROR';
export type AgentCategory = 'LEAD_CAPTURE' | 'CUSTOMER_SUPPORT' | 'ANALYTICS' | 'OUTREACH';
export type ApprovalStatus = 'PENDING' | 'APPROVED' | 'REJECTED';
export type ChangeRequestStatus = 'PENDING' | 'IN_PROGRESS' | 'COMPLETED' | 'REJECTED';

export interface Tenant {
  id: string;
  name: string;
  domain: string;
  plan: TenantPlan;
  status: 'ACTIVE' | 'SUSPENDED' | 'TRIAL';
  createdAt: string;
  subscriptionEndsAt: string | null;
}

export interface User {
  id: string;
  tenantId: string;
  email: string;
  name: string;
  role: UserRole;
  tenant: Tenant;
}

export interface WorkflowTemplate {
  id: string;
  name: string;
  description: string;
  category: string;
  n8nWorkflowId: string | null;
  configSchema: Record<string, any>;
}

export interface TenantWorkflow {
  id: string;
  tenantId: string;
  templateId: string;
  customName: string | null;
  status: WorkflowStatus;
  n8nInstanceId: string | null;
  config: Record<string, any>;
  createdAt: string;
  lastRunAt: string | null;
  template?: WorkflowTemplate;
}

export interface AgentTemplate {
  id: string;
  name: string;
  description: string;
  category: AgentCategory;
  capabilities: string[];
  configSchema: Record<string, any>;
}

export interface TenantAgent {
  id: string;
  tenantId: string;
  templateId: string;
  customName: string | null;
  status: 'ACTIVE' | 'PAUSED';
  config: Record<string, any>;
  createdAt: string;
  lastActiveAt: string | null;
  template?: AgentTemplate;
}

export interface MetricSnapshot {
  leadsCaptured: number;
  automationsRun: number;
  hoursSaved: number;
}

export interface ChangeUsage {
  smallUsed: number;
  smallAllowed: number;
  mediumUsed: number;
  mediumAllowed: number;
  newUsed: number;
  newAllowed: number;
  newAllowedPerQuarter: number;
}

export interface ActivityItem {
  id: string;
  timestamp: string;
  type: 'workflow_run' | 'agent_action' | 'approval_request' | 'change_request';
  description: string;
  metadata?: Record<string, any>;
}

export interface Approval {
  id: string;
  tenantId: string;
  requestedById: string;
  type: 'WORKFLOW_ACTIVATION' | 'AGENT_DEPLOYMENT' | 'CONFIG_CHANGE';
  targetEntityId: string;
  description: string;
  status: ApprovalStatus;
  createdAt: string;
  resolvedAt: string | null;
  resolvedById: string | null;
}

export interface ChangeRequest {
  id: string;
  tenantId: string;
  requestedById: string;
  category: 'SMALL' | 'MEDIUM' | 'NEW';
  title: string;
  description: string;
  status: ChangeRequestStatus;
  approvalId: string | null;
  createdAt: string;
  completedAt: string | null;
}

export interface TenantSnapshot {
  tenant: Tenant;
  overview: {
    period: string;
    metrics: MetricSnapshot;
    changeUsage: ChangeUsage;
    recentActivity: ActivityItem[];
  };
  workflows: TenantWorkflow[];
  agents: TenantAgent[];
  approvalsPending: Approval[];
}
```

These types match the API contract from `rl-control-center-data-model-v2.md`.

---

## 6. Layout Components

### 6.1 Header (`components/layout/Header.astro`)

```astro
---
// apps/web/src/components/layout/Header.astro
import { api } from '@lib/api-client';

let userName = 'User';
try {
  const { user } = await api.getMe();
  userName = user.name;
} catch (err) {
  console.error('Failed to fetch user:', err);
}
---

<header class="header">
  <div class="header-content">
    <div class="logo">
      <img src="/logo-rl.svg" alt="RelayLaunch" />
      <span>Control Center</span>
    </div>
    <nav class="nav">
      <a href="/">Home</a>
      <a href="/dashboard">Dashboard</a>
    </nav>
    <div class="user-info">
      <span>{userName}</span>
    </div>
  </div>
</header>

<style>
  .header {
    background: #1a1a1a;
    border-bottom: 1px solid #333;
    padding: 1rem 2rem;
  }
  .header-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: 1400px;
    margin: 0 auto;
  }
  .logo {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    font-weight: 600;
    font-size: 1.125rem;
  }
  .logo img {
    height: 32px;
  }
  .nav {
    display: flex;
    gap: 1.5rem;
  }
  .nav a {
    color: #ccc;
    text-decoration: none;
    transition: color 0.2s;
  }
  .nav a:hover {
    color: #fff;
  }
  .user-info {
    color: #aaa;
    font-size: 0.875rem;
  }
</style>
```

### 6.2 Sidebar (`components/layout/Sidebar.astro`)

```astro
---
// apps/web/src/components/layout/Sidebar.astro
const { tenantId } = Astro.props;
---

<aside class="sidebar">
  <nav class="sidebar-nav">
    <a href={`/dashboard/${tenantId}`} class="nav-item active">
      <span class="icon">📊</span>
      <span>Overview</span>
    </a>
    <a href={`/dashboard/${tenantId}/workflows`} class="nav-item">
      <span class="icon">⚙️</span>
      <span>Workflows</span>
    </a>
    <a href={`/dashboard/${tenantId}/agents`} class="nav-item">
      <span class="icon">🤖</span>
      <span>AI Agents</span>
    </a>
    <a href={`/dashboard/${tenantId}/approvals`} class="nav-item">
      <span class="icon">✅</span>
      <span>Approvals</span>
    </a>
    <a href={`/dashboard/${tenantId}/changes`} class="nav-item">
      <span class="icon">🔧</span>
      <span>Change Requests</span>
    </a>
  </nav>
</aside>

<style>
  .sidebar {
    width: 240px;
    background: #1e1e1e;
    border-right: 1px solid #333;
    padding: 1.5rem 0;
    min-height: 100vh;
  }
  .sidebar-nav {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }
  .nav-item {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.75rem 1.5rem;
    color: #aaa;
    text-decoration: none;
    transition: all 0.2s;
  }
  .nav-item:hover {
    background: #2a2a2a;
    color: #fff;
  }
  .nav-item.active {
    background: #2d3748;
    color: #fff;
    border-left: 3px solid #3b82f6;
  }
  .icon {
    font-size: 1.25rem;
  }
</style>
```

---

## 7. Dashboard Page (`pages/dashboard/[tenantId].astro`)

The main dashboard route that fetches and renders the tenant snapshot:

```astro
---
// apps/web/src/pages/dashboard/[tenantId].astro
import Header from '@components/layout/Header.astro';
import Sidebar from '@components/layout/Sidebar.astro';
import SnapshotOverview from '@components/dashboard/SnapshotOverview';
import WorkflowList from '@components/dashboard/WorkflowList';
import AgentList from '@components/dashboard/AgentList';
import ApprovalList from '@components/dashboard/ApprovalList';
import { api } from '@lib/api-client';

const { tenantId } = Astro.params;

let snapshot;
try {
  snapshot = await api.getTenantSnapshot(tenantId);
} catch (err) {
  return Astro.redirect('/error?message=Tenant not found');
}
---

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{snapshot.tenant.name} Dashboard | RelayLaunch Control Center</title>
  <link rel="stylesheet" href="/styles/global.css" />
</head>
<body>
  <Header />
  <div class="layout">
    <Sidebar tenantId={tenantId} />
    <main class="main-content">
      <h1>{snapshot.tenant.name} Dashboard</h1>
      
      <SnapshotOverview
        client:load
        overview={snapshot.overview}
        tenant={snapshot.tenant}
      />

      <div class="grid-2">
        <WorkflowList client:load workflows={snapshot.workflows} />
        <AgentList client:load agents={snapshot.agents} />
      </div>

      {snapshot.approvalsPending.length > 0 && (
        <ApprovalList client:load approvals={snapshot.approvalsPending} />
      )}
    </main>
  </div>
</body>
</html>

<style>
  .layout {
    display: flex;
  }
  .main-content {
    flex: 1;
    padding: 2rem;
    background: #0f0f0f;
    color: #fff;
    min-height: 100vh;
  }
  h1 {
    font-size: 2rem;
    margin-bottom: 1.5rem;
  }
  .grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5rem;
    margin-top: 1.5rem;
  }
</style>
```

Note the `client:load` directive on React components to make them interactive islands.

---

## 8. Dashboard React Components

### 8.1 `SnapshotOverview.tsx`

Displays high-level metrics and change usage:

```tsx
// apps/web/src/components/dashboard/SnapshotOverview.tsx
import React from 'react';
import type { TenantSnapshot } from '@lib/types';
import Card from '@components/ui/Card';

interface Props {
  overview: TenantSnapshot['overview'];
  tenant: TenantSnapshot['tenant'];
}

export default function SnapshotOverview({ overview, tenant }: Props) {
  const { metrics, changeUsage } = overview;

  return (
    <div className="overview-grid">
      <Card title="Leads Captured">
        <div className="metric-value">{metrics.leadsCaptured.toLocaleString()}</div>
        <div className="metric-label">Last 30 days</div>
      </Card>

      <Card title="Automations Run">
        <div className="metric-value">{metrics.automationsRun.toLocaleString()}</div>
        <div className="metric-label">Last 30 days</div>
      </Card>

      <Card title="Hours Saved">
        <div className="metric-value">{metrics.hoursSaved.toLocaleString()}</div>
        <div className="metric-label">Estimated</div>
      </Card>

      <Card title="Change Budget">
        <div className="change-budget">
          <div className="budget-row">
            <span>Small:</span>
            <span>{changeUsage.smallUsed} / {changeUsage.smallAllowed}</span>
          </div>
          <div className="budget-row">
            <span>Medium:</span>
            <span>{changeUsage.mediumUsed} / {changeUsage.mediumAllowed}</span>
          </div>
          <div className="budget-row">
            <span>New (Quarterly):</span>
            <span>{changeUsage.newUsed} / {changeUsage.newAllowed}</span>
          </div>
        </div>
      </Card>
    </div>
  );
}
```

### 8.2 `WorkflowList.tsx`

Displays active workflows:

```tsx
// apps/web/src/components/dashboard/WorkflowList.tsx
import React from 'react';
import type { TenantWorkflow } from '@lib/types';
import Card from '@components/ui/Card';
import Badge from '@components/ui/Badge';

interface Props {
  workflows: TenantWorkflow[];
}

export default function WorkflowList({ workflows }: Props) {
  return (
    <Card title="Active Workflows">
      {workflows.length === 0 ? (
        <p className="empty-state">No workflows configured yet.</p>
      ) : (
        <ul className="workflow-list">
          {workflows.map((wf) => (
            <li key={wf.id} className="workflow-item">
              <div className="workflow-info">
                <div className="workflow-name">
                  {wf.customName || wf.template?.name || 'Unnamed Workflow'}
                </div>
                <div className="workflow-meta">
                  Last run: {wf.lastRunAt ? new Date(wf.lastRunAt).toLocaleDateString() : 'Never'}
                </div>
              </div>
              <Badge status={wf.status} />
            </li>
          ))}
        </ul>
      )}
    </Card>
  );
}
```

### 8.3 `AgentList.tsx`

Displays active AI agents:

```tsx
// apps/web/src/components/dashboard/AgentList.tsx
import React from 'react';
import type { TenantAgent } from '@lib/types';
import Card from '@components/ui/Card';
import Badge from '@components/ui/Badge';

interface Props {
  agents: TenantAgent[];
}

export default function AgentList({ agents }: Props) {
  return (
    <Card title="AI Agents">
      {agents.length === 0 ? (
        <p className="empty-state">No agents deployed yet.</p>
      ) : (
        <ul className="agent-list">
          {agents.map((agent) => (
            <li key={agent.id} className="agent-item">
              <div className="agent-info">
                <div className="agent-name">
                  {agent.customName || agent.template?.name || 'Unnamed Agent'}
                </div>
                <div className="agent-category">{agent.template?.category || 'GENERAL'}</div>
              </div>
              <Badge status={agent.status} />
            </li>
          ))}
        </ul>
      )}
    </Card>
  );
}
```

### 8.4 `ApprovalList.tsx`

Shows pending approvals:

```tsx
// apps/web/src/components/dashboard/ApprovalList.tsx
import React from 'react';
import type { Approval } from '@lib/types';
import Card from '@components/ui/Card';
import Button from '@components/ui/Button';

interface Props {
  approvals: Approval[];
}

export default function ApprovalList({ approvals }: Props) {
  const handleApprove = (id: string) => {
    console.log('Approve:', id);
    // TODO: Call API to approve
  };

  const handleReject = (id: string) => {
    console.log('Reject:', id);
    // TODO: Call API to reject
  };

  return (
    <Card title="Pending Approvals">
      <ul className="approval-list">
        {approvals.map((appr) => (
          <li key={appr.id} className="approval-item">
            <div className="approval-info">
              <div className="approval-desc">{appr.description}</div>
              <div className="approval-meta">
                {appr.type} • {new Date(appr.createdAt).toLocaleDateString()}
              </div>
            </div>
            <div className="approval-actions">
              <Button variant="primary" onClick={() => handleApprove(appr.id)}>
                Approve
              </Button>
              <Button variant="secondary" onClick={() => handleReject(appr.id)}>
                Reject
              </Button>
            </div>
          </li>
        ))}
      </ul>
    </Card>
  );
}
```

---

## 9. Reusable UI Components

### 9.1 `Card.tsx`

```tsx
// apps/web/src/components/ui/Card.tsx
import React, { type ReactNode } from 'react';

interface Props {
  title?: string;
  children: ReactNode;
  className?: string;
}

export default function Card({ title, children, className = '' }: Props) {
  return (
    <div className={`card ${className}`}>
      {title && <h3 className="card-title">{title}</h3>}
      <div className="card-content">{children}</div>
    </div>
  );
}
```

### 9.2 `Badge.tsx`

```tsx
// apps/web/src/components/ui/Badge.tsx
import React from 'react';

interface Props {
  status: string;
}

const statusColors: Record<string, string> = {
  ACTIVE: 'green',
  PAUSED: 'yellow',
  ERROR: 'red',
  PENDING: 'blue',
  APPROVED: 'green',
  REJECTED: 'red',
};

export default function Badge({ status }: Props) {
  const color = statusColors[status] || 'gray';
  return (
    <span className={`badge badge-${color}`}>
      {status}
    </span>
  );
}
```

### 9.3 `Button.tsx`

```tsx
// apps/web/src/components/ui/Button.tsx
import React, { type ReactNode } from 'react';

interface Props {
  children: ReactNode;
  variant?: 'primary' | 'secondary' | 'danger';
  onClick?: () => void;
  disabled?: boolean;
}

export default function Button({
  children,
  variant = 'primary',
  onClick,
  disabled = false,
}: Props) {
  return (
    <button
      className={`btn btn-${variant}`}
      onClick={onClick}
      disabled={disabled}
    >
      {children}
    </button>
  );
}
```

---

## 10. Global Styles (`styles/global.css`)

A minimal dark-mode design system:

```css
/* apps/web/src/styles/global.css */

:root {
  --color-bg: #0f0f0f;
  --color-surface: #1a1a1a;
  --color-border: #333;
  --color-text: #fff;
  --color-text-muted: #aaa;
  --color-primary: #3b82f6;
  --color-primary-hover: #2563eb;
  --color-secondary: #6b7280;
  --color-danger: #ef4444;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background: var(--color-bg);
  color: var(--color-text);
}

/* Card */
.card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: 8px;
  padding: 1.5rem;
}

.card-title {
  font-size: 1.125rem;
  font-weight: 600;
  margin-bottom: 1rem;
}

.card-content {
  font-size: 0.875rem;
}

/* Badge */
.badge {
  display: inline-block;
  padding: 0.25rem 0.75rem;
  border-radius: 12px;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
}

.badge-green {
  background: #10b98144;
  color: #10b981;
}

.badge-yellow {
  background: #f59e0b44;
  color: #f59e0b;
}

.badge-red {
  background: #ef444444;
  color: #ef4444;
}

.badge-blue {
  background: #3b82f644;
  color: #3b82f6;
}

/* Button */
.btn {
  padding: 0.5rem 1rem;
  border-radius: 6px;
  border: none;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-primary {
  background: var(--color-primary);
  color: #fff;
}

.btn-primary:hover {
  background: var(--color-primary-hover);
}

.btn-secondary {
  background: var(--color-secondary);
  color: #fff;
}

.btn-secondary:hover {
  background: #4b5563;
}

.btn-danger {
  background: var(--color-danger);
  color: #fff;
}

.btn-danger:hover {
  background: #dc2626;
}

.btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* Lists */
.workflow-list,
.agent-list,
.approval-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.workflow-item,
.agent-item,
.approval-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.75rem;
  background: #1e1e1e;
  border: 1px solid var(--color-border);
  border-radius: 6px;
}

.workflow-name,
.agent-name,
.approval-desc {
  font-weight: 500;
}

.workflow-meta,
.agent-category,
.approval-meta {
  font-size: 0.75rem;
  color: var(--color-text-muted);
  margin-top: 0.25rem;
}

.approval-actions {
  display: flex;
  gap: 0.5rem;
}

/* Metrics */
.overview-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.metric-value {
  font-size: 2.5rem;
  font-weight: 700;
  color: var(--color-primary);
  margin-bottom: 0.5rem;
}

.metric-label {
  font-size: 0.875rem;
  color: var(--color-text-muted);
}

.change-budget {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.budget-row {
  display: flex;
  justify-content: space-between;
  font-size: 0.875rem;
}

.empty-state {
  color: var(--color-text-muted);
  font-style: italic;
}
```

---

## 11. Vercel Configuration (`vercel.json`)

At the root of `apps/web`:

```json
{
  "buildCommand": "pnpm build",
  "outputDirectory": "dist",
  "framework": "astro"
}
```

Vercel auto-detects Astro projects, but this ensures clarity.

---

## 12. Local Development Workflow

1. Set `PUBLIC_API_URL` in `.env`:

   ```env
   PUBLIC_API_URL=http://localhost:3000/api
   ```

2. Ensure the API (`apps/api`) is running on `localhost:3000`.

3. Start the web app:

   ```bash
   cd apps/web
   pnpm dev
   ```

4. Open `http://localhost:4321` (default Astro port).

5. Navigate to `/dashboard/{tenantId}` using a seeded tenant ID.

---

## 13. Build Acceptance Checklist (Build 1)

Before marking Build 1 complete:

- [ ] `/dashboard/[tenantId]` route renders without errors.
- [ ] Header displays current user name from `/api/me`.
- [ ] Sidebar renders navigation links.
- [ ] `SnapshotOverview` displays metric cards (even if zeroed out).
- [ ] `WorkflowList` and `AgentList` show empty states when no data.
- [ ] Page layout is responsive and visually matches the dark-mode design system.
- [ ] No console errors related to missing types or API failures.

---

## 14. Future Enhancements (Build 2+)

- **Real-time updates:** Add WebSocket or polling for live metrics refresh.
- **Charts:** Integrate Chart.js or Recharts for visual trend graphs.
- **Filtering & search:** Add controls to filter workflows/agents by status or category.
- **Modal dialogs:** Use `Modal.tsx` for approval actions and config edits.
- **Authentication:** Replace `/api/me` stub with real Supabase Auth or JWT flow.

---

This gives you a complete, opinionated front-end structure that:
- Consumes the API from `apps/api` using the defined snapshot shape.
- Uses Astro for routing and SSR with React islands for interactivity.
- Provides reusable UI components (Card, Badge, Button) matching a consistent design system.
- Is ready to deploy to Vercel alongside the API.

Pair this with `rl-control-center-api-layout-v1.md` and the other v2 docs to have a full Phase 1 implementation blueprint.
