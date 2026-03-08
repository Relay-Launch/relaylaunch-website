# Website Deployment Setup Guide

## Current Status

🔴 **Website is NOT live** - The Relay Launch website at `relaylaunch.com` is currently showing a 404 error because GitHub Pages has not been properly configured.

## Root Cause

The deployment workflow (`astro.yml`) exists and is correctly configured, but it has **never run** because GitHub Pages source is not set to "GitHub Actions" in the repository settings. This is a **one-time manual configuration step** that must be performed by a repository administrator.

## Verification Results

✅ **Build System**: Working perfectly
- The website builds successfully locally
- All pages generate correctly
- CNAME file is properly included in the build output
- No build errors or warnings

✅ **Workflow Configuration**: Correct
- `.github/workflows/astro.yml` is properly configured
- Supports both GitHub Actions and branch-based deployment
- Pushes to `gh-pages` branch as a fallback

❌ **GitHub Pages Configuration**: Not Enabled
- Pages source is not configured
- Workflow has never been triggered (0 runs)
- Website is inaccessible

## Required Actions

### Step 1: Enable GitHub Pages (REQUIRED - Repository Admin Only)

A repository administrator must complete this one-time setup:

1. Go to **[Repository Settings → Pages](https://github.com/Relay-Launch/relaylaunch-website/settings/pages)**

2. Under "Build and deployment" → **Source**:
   - Select **"GitHub Actions"** from the dropdown

3. Under **Custom domain**:
   - Enter: `relaylaunch.com`
   - Click **Save**

4. Once DNS validation passes:
   - Check **"Enforce HTTPS"**

### Step 2: Verify DNS Configuration

Ensure your domain registrar has one of these configurations:

**Option A: A Records (Apex Domain)**
```
Type: A
Name: @
Value: 185.199.108.153

Type: A
Name: @
Value: 185.199.109.153

Type: A
Name: @
Value: 185.199.110.153

Type: A
Name: @
Value: 185.199.111.153
```

**Option B: CNAME (www subdomain)**
```
Type: CNAME
Name: www
Value: relay-launch.github.io
```

### Step 3: Trigger First Deployment

After enabling Pages in Step 1, trigger the workflow:

**Option A: Merge this PR**
- Merging this PR to `main` will automatically trigger the deployment workflow

**Option B: Manual Trigger**
1. Go to **[Actions → Deploy Astro site to Pages](https://github.com/Relay-Launch/relaylaunch-website/actions/workflows/astro.yml)**
2. Click **"Run workflow"**
3. Select branch: `main`
4. Click **"Run workflow"**

### Step 4: Verify Deployment

After the workflow completes:

1. Check workflow status: [Actions tab](https://github.com/Relay-Launch/relaylaunch-website/actions)
2. Visit `https://relaylaunch.com` (allow up to 10 minutes for first deployment)
3. Verify all pages load correctly

## Troubleshooting

### "domain already taken by another repository"

If you see this error when setting the custom domain, it means another repository (likely `Relay-Launch/.github`) has claimed `relaylaunch.com`:

**Fix:**
1. Go to [github.com/Relay-Launch/.github](https://github.com/Relay-Launch/.github)
2. Check if there's a `CNAME` file in the root
3. Delete that `CNAME` file
4. Return to this repository's Pages settings
5. Enter `relaylaunch.com` and save

### Workflow not running after merge

If the workflow doesn't run after merging to `main`:

1. Verify Pages source is set to "GitHub Actions" (Step 1)
2. Manually trigger the workflow (Step 3, Option B)
3. Check Actions tab for any errors

### Website shows 404 after successful deployment

1. Verify DNS records are correct (Step 2)
2. Wait 24-48 hours for DNS propagation
3. Try accessing via `https://relay-launch.github.io/relaylaunch-website/` to verify the build is deployed
4. Check Pages settings to ensure custom domain is saved

## Technical Details

### Workflow Behavior

The `astro.yml` workflow:
- Triggers on every push to `main`
- Builds the Astro site
- Pushes to `gh-pages` branch (for branch-based deployment fallback)
- Also uploads artifact for GitHub Actions deployment
- Supports both deployment methods simultaneously

### File Locations

- **Workflow**: `.github/workflows/astro.yml`
- **CNAME**: `public/CNAME` (gets copied to `dist/CNAME` during build)
- **Build output**: `dist/` directory
- **Site config**: `astro.config.mjs` (site URL set to `https://relaylaunch.com`)

## Summary

The website code and build system are **100% ready**. The only blocker is the **one-time manual GitHub Pages configuration** in the repository settings, which requires repository administrator access.

Once Step 1 is completed, the website will be live within minutes.
