# RelayLaunch Control Center – Monorepo Setup & Package Configuration (v1)

This document provides **exact package.json, tsconfig, and tooling setup** for the Control Center monorepo, matching the Node/TS + Vercel Phase 1 architecture.

It is meant to be read alongside:
- `rl-control-center-options-v2.md`
- `rl-control-center-build-framework-v2.md`
- `rl-control-center-api-layout-v1.md`
- `rl-control-center-web-layout-v1.md`
- `rl-control-center-agent-instructions-v1.md`

---

## 1. Monorepo Root Structure

```text
control-center/
  apps/
    api/
    web/
  packages/
    core-models/
    client-sdk/
  infra/
    terraform/
  docs/
  .gitignore
  package.json
  pnpm-workspace.yaml
  tsconfig.base.json
  turbo.json
  README.md
```

### 1.1 Why this structure

- **apps/**: Deployable applications (API + web UI).
- **packages/**: Shared libraries (TypeScript interfaces, SDK helpers).
- **infra/**: Infrastructure-as-code (Terraform for future AWS migration).
- **docs/**: All the v2 spec documents and schemas.

---

## 2. Root `package.json`

```json
{
  "name": "relaylaunch-control-center",
  "version": "1.0.0",
  "private": true,
  "description": "Multi-tenant control center for RelayLaunch client automations and AI agents",
  "author": "Victor David Medina <victor@relaylaunch.com>",
  "license": "UNLICENSED",
  "scripts": {
    "dev": "turbo run dev --parallel",
    "build": "turbo run build",
    "lint": "turbo run lint",
    "test": "turbo run test",
    "clean": "turbo run clean && rm -rf node_modules",
    "typecheck": "turbo run typecheck"
  },
  "devDependencies": {
    "@types/node": "^20.11.0",
    "turbo": "^1.12.0",
    "typescript": "^5.3.3"
  },
  "engines": {
    "node": ">=20.0.0",
    "pnpm": ">=8.0.0"
  },
  "packageManager": "pnpm@8.15.0"
}
```

### 2.1 Key notes

- **Turbo:** Used for fast, cached builds and parallel dev servers.
- **pnpm:** Workspace manager; faster and more efficient than npm/yarn.
- **Node 20+**: Phase 1 targets modern Node LTS.

---

## 3. Workspace Configuration (`pnpm-workspace.yaml`)

```yaml
# pnpm-workspace.yaml
packages:
  - 'apps/*'
  - 'packages/*'
```

This tells pnpm to treat `apps/*` and `packages/*` as workspace members.

---

## 4. Turbo Configuration (`turbo.json`)

```json
{
  "$schema": "https://turbo.build/schema.json",
  "globalDependencies": ["**/.env.*local"],
  "pipeline": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**", ".next/**", ".vercel/**"]
    },
    "dev": {
      "cache": false,
      "persistent": true
    },
    "lint": {
      "outputs": []
    },
    "typecheck": {
      "dependsOn": ["^typecheck"],
      "outputs": []
    },
    "test": {
      "dependsOn": ["^build"],
      "outputs": ["coverage/**"]
    },
    "clean": {
      "cache": false
    }
  }
}
```

### 4.1 Pipeline explanation

- **build**: Runs builds in dependency order (e.g., `core-models` before `api`).
- **dev**: Runs dev servers without caching (for live reload).
- **lint/typecheck**: Standard quality checks.
- **test**: Future-ready for Jest/Vitest.

---

## 5. Base TypeScript Config (`tsconfig.base.json`)

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "lib": ["ES2020"],
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "allowSyntheticDefaultImports": true,
    "esModuleInterop": true,
    "strict": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true
  },
  "exclude": ["node_modules", "dist", ".next", ".vercel", "coverage"]
}
```

This is extended by all workspace packages for consistent compiler settings.

---

## 6. Root `.gitignore`

```gitignore
# Dependencies
node_modules/
.pnpm-store/

# Build outputs
dist/
.next/
.vercel/
.turbo/

# Environment
.env
.env.local
.env.*.local

# Logs
*.log
npm-debug.log*
pnpm-debug.log*

# OS
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/
*.swp
*.swo

# Prisma
prisma/migrations/**/migration.sql.bak

