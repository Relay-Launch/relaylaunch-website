#!/bin/bash
# Manual deployment script for GitHub Pages
# Use this script only if you need to manually deploy the site
# Normally, the workflow handles this automatically

set -e

echo "🚀 Manual Deployment to GitHub Pages"
echo "===================================="
echo ""

# Check if we're in the right directory
if [ ! -f "package.json" ]; then
  echo "❌ Error: Must be run from repository root"
  exit 1
fi

# Check if we have a clean working directory
if [ -n "$(git status --porcelain)" ]; then
  echo "⚠️  Warning: You have uncommitted changes"
  read -p "Continue anyway? (y/n) " -n 1 -r
  echo
  if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    exit 1
  fi
fi

echo "📦 Installing dependencies..."
npm ci

echo "🔨 Building site..."
npm run build

echo "📁 Checking build output..."
if [ ! -f "dist/index.html" ]; then
  echo "❌ Error: Build failed - dist/index.html not found"
  exit 1
fi

if [ ! -f "dist/CNAME" ]; then
  echo "❌ Error: CNAME file missing from build output"
  exit 1
fi

echo "✅ Build successful"
echo ""
echo "🌐 Deploying to gh-pages branch..."

cd dist

# Initialize git in dist folder
git init
git config user.email "github-actions[bot]@users.noreply.github.com"
git config user.name "github-actions[bot]"

# Add all files and commit
git add -A
git commit -m "Deploy site — $(date -u '+%Y-%m-%d %H:%M:%S UTC')"

# Add remote and push
git remote add origin "https://github.com/Relay-Launch/relaylaunch-website.git"

echo ""
echo "⚠️  IMPORTANT: This will force push to the gh-pages branch"
read -p "Continue? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
  cd ..
  rm -rf dist/.git
  exit 1
fi

# Push to gh-pages
if git push --force origin HEAD:gh-pages; then
  cd ..
  rm -rf dist/.git
  echo ""
  echo "✅ Deployment successful!"
  echo ""
  echo "Next steps:"
  echo "1. Go to https://github.com/Relay-Launch/relaylaunch-website/settings/pages"
  echo "2. Under 'Source', select 'Deploy from a branch'"
  echo "3. Select branch 'gh-pages' and folder '/ (root)'"
  echo "4. Under 'Custom domain', enter: relaylaunch.com"
  echo "5. Wait 2-3 minutes for the site to deploy"
  echo "6. Visit https://relaylaunch.com to verify"
else
  echo "❌ Deployment failed"
  cd ..
  rm -rf dist/.git
  exit 1
fi
