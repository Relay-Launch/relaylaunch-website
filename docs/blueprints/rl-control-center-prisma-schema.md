# RelayLaunch Control Center – Prisma Schema (v1)

This document provides a **Prisma schema** that matches `rl-control-center-data-model-v2.md` and is designed for:
- **Supabase Postgres** in Phase 1 (Vercel API)
- Easy migration to AWS RDS Postgres in Phase 2

You can copy the `schema.prisma` block directly into your API project under `apps/api/prisma/schema.prisma`.

---

## 1. schema.prisma

```prisma
// schema.prisma – RelayLaunch Control Center
// Phase 1: Supabase Postgres, Node.js + TypeScript API on Vercel

generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

// -----------------------------
// Core Models
// -----------------------------

model Tenant {
  id          String   @id @default(cuid())
  slug        String   @unique
  name        String

  primaryContact Json
  plan          Plan
  status        TenantStatus @default(ACTIVE)

  branding        Json?
  n8n             Json
  aws             Json?
  metricsConfig   Json
  changeAllowances Json
  featureFlags    Json

  users           User[]
  workflows       TenantWorkflow[]
  agents          TenantAgent[]
  tenantMetrics   TenantDailyMetrics[]
  approvals       Approval[]
  changeRequests  ChangeRequest[]

  createdAt    DateTime @default(now())
  updatedAt    DateTime @updatedAt
}

model User {
  id        String   @id @default(cuid())
  email     String   @unique
  name      String
  role      UserRole
  status    UserStatus @default(ACTIVE)

  tenantId  String?
  tenant    Tenant?   @relation(fields: [tenantId], references: [id])

  approvalsApproved Approval[] @relation("ApprovalApprovedBy")
  changeRequests    ChangeRequest[] @relation("ChangeRequestCreatedBy")

  lastLoginAt DateTime?
  createdAt   DateTime @default(now())
  updatedAt   DateTime @updatedAt
}

// -----------------------------
// Workflows
// -----------------------------

model WorkflowTemplate {
  id                     String            @id @default(cuid())
  key                    String            @unique
  name                   String
  category               WorkflowCategory
  shortDescription       String
  longDescription        String
  n8nTemplateId          String?
  docsUrl                String?
  defaultHoursSavedPerRun Float

  tenantWorkflows        TenantWorkflow[]

  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
}

model TenantWorkflow {
  id                 String           @id @default(cuid())
  tenantId           String
  workflowTemplateId String

  displayName        String
  status             WorkflowStatus   @default(ON)
  n8nWorkflowId      String
  lastRunAt          DateTime?
  config             Json

  tenant             Tenant           @relation(fields: [tenantId], references: [id])
  template           WorkflowTemplate @relation(fields: [workflowTemplateId], references: [id])
  metrics            WorkflowDailyMetrics[]

  changeRequests     ChangeRequest[]  @relation("ChangeRequestWorkflow")

  createdAt          DateTime @default(now())
  updatedAt          DateTime @updatedAt
}

// -----------------------------
// Agents
// -----------------------------

model AgentTemplate {
  id                         String         @id @default(cuid())
  key                        String         @unique
  name                       String
  category                   AgentCategory
  roleType                   AgentRoleType
  shortTagline               String
  longDescription            String
  iconRef                    String
  toolsUsed                  String[]
  defaultInputs              String[]
  defaultOutputs             String[]
  estimatedHoursSavedPerMonth Float
  docsUrl                    String?

  tenantAgents               TenantAgent[]

  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
}

model TenantAgent {
  id            String        @id @default(cuid())
  tenantId      String
  agentTemplateId String

  status        AgentStatus   @default(ACTIVE)
  displayName   String
  config        Json
  lastRunAt     DateTime?

  runsLast30Days               Int      @default(0)
  estimatedHoursSavedLast30Days Float   @default(0)

  tenant        Tenant        @relation(fields: [tenantId], references: [id])
  template      AgentTemplate @relation(fields: [agentTemplateId], references: [id])

  changeRequests ChangeRequest[] @relation("ChangeRequestAgent")

  createdAt     DateTime @default(now())
  updatedAt     DateTime @updatedAt
}

// -----------------------------
// Metrics
// -----------------------------

model TenantDailyMetrics {
  id             String   @id @default(cuid())
  tenantId       String
  date           DateTime

  leadsCaptured  Int      @default(0)
  automationsRun Int      @default(0)
  hoursSaved     Float    @default(0)
  marketing      Json?

  tenant         Tenant   @relation(fields: [tenantId], references: [id])

  createdAt      DateTime @default(now())

  @@unique([tenantId, date])
}

model WorkflowDailyMetrics {
  id                String          @id @default(cuid())
  tenantWorkflowId  String
  date              DateTime

  runsSuccess       Int             @default(0)
  runsFailed        Int             @default(0)
  hoursSaved        Float           @default(0)

  workflow          TenantWorkflow  @relation(fields: [tenantWorkflowId], references: [id])

  createdAt         DateTime @default(now())

  @@unique([tenantWorkflowId, date])
}

// -----------------------------
// Approvals & Change Requests
// -----------------------------

model Approval {
  id                String         @id @default(cuid())
  tenantId          String
  agentOrWorkflowId String?

  type              ApprovalType
  status            ApprovalStatus @default(PENDING)

  payload           Json

  requestedAt       DateTime @default(now())
  approvedAt        DateTime?

  approvedByUserId  String?
  approvedBy        User?   @relation("ApprovalApprovedBy", fields: [approvedByUserId], references: [id])

  rejectionReason   String?

  tenant            Tenant @relation(fields: [tenantId], references: [id])

  createdAt         DateTime @default(now())
  updatedAt         DateTime @updatedAt
}

model ChangeRequest {
  id                   String           @id @default(cuid())
  tenantId             String
  createdByUserId      String?

  type                 ChangeType
  status               ChangeStatus    @default(OPEN)

  affectedWorkflowId   String?
  affectedAgentId      String?

  title                String
  description          String
  priority             ChangePriority  @default(NORMAL)
  internalEstimatedHours Float         @default(0)
  countsAgainstAllowance Boolean       @default(true)

  createdAt            DateTime @default(now())
  updatedAt            DateTime @updatedAt
  completedAt          DateTime?

  tenant               Tenant @relation(fields: [tenantId], references: [id])
  createdBy            User?  @relation("ChangeRequestCreatedBy", fields: [createdByUserId], references: [id])

  workflow             TenantWorkflow? @relation("ChangeRequestWorkflow", fields: [affectedWorkflowId], references: [id])
  agent                TenantAgent?    @relation("ChangeRequestAgent", fields: [affectedAgentId], references: [id])
}

// -----------------------------
// Enums
// -----------------------------

enum Plan {
  LAUNCH
  RUN
  SCALE
}

enum TenantStatus {
  ACTIVE
  PAUSED
  PROSPECT
  OFFBOARDED
}

enum UserRole {
  OWNER
  MEMBER
  ADMIN
}

enum UserStatus {
  ACTIVE
  INVITED
  DISABLED
}

enum WorkflowCategory {
  LEADS
  SALES
  BILLING
  OPERATIONS
  MARKETING
  ADMIN
}

enum WorkflowStatus {
  ON
  OFF
  DRAFT
}

enum AgentCategory {
  MARKETING
  SALES
  FINANCE
  OPS
  INFRA
  DESIGN
  DEV
}

enum AgentRoleType {
  BUSINESS
  JOB_HELPER
}

enum AgentStatus {
  ACTIVE
  PAUSED
  PLANNED
}

enum ApprovalType {
  EMAIL
  SOCIAL_POST
  OFFER
  AUTOMATION_ACTION
}

enum ApprovalStatus {
  PENDING
  APPROVED
  REJECTED
  EXECUTED
}

enum ChangeType {
  SMALL
  MEDIUM
  NEW
}

enum ChangeStatus {
  OPEN
  IN_PROGRESS
  COMPLETED
  DEFERRED
  REJECTED
}

enum ChangePriority {
  NORMAL
  HIGH
}
```

---

## 2. Notes & Conventions

- All IDs are `String @id @default(cuid())` for simplicity in serverless environments.
- `Json` fields correspond directly to the JSONB structures described in `rl-control-center-data-model-v2.md`.
- Enum names map to the logical types in the data‑model doc (Plan, WorkflowCategory, etc.).
- Relationships are explicitly named (`@relation("ChangeRequestWorkflow")`, etc.) to keep Prisma from guessing relation names.

After placing this file, run:

```bash
pnpm prisma migrate dev --name init_control_center
pnpm prisma generate
```

This will create the schema in Supabase (or any Postgres) and generate a fully typed Prisma Client for your Node/TypeScript API on Vercel.