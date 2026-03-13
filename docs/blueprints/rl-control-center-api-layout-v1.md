# RelayLaunch Control Center – API Project Layout & Starter Patterns (v1)

This document describes **how to structure and initialize the `apps/api` project** for the RelayLaunch Control Center, assuming:

- Node.js + TypeScript
- Prisma + Postgres (Supabase) as defined in `rl-control-center-prisma-schema.md`
- Hosting on **Vercel serverless functions** for Phase 1

It is meant to be read alongside:
- `rl-control-center-options-v2.md`
- `rl-control-center-data-model-v2.md`
- `rl-control-center-build-framework-v2.md`
- `rl-control-center-prisma-schema.md`

---

## 1. Folder & File Structure for `apps/api`

Under the monorepo root:

```text
control-center/
  apps/
    api/
      src/
        env.ts
        server.ts
        routes/
          health.ts
          tenants/
            getTenant.ts
            getSnapshot.ts
          me/
            getMe.ts
      prisma/
        schema.prisma
      package.json
      tsconfig.json
      vercel.json
```

### 1.1 Purpose of key files

- `src/env.ts`
  - Central place to read and validate environment variables (e.g., `DATABASE_URL`).
- `src/server.ts`
  - Creates the Express/Fastify app and wires routes.
- `src/routes/**`
  - One file per endpoint or group of related endpoints.
- `prisma/schema.prisma`
  - Prisma data model (from `rl-control-center-prisma-schema.md`).
- `vercel.json`
  - Vercel configuration to route HTTP paths to specific functions.

---

## 2. Environment Configuration (`env.ts`)

Use a small helper to ensure required env vars exist:

```ts
// apps/api/src/env.ts

function requireEnv(key: string): string {
  const value = process.env[key];
  if (!value) {
    throw new Error(`Missing required env var: ${key}`);
  }
  return value;
}

export const ENV = {
  databaseUrl: requireEnv('DATABASE_URL'),
  nodeEnv: process.env.NODE_ENV ?? 'development',
};
```

In Vercel, set `DATABASE_URL` to the Supabase connection string.

---

## 3. Bootstrapping the Server (`server.ts`)

Use a lightweight Express app. For Vercel, you can either:
- Export individual handlers per route, or
- Export a single `app` wrapped by a Vercel adapter.

Below is a single Express app pattern suitable for Vercel’s `@vercel/node` runtime.

```ts
// apps/api/src/server.ts

import express from 'express';
import type { Request, Response, NextFunction } from 'express';
import { PrismaClient } from '@prisma/client';
import { ENV } from './env';

const prisma = new PrismaClient();

export const app = express();

app.use(express.json());

// Simple request logging for dev
app.use((req: Request, _res: Response, next: NextFunction) => {
  if (ENV.nodeEnv !== 'production') {
    console.log(`[API] ${req.method} ${req.url}`);
  }
  next();
});

// Health route (can be in its own file)
app.get('/api/health', (_req, res) => {
  res.json({ status: 'ok' });
});

// Import route handlers from separate modules
import { registerTenantRoutes } from './routes/tenants';
import { registerMeRoutes } from './routes/me';

registerTenantRoutes(app, prisma);
registerMeRoutes(app, prisma);
```

For Vercel, create an entrypoint that adapts `app`:

```ts
// apps/api/api/index.ts (Vercel entry)

import { app } from '../src/server';
import serverless from 'serverless-http';

export default serverless(app);
```

Vercel will treat `api/index.ts` as the serverless function for all `/api/*` routes.

---

## 4. Tenant Routes

### 4.1 `registerTenantRoutes`

```ts
// apps/api/src/routes/tenants/index.ts

import type { Express } from 'express';
import type { PrismaClient } from '@prisma/client';
import { getTenantHandler } from './getTenant';
import { getSnapshotHandler } from './getSnapshot';

export function registerTenantRoutes(app: Express, prisma: PrismaClient) {
  app.get('/api/tenants/:id', getTenantHandler(prisma));
  app.get('/api/tenants/:id/snapshot', getSnapshotHandler(prisma));
}
```

### 4.2 `getTenant` handler

```ts
// apps/api/src/routes/tenants/getTenant.ts

import type { Request, Response } from 'express';
import type { PrismaClient } from '@prisma/client';

export function getTenantHandler(prisma: PrismaClient) {
  return async (req: Request, res: Response) => {
    const { id } = req.params;

    const tenant = await prisma.tenant.findUnique({ where: { id } });

    if (!tenant) {
      return res.status(404).json({ error: 'Tenant not found' });
    }

    return res.json({ tenant });
  };
}
```

