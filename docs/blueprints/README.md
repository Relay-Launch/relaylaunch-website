# Blueprints — AI-Assisted Development Resources

This folder contains architecture documents, specifications, and reference
materials that AI coding tools (Claude Code, GitHub Copilot, etc.) should
consult when generating or reviewing code in this repository.

## How It Works

When starting a build session, point your AI tool at this folder:

- **Claude Code:** `@docs/blueprints` or reference files directly
- **GitHub Copilot:** Files here are indexed automatically via workspace context
- **Any AI tool:** Upload or reference these documents at the start of a session

---

## Document Index

### Website-Specific (This Repo)

These documents describe the architecture, standards, and workflows for the
`relaylaunch-website` marketing site.

| Document | Version | Description |
|----------|---------|-------------|
| `rl-website-agent-instructions-v1.md` | v1 | **Start here** — Rules for AI agents working on this repo |
| `rl-website-architecture-v1.md` | v1 | Technical architecture, component map, deployment pipeline |
| `rl-website-build-framework-v1.md` | v1 | Development workflow, quality gates, content operations |
| `rl-site-audit-v1.md` | v1 | Homepage alignment audit against Control Center positioning |
| `rl-slogan-system-v1.md` | v1 | Brand messaging system, taglines, section headers |

### Control Center (Cross-Repo Context)

These documents describe the `relaylaunch-control-center` repo. They are
stored here so AI tools working on the website have full cross-repo context
for integration work.

| Document | Version | Description |
|----------|---------|-------------|
| `cc-readme-v1.md` | v1 | Control Center project overview and README |
| `cc-product-v1.md` | v1 | Product one-pager, target market, pricing |
| `cc-db-seeding-v1.md` | v1 | Database seeding script and demo data |
| `cc-sales-deck-outline-v1.md` | v1 | Sales deck slide structure |
| `rl-control-center-agent-instructions-v1.md` | v1 | AI agent rules for Control Center repo |
| `rl-control-center-data-model-v2.md` | v2 | Canonical data model and API shapes |
| `rl-control-center-build-framework-v2.md` | v2 | 3-build implementation plan |
| `rl-control-center-options-v2.md` | v2 | Tech stack decisions (Phase 1 locked) |
| `rl-control-center-monorepo-setup-v1.md` | v1 | Monorepo configuration (Turbo, pnpm) |
| `rl-control-center-api-layout-v1.md` | v1 | API folder structure and starter routes |
| `rl-control-center-web-layout-v1.md` | v1 | Frontend layout and component plan |
| `rl-control-center-prisma-schema.md` | v1 | Prisma database schema |

### Shared / Strategy

These documents apply to both repos and the overall RelayLaunch business.

| Document | Version | Description |
|----------|---------|-------------|
| `rl-service-playbook-v1.md` | v1 | Service delivery playbook (Discovery → Build → Run) |
| `relaylaunch-market-landscape-v1.md` | v1 | Market research, competitive landscape, sizing |

---

## Versioning Convention

Documents are versioned with a `-v1`, `-v2` suffix. When proposing changes
to a canonical spec:

1. **Do NOT** silently edit an existing versioned document.
2. **Create a new version** (e.g., `rl-website-architecture-v2.md`) that
   explains the proposed changes.
3. Wait for human approval before treating the new version as canonical.

---

## Cross-Repo Context

This repository (`relaylaunch-website`) is the public-facing marketing site.
It works alongside the **Command Center** (`relaylaunch-control-center`),
which is the internal client/operations dashboard.

For shared context between repos, maintain parallel `docs/blueprints/` folders
in both repositories. Documents that define the interface between the two
systems (API contracts, shared data models, webhook specs) should exist in
both repos so each AI tool has full context regardless of which repo it is
working in.

**Source of truth rules:**
- Website repo owns: brand standards, service tier names, public messaging, agent registry
- Control Center repo owns: data model, API contracts, Prisma schema, monorepo config
- Shared: market landscape, service playbook

**Keeping specs in sync:** Pick one repo as the source of truth for each
shared document (typically the repo that owns the domain). Copy the spec
to the other repo and note at the top which repo holds the canonical version.

---

## Tips for Blueprint-Driven Development

1. **Upload first, build second** — Add your specs to this folder before
   asking the AI to implement them
2. **Be specific** — Include acceptance criteria, edge cases, and examples
3. **Keep docs current** — Update blueprints when requirements change
4. **Reference in prompts** — Tell the AI to "read docs/blueprints/[file]
   before implementing"
5. **Cross-link repos** — When a feature spans both repos, note the
   counterpart in each blueprint
6. **Use the right agent** — Check [`docs/agents.md`](../agents.md) to pick
   the best agent for your task before starting
