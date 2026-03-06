#!/usr/bin/env bash
#
# Manual deploy script for relaylaunch.com
#
# Builds the Astro site and pushes the dist/ output to the gh-pages branch.
# Use this as a workaround when GitHub Actions is unavailable.
#
# Usage:
#   bash scripts/deploy.sh
#
# After running, set the GitHub Pages source to:
#   Settings → Pages → Source → Deploy from a branch → gh-pages / (root)
#
set -euo pipefail

DIST_DIR="dist"
DEPLOY_BRANCH="gh-pages"

# Ensure we're at the repo root
cd "$(git rev-parse --show-toplevel)"

echo "==> Installing dependencies..."
npm ci

echo "==> Building site..."
npm run build

# Verify build output exists
if [ ! -d "$DIST_DIR" ]; then
  echo "ERROR: Build output directory '$DIST_DIR' not found." >&2
  exit 1
fi

if [ ! -f "$DIST_DIR/index.html" ]; then
  echo "ERROR: Build output missing index.html — build may have failed." >&2
  exit 1
fi

echo "==> Deploying to branch '$DEPLOY_BRANCH'..."

# Save current branch to restore later
CURRENT_BRANCH="$(git rev-parse --abbrev-ref HEAD)"

# Create a temporary directory for the deploy
TEMP_DIR="$(mktemp -d)"
cp -r "$DIST_DIR"/. "$TEMP_DIR"

# Set up the gh-pages branch
if git show-ref --verify --quiet "refs/heads/$DEPLOY_BRANCH"; then
  git checkout "$DEPLOY_BRANCH"
else
  git checkout --orphan "$DEPLOY_BRANCH"
fi

# Remove all tracked files, then copy in the build output
git rm -rf . 2>/dev/null || true
cp -r "$TEMP_DIR"/. .
rm -rf "$TEMP_DIR"

# Commit and push
git add -A
git commit -m "Deploy site — $(date -u '+%Y-%m-%d %H:%M:%S UTC')" --allow-empty
git push origin "$DEPLOY_BRANCH"

# Return to the original branch
git checkout "$CURRENT_BRANCH"

echo ""
echo "==> Deployed successfully to '$DEPLOY_BRANCH' branch."
echo ""
echo "    Next step: set the GitHub Pages source to"
echo "    Settings → Pages → Source → Deploy from a branch → gh-pages / (root)"