### 4.3 `getSnapshot` handler (stubbed)

```ts
// apps/api/src/routes/tenants/getSnapshot.ts

import type { Request, Response } from 'express';
import type { PrismaClient } from '@prisma/client';

export function getSnapshotHandler(prisma: PrismaClient) {
  return async (req: Request, res: Response) => {
    const { id } = req.params;

    const tenant = await prisma.tenant.findUnique({ where: { id } });

    if (!tenant) {
      return res.status(404).json({ error: 'Tenant not found' });
    }

    // TODO: Replace with real aggregations once metrics are live
    const snapshot = {
      tenant,
      overview: {
        period: 'last_30_days',
        metrics: {
          leadsCaptured: 0,
          automationsRun: 0,
          hoursSaved: 0,
        },
        changeUsage: {
          smallUsed: 0,
          smallAllowed: 6,
          mediumUsed: 0,
          mediumAllowed: 1,
          newUsed: 0,
          newAllowed: 0,
          newAllowedPerQuarter: 1,
        },
        recentActivity: [],
      },
      workflows: [],
      agents: [],
      approvalsPending: [],
    };

    return res.json(snapshot);
  };
}
```

This stub is enough for the front‑end to render a basic snapshot; later you’ll populate workflows, agents, and metrics using the Prisma schema.

---

## 5. `/me` Route

For Phase 1, keep auth simple: return a fixed admin user until you integrate real auth.

```ts
// apps/api/src/routes/me/index.ts

import type { Express } from 'express';
import type { PrismaClient } from '@prisma/client';

export function registerMeRoutes(app: Express, prisma: PrismaClient) {
  app.get('/api/me', async (_req, res) => {
    // For now, just grab the first admin user
    const user = await prisma.user.findFirst({
      where: { role: 'ADMIN' },
      include: { tenant: true },
    });

    if (!user) {
      return res.status(500).json({ error: 'No admin user seeded yet' });
    }

    res.json({ user });
  });
}
```

Later, you can swap this for JWT‑based auth or Supabase auth integration.

---

## 6. Vercel Configuration (`vercel.json`)

At the root of `apps/api`:

```json
{
  "version": 2,
  "builds": [
    { "src": "api/index.ts", "use": "@vercel/node" }
  ],
  "routes": [
    { "src": "/api/(.*)", "dest": "api/index.ts" }
  ]
}
```

In the monorepo root, you can either:
- Configure Vercel to use `apps/api` as a separate project, or
- Use a root‑level `vercel.json` that delegates to this entry.

---

## 7. TypeScript Configuration

A minimal `tsconfig.json` for `apps/api`:

```json
{
  "extends": "../../tsconfig.base.json",
  "compilerOptions": {
    "outDir": "dist",
    "rootDir": "src",
    "module": "commonjs",
    "target": "ES2020",
    "esModuleInterop": true,
    "strict": true
  },
  "include": ["src", "api"],
  "exclude": ["node_modules", "dist"]
}
```

Ensure the monorepo has a `tsconfig.base.json` with shared compiler settings if you prefer.

---

## 8. Local Development Workflow

1. Ensure `DATABASE_URL` points to your local or Supabase Postgres instance.
2. Run Prisma migrations:

   ```bash
   pnpm prisma migrate dev --name init_control_center
   pnpm prisma generate
   ```

3. Start the API locally (e.g., using `ts-node-dev` or `nodemon`):

   ```bash
   pnpm dev
   ```

4. Confirm `GET http://localhost:3000/api/health` returns `{ "status": "ok" }`.
5. Confirm `GET /api/tenants/:id` returns the seeded RelayLaunch tenant.

---

## 9. Production Readiness Checklist (Phase 1)

Before pointing any client data at the Control Center API:

- [ ] All Prisma migrations are checked into git.
- [ ] `DATABASE_URL` in Vercel points to the **production** Supabase instance.
- [ ] There is at least one seeded admin user and one tenant.
- [ ] `GET /api/tenants/:id/snapshot` returns structured, non‑null data for that tenant.
- [ ] Basic logging is in place and doesn’t leak secrets.
- [ ] Error paths return structured `{ error: string }` JSON.

This gives you a clean, opinionated starting point that matches your v2 specs and is easy for agents or collaborators to extend safely.
