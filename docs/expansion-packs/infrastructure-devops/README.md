# Infrastructure & DevOps Expansion Pack — The Relay Method™

Adapted from the [BMAD Infrastructure & DevOps Expansion Pack](https://github.com/bmadcode/BMAD-METHOD-v5/tree/main/expansion-packs/bmad-infrastructure-devops) for the RelayLaunch stack.

## What This Pack Adds

- **Infrastructure Validation Checklist** — 16-section pre-deployment gate
- **Architecture Template** — Infrastructure architecture design document
- **Validation Task** — Step-by-step infrastructure review workflow

## RelayLaunch Stack Context

This pack is tuned for our production stack:
- **Hosting:** Cloudflare Workers (static + edge compute)
- **DNS:** Cloudflare (zone: relaylaunch.com)
- **CI/CD:** GitHub Actions → wrangler deploy
- **Framework:** Astro 5 + Tailwind CSS 4.2
- **Registrar:** Porkbun
- **Email:** Google Workspace (MX via Porkbun forwarding)

## Integration Points

| Phase | When It Runs | What It Does |
|-------|-------------|--------------|
| Post-Architecture | After `/architect` | Generates infrastructure architecture doc |
| Parallel to Dev | During `/build` | Validates infra changes alongside code |
| Pre-Deployment | During `/ship` gate | Runs infrastructure validation checklist |

## How to Use

- `/infra` — Activate the Infra Agent with this pack's context
- `?ops` — Audit infrastructure without changes
- `!ops` — Fix infrastructure issues
- `/relay deploy` — Full deployment with infrastructure validation

## Files

| File | Purpose |
|------|---------|
| `checklists/infrastructure-checklist.md` | 16-section validation checklist |
| `templates/infrastructure-architecture.md` | Architecture design template |
| `tasks/validate-infrastructure.md` | Validation workflow task |
