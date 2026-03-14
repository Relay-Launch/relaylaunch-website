# Infrastructure Architecture — [Project/Feature Name]

> Template from BMAD Infrastructure & DevOps Expansion Pack, adapted for RelayLaunch.

## 1. Overview

**Purpose:** [What infrastructure problem does this solve?]
**Scope:** [What systems are affected?]
**Owner:** [Who is responsible?]

## 2. Current State

| Component | Current Config | Notes |
|-----------|---------------|-------|
| Hosting | Cloudflare Workers | Static + edge compute |
| DNS | Cloudflare (Zone: relaylaunch.com) | Nameservers: lindsey.ns, steven.ns |
| CI/CD | GitHub Actions → wrangler deploy | `.github/workflows/astro.yml` |
| Framework | Astro 5 + Tailwind CSS 4.2 | Static output, islands architecture |
| Registrar | Porkbun | Domain: relaylaunch.com |
| Email | Google Workspace | MX via Porkbun forwarding |

## 3. Proposed Changes

### What Changes

[Describe the infrastructure changes]

### Why

[Business justification and technical rationale]

### Architecture Diagram

```
[ASCII diagram of the proposed infrastructure]
```

## 4. Security Considerations

- [ ] Secrets management approach defined
- [ ] Access scoping reviewed
- [ ] CSP impact assessed
- [ ] Dependency security checked

## 5. Performance Impact

- [ ] Expected load time impact: [faster/same/slower]
- [ ] CDN caching strategy: [unchanged/modified]
- [ ] Bundle size impact: [smaller/same/larger]

## 6. Rollback Plan

**If the change fails:**
1. [Step 1 to revert]
2. [Step 2 to revert]
3. [Verification that rollback succeeded]

## 7. Validation

Run the infrastructure checklist: `docs/expansion-packs/infrastructure-devops/checklists/infrastructure-checklist.md`

## 8. Timeline

| Phase | Duration | Gate |
|-------|----------|------|
| Implementation | [X hours/days] | Build passes |
| Testing | [X hours/days] | Checklist passes |
| Deployment | [X minutes] | `/ship` gate |
| Monitoring | 24-48 hours post-deploy | No errors in Cloudflare Analytics |
