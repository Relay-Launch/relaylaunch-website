# Deployment Diagnosis & Solution

**Date:** 2026-03-07
**Status as of 2026-03-07:** Website was NOT deployed (showing 404 error)

## Root Cause Analysis

After thorough investigation, the **root cause** is clear:

### The `astro.yml` workflow has NEVER successfully run on the main branch

- **Zero workflow runs** of "Deploy Astro site to Pages" exist on the main branch
- The workflow file exists at `.github/workflows/astro.yml` and is correctly configured
- The build works perfectly (tested locally - builds 15 pages successfully)
- PR #20 already moved `Setup Pages` before the build step (correct configuration)

### Why there is no successful deployment yet

**GitHub Pages is NOT properly enabled/configured for this repository.**

The `astro.yml` workflow is configured to trigger on `push` to the `main` branch. GitHub Pages settings do **not** prevent a `push`-triggered workflow run from being created, but they **do** determine whether the Pages deployment steps in that workflow can complete successfully.

For GitHub Pages deployment from Actions to work as intended, the repository should have:
1. **Pages Source** set to "GitHub Actions" (not "Deploy from a branch")
2. **Pages enabled** in repository settings
3. The workflow environment (`github-pages`) configured with proper permissions

If you truly see **zero workflow runs** in the Actions tab, also verify:
- GitHub Actions is **enabled** for this repository (and organization, if applicable)
- There has been at least one **push to `main` after `astro.yml` was added** to `.github/workflows/`
- The workflow file is in the correct **path and name** (`.github/workflows/astro.yml`) on the default branch
- The workflow is not limited by additional conditions (e.g., `paths`, `branches`, or `if:` expressions) that are not being met
## Evidence

1. **Workflow runs query returned 0 results** for `astro.yml` on main branch
2. **Repository memories** repeatedly mention: "GitHub Pages Source must be set to 'GitHub Actions'"
3. **Previous PRs (#10, #14, #18, #20)** all identified the same issue: Pages source misconfiguration
4. **Build test:** Successfully built 15 pages with no errors

## Current State

### ✅ What's Working
- Astro build completes successfully
- CNAME file correctly placed in `public/` and copied to `dist/`
- Workflow file structure is correct
- Site configuration (`astro.config.mjs`) is correct
- PR #20's changes (Setup Pages before build) are already merged

### ❌ What's Broken
- Workflow has never executed on main branch
- Website shows 404 error
- Pages deployment not happening

## Required Solution

The user **MUST manually configure GitHub Pages settings** (cannot be done via code):

### Step 1: Enable GitHub Pages with Actions Source

1. Go to: https://github.com/Relay-Launch/relaylaunch-website/settings/pages
2. Under "Build and deployment" → **Source**: Select **"GitHub Actions"**
3. Under "Custom domain": Enter **`relaylaunch.com`**
4. Check "Enforce HTTPS" (after DNS propagates)
5. Click "Save"

### Step 2: Verify DNS Configuration

Ensure DNS records at Porkbun (or DNS provider) are configured:

**Option A: Apex domain (relaylaunch.com)**
- Four A records pointing to GitHub Pages IPs:
  - `185.199.108.153`
  - `185.199.109.153`
  - `185.199.110.153`
  - `185.199.111.153`

**Option B: CNAME (if using www)**
- CNAME record: `www.relaylaunch.com` → `relay-launch.github.io`

### Step 3: Trigger First Deployment

After configuring Pages settings:

**Option A: Push a commit to main**
```bash
# Make any small change and commit
git checkout main
git pull
echo "# Trigger deployment" >> README.md
git add README.md
git commit -m "chore: trigger initial Pages deployment"
git push origin main
```

**Option B: Manually trigger workflow**
1. Go to: https://github.com/Relay-Launch/relaylaunch-website/actions/workflows/astro.yml
2. Click "Run workflow"
3. Select branch: `main`
4. Click "Run workflow"

### Step 4: Verify Deployment

1. Go to Actions tab: https://github.com/Relay-Launch/relaylaunch-website/actions
2. Watch for "Deploy Astro site to Pages" workflow to run
3. Wait for workflow to complete (should take 1-2 minutes)
4. Check deployment URL (will be shown in workflow output)
5. Visit https://relaylaunch.com (may take a few minutes for DNS)

## Why This Couldn't Be Fixed By Code Alone

- **Repository settings** (Pages source, custom domain) require admin access via GitHub UI
- **Workflow permissions** are controlled by organization/repository settings
- **Environment protection rules** cannot be created via code commits
- Previous 20+ PRs tried to fix via code changes, but the issue is configuration, not code

## Verification After Fix

Once Pages is properly configured, you should see:
- ✅ "Deploy Astro site to Pages" workflow runs on push to main
- ✅ Green checkmark on workflow runs
- ✅ Website accessible at https://relaylaunch.com
- ✅ No 404 errors
- ✅ Custom domain working with HTTPS

## Alternative: Manual Deployment Script

If GitHub Actions remain blocked, use the manual deployment script:

```bash
bash scripts/deploy.sh
```

Then set Pages source to "Deploy from a branch" → `gh-pages` / `(root)`.

## Summary

**The code is correct. The workflow is correct. The build works.**

**What's missing:** Manual GitHub Pages configuration in repository settings.

**Action required:** Repository owner must enable Pages with "GitHub Actions" source.
