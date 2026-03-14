# Blueprints — AI-Assisted Development

Architecture documents, specifications, and reference materials for AI coding
tools (Claude Code, GitHub Copilot, Cursor) working in the RelayLaunch
codebase.

## How to Use

Point your AI tool at this folder before starting a build session:

- **Claude Code:** Reference files directly or use `@docs/blueprints`
- **GitHub Copilot:** Files are indexed automatically via workspace context
- **Any AI tool:** Upload or reference documents at session start

**Rule:** Upload first, build second. The AI builds better when it reads the spec before writing code.

---

## Document Index

### Website (This Repo)

Documents covering the architecture, standards, and workflows for the
`relaylaunch-website` marketing site.

| Document | Version | Description |
|----------|---------|-------------|
| `rl-website-agent-instructions-v1.md` | v1 | Rules for AI agents working on this repo — start here |
| `rl-website-architecture-v1.md` | v1 | Technical architecture, component map, deployment pipeline |
| `rl-website-build-framework-v1.md` | v1 | Development workflow, quality gates, content operations |
| `rl-site-audit-v1.md` | v1 | Homepage alignment audit against Control Center positioning |
| `rl-slogan-system-v1.md` | v1 | Brand messaging system, taglines, section headers |
| `rl-trigger-system-v1.md` | v1 | Mode + Domain trigger system, Ship Gate, Prose Agent spec |

### Control Center (Cross-Repo Context)

Documents describing the `relaylaunch-control-center` repo. Stored here so
AI tools working on the website have full cross-repo context for integration
work.

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

Documents that apply across both repos and the overall RelayLaunch business.

| Document | Version | Description |
|----------|---------|-------------|
| `rl-service-playbook-v1.md` | v1 | Service delivery playbook (Discovery to Build to Run) |
| `relaylaunch-market-landscape-v1.md` | v1 | Market research, competitive landscape, sizing |
| `rl-agent-frameworks-v1.md` | v1 | Agent framework overview and installation guide |

---

## Versioning

Documents use a `-v1`, `-v2` suffix. When proposing changes to a spec:

1. Do **not** edit an existing versioned document silently
2. Create a new version (e.g., `rl-website-architecture-v2.md`) explaining changes
3. Wait for human approval before treating the new version as canonical

---

## Source of Truth

| Domain | Owned By |
|--------|----------|
| Brand standards, service tiers, public messaging, agent registry | Website repo |
| Data model, API contracts, Prisma schema, monorepo config | Control Center repo |
| Market landscape, service playbook | Shared (pick one repo as canonical, copy to the other) |

For shared documents, note at the top of each copy which repo holds the
canonical version.

---

## Tips

1. **Upload first, build second** — add specs before asking the AI to implement
2. **Be specific** — include acceptance criteria, edge cases, examples
3. **Keep docs current** — update blueprints when requirements change
4. **Reference in prompts** — tell the AI to "read `docs/blueprints/[file]` first"
5. **Cross-link repos** — note the counterpart when a feature spans both repos
6. **Use the right agent** — check [`docs/agents.md`](../agents.md) to match the task to a specialist