# Test coverage
coverage/
```

---

## 7. `apps/api/package.json`

```json
{
  "name": "@control-center/api",
  "version": "1.0.0",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "tsx watch src/server.ts",
    "build": "tsc && tsc-alias",
    "start": "node dist/server.js",
    "typecheck": "tsc --noEmit",
    "lint": "eslint src --ext .ts",
    "prisma:generate": "prisma generate",
    "prisma:migrate": "prisma migrate dev",
    "prisma:studio": "prisma studio",
    "clean": "rm -rf dist"
  },
  "dependencies": {
    "@prisma/client": "^5.9.0",
    "express": "^4.18.2",
    "serverless-http": "^3.2.0"
  },
  "devDependencies": {
    "@types/express": "^4.17.21",
    "@types/node": "^20.11.0",
    "eslint": "^8.56.0",
    "prisma": "^5.9.0",
    "tsc-alias": "^1.8.8",
    "tsx": "^4.7.0",
    "typescript": "^5.3.3"
  }
}
```

### 7.1 Key dependencies

- **express**: Minimal Node.js web framework.
- **@prisma/client**: Generated DB client.
- **serverless-http**: Adapter for Vercel serverless functions.
- **tsx**: Fast TypeScript execution for dev mode.
- **tsc-alias**: Resolves TS path aliases in build output.

---

## 8. `apps/web/package.json`

```json
{
  "name": "@control-center/web",
  "version": "1.0.0",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "astro dev",
    "build": "astro build",
    "preview": "astro preview",
    "typecheck": "astro check && tsc --noEmit",
    "lint": "eslint src --ext .ts,.tsx,.astro",
    "clean": "rm -rf dist .astro"
  },
  "dependencies": {
    "@astrojs/react": "^3.0.9",
    "@astrojs/vercel": "^6.1.0",
    "astro": "^4.2.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "@types/react": "^18.2.48",
    "@types/react-dom": "^18.2.18",
    "eslint": "^8.56.0",
    "typescript": "^5.3.3"
  }
}
```

### 8.1 Key dependencies

- **astro**: Static-site generator with SSR support.
- **@astrojs/react**: Enables React islands.
- **@astrojs/vercel**: Vercel serverless adapter for Astro.

---

## 9. `packages/core-models/package.json`

Shared TypeScript types/interfaces used by both API and web:

```json
{
  "name": "@control-center/core-models",
  "version": "1.0.0",
  "private": true,
  "main": "./dist/index.js",
  "types": "./dist/index.d.ts",
  "scripts": {
    "build": "tsc",
    "typecheck": "tsc --noEmit",
    "clean": "rm -rf dist"
  },
  "devDependencies": {
    "typescript": "^5.3.3"
  }
}
```

### 9.1 Structure

```text
packages/core-models/
  src/
    index.ts
    tenant.ts
    user.ts
    workflow.ts
    agent.ts
    metrics.ts
    approval.ts
    change-request.ts
  tsconfig.json
  package.json
```

**Example `src/index.ts`:**

```ts
export * from './tenant';
export * from './user';
export * from './workflow';
export * from './agent';
export * from './metrics';
export * from './approval';
export * from './change-request';
```

**Example `src/tenant.ts`:**

```ts
export type TenantPlan = 'STARTER' | 'PROFESSIONAL' | 'ENTERPRISE';

