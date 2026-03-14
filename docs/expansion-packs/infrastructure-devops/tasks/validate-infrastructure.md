# Task: Validate Infrastructure Changes

> Adapted from BMAD Infrastructure & DevOps Expansion Pack for RelayLaunch.

## Trigger

Run this task when:
- Any `wrangler.jsonc` change is made
- Any `.github/workflows/` file is modified
- DNS or domain configuration is changed
- A new deployment target is added
- `/infra` or `?ops` is triggered

## Workflow

### Step 1: Inventory Changes

List all infrastructure files modified:
- `wrangler.jsonc`
- `.github/workflows/astro.yml`
- DNS records (if applicable)
- Environment variables (if applicable)

### Step 2: Run Checklist

Open `docs/expansion-packs/infrastructure-devops/checklists/infrastructure-checklist.md` and validate each applicable section.

### Step 3: Test Locally

```bash
npm run build          # Verify build passes
npm run preview        # Test with local Cloudflare emulation (wrangler dev)
```

### Step 4: Validate DNS (if changed)

```bash
dig relaylaunch.com A
dig www.relaylaunch.com A
dig relaylaunch.com MX
dig relaylaunch.com TXT
```

### Step 5: Report

Produce a validation report with:
- **Pass/Fail** for each checklist section
- **Risk level** (low/medium/high)
- **Recommendation** (proceed / fix first / block)

## Output

A structured report confirming infrastructure readiness for deployment.
Feeds into the `/ship` gate as the Infra Agent's contribution.
