# 🚨 ACTION REQUIRED: Website 404 Error Fix

## Current Status
**The website at relaylaunch.com is showing a 404 error because it has never been deployed.**

## Root Cause
The GitHub Pages deployment workflow (`astro.yml`) exists and works correctly, but it has **never run** because:
1. GitHub Pages is not enabled in repository settings
2. The workflow only triggers on pushes to the `main` branch
3. This requires a **one-time manual configuration by a repository administrator**

## ✅ What's Working
- ✅ Website builds successfully (verified locally)
- ✅ All pages generate correctly
- ✅ CNAME file is properly configured
- ✅ Workflow configuration is correct
- ✅ DNS settings appear to be configured

## 🔧 Required Actions

### Option 1: Enable GitHub Pages (RECOMMENDED - 2 minutes)

**This is the proper, permanent solution:**

1. **Go to Repository Settings → Pages**
   https://github.com/Relay-Launch/relaylaunch-website/settings/pages

2. **Under "Build and deployment" → Source:**
   - Select: **"GitHub Actions"**

3. **Under "Custom domain":**
   - Enter: `relaylaunch.com`
   - Click **Save**

4. **Trigger the workflow (choose one):**
   - **Option A**: Merge PR #32 to `main` (this will auto-trigger deployment)
   - **Option B**: Manually trigger the workflow:
     1. Go to https://github.com/Relay-Launch/relaylaunch-website/actions/workflows/astro.yml
     2. Click "Run workflow"
     3. Select branch: `main`
     4. Click "Run workflow"

5. **Wait 2-3 minutes** for deployment to complete

6. **Visit https://relaylaunch.com** to verify the site is live

---

### Option 2: Manual Deployment Script (Alternative - 5 minutes)

**Use this only if you need the site live immediately and cannot wait for the workflow:**

```bash
# From repository root:
./scripts/manual-deploy.sh
```

This script will:
1. Build the site locally
2. Push the built site to the `gh-pages` branch
3. Require you to then configure Pages to deploy from the `gh-pages` branch

**After running the script, you still need to:**
1. Go to https://github.com/Relay-Launch/relaylaunch-website/settings/pages
2. Under "Source", select **"Deploy from a branch"**
3. Select branch: **gh-pages** and folder: **/ (root)**
4. Enter custom domain: `relaylaunch.com`
5. Click Save

---

## ⚠️ Important Notes

### Why the workflow hasn't run:
The workflow configuration is correct, but it only triggers when:
- Code is pushed to the `main` branch, OR
- The workflow is manually triggered

Since GitHub Pages was never enabled, and the workflow was never triggered, the site was never deployed.

### After fixing:
- Future pushes to `main` will automatically deploy the site
- No further manual action will be needed
- The site will stay up-to-date automatically

### Troubleshooting:
- **"Domain already taken" error**: Another repository may be claiming `relaylaunch.com`. Check `Relay-Launch/.github` for a CNAME file and remove it.
- **404 after deployment**: Wait 5-10 minutes for DNS propagation. Try accessing via `https://relay-launch.github.io/relaylaunch-website/` to verify the build deployed.
- **Workflow not running**: Verify Pages source is set to "GitHub Actions" in settings.

---

## Timeline
- **Manual setup**: 2-3 minutes to enable + 2-3 minutes for first deployment = **5 minutes total**
- **Script method**: 5 minutes to run script + manual configuration = **10 minutes total**

---

## Questions?
See the complete setup guide in `DEPLOYMENT_SETUP.md` or contact the repository administrator.

---

## Technical Details

### Verified Components:
- ✅ `public/CNAME` contains `relaylaunch.com`
- ✅ `astro.config.mjs` site URL is `https://relaylaunch.com`
- ✅ `.github/workflows/astro.yml` workflow is correctly configured
- ✅ Build generates `dist/CNAME` correctly
- ✅ Build generates all pages successfully
- ✅ Workflow supports both GitHub Actions and branch-based deployment

### What the workflow does:
1. Builds the Astro site
2. Pushes to `gh-pages` branch (fallback for branch-based deployment)
3. Uploads artifact for GitHub Actions deployment
4. Deploys via actions/deploy-pages if Pages source is set to "GitHub Actions"