export interface Tenant {
  id: string;
  name: string;
  domain: string;
  plan: TenantPlan;
  status: 'ACTIVE' | 'SUSPENDED' | 'TRIAL';
  createdAt: string;
  subscriptionEndsAt: string | null;
}
```

All other files follow the same pattern from `rl-control-center-data-model-v2.md`.

---

## 10. `packages/core-models/tsconfig.json`

```json
{
  "extends": "../../tsconfig.base.json",
  "compilerOptions": {
    "outDir": "dist",
    "rootDir": "src",
    "composite": true
  },
  "include": ["src"],
  "exclude": ["node_modules", "dist"]
}
```

---

## 11. `packages/client-sdk/package.json` (Optional)

Typed HTTP client for consuming the API (if you want a shared SDK):

```json
{
  "name": "@control-center/client-sdk",
  "version": "1.0.0",
  "private": true,
  "main": "./dist/index.js",
  "types": "./dist/index.d.ts",
  "scripts": {
    "build": "tsc",
    "typecheck": "tsc --noEmit",
    "clean": "rm -rf dist"
  },
  "dependencies": {
    "@control-center/core-models": "workspace:*"
  },
  "devDependencies": {
    "typescript": "^5.3.3"
  }
}
```

**Example `src/index.ts`:**

```ts
import type { Tenant, TenantSnapshot, User } from '@control-center/core-models';

export class ControlCenterClient {
  constructor(private baseUrl: string) {}

  async getMe(): Promise<{ user: User }> {
    const res = await fetch(`${this.baseUrl}/me`);
    if (!res.ok) throw new Error(`API error: ${res.status}`);
    return res.json();
  }

  async getTenant(id: string): Promise<{ tenant: Tenant }> {
    const res = await fetch(`${this.baseUrl}/tenants/${id}`);
    if (!res.ok) throw new Error(`API error: ${res.status}`);
    return res.json();
  }

  async getTenantSnapshot(id: string): Promise<TenantSnapshot> {
    const res = await fetch(`${this.baseUrl}/tenants/${id}/snapshot`);
    if (!res.ok) throw new Error(`API error: ${res.status}`);
    return res.json();
  }
}
```

This lets both `apps/web` and any future mobile/CLI apps import a single SDK.

---

## 12. Environment Variable Setup

### 12.1 `apps/api/.env.example`

```env
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/control_center

# Node environment
NODE_ENV=development
```

Copy to `.env` and fill in your Supabase connection string.

### 12.2 `apps/web/.env.example`

```env
# API endpoint
PUBLIC_API_URL=http://localhost:3000/api
```

Copy to `.env` for local dev, or set in Vercel for production.

---

## 13. Installation & First-Run Commands

From the monorepo root:

```bash
# Install all dependencies
pnpm install

# Generate Prisma client
cd apps/api
pnpm prisma:generate
pnpm prisma:migrate

# Seed initial data (optional script)
# pnpm prisma db seed

# Start all apps in dev mode
cd ../..
pnpm dev
```

This will:
- Start the API on `http://localhost:3000`
- Start the web app on `http://localhost:4321`

---

## 14. Deployment Checklist (Vercel)

### 14.1 API deployment

1. Create a new Vercel project linked to `apps/api`.
2. Set **Root Directory** to `apps/api`.
3. Add environment variables:
   - `DATABASE_URL` → Supabase production connection string
   - `NODE_ENV` → `production`
4. Deploy. Vercel will auto-detect the `vercel.json` and use `@vercel/node`.

### 14.2 Web deployment

1. Create a new Vercel project linked to `apps/web`.
2. Set **Root Directory** to `apps/web`.
3. Add environment variable:
   - `PUBLIC_API_URL` → `https://your-api.vercel.app/api`
4. Deploy. Vercel will auto-detect Astro and use the serverless adapter.

---

## 15. Future Migration Notes (AWS Phase 2)

When moving to AWS:
- The `packages/core-models` and `client-sdk` remain unchanged.
- `apps/api` will be refactored to run on Lambda or ECS, using the same Prisma models.
- `apps/web` can stay on Vercel or move to S3 + CloudFront.
- Add Terraform configs to `infra/terraform/` for RDS, Lambda, API Gateway, etc.

The monorepo structure is designed to make this transition low-friction.

---

## 16. Summary

This document provides:
- Exact `package.json` files for root, API, web, and shared packages.
- TypeScript, Turbo, pnpm workspace configs.
- Environment variable templates.
- Install and deploy commands.

Combined with the other v2 docs, you now have a **complete blueprint** for setting up and building the Control Center monorepo from scratch.

Agents should reference this when scaffolding new packages or updating dependencies.
