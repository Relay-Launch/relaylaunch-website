#!/bin/bash
# Script to delete stale branches from the repository
# Run this script to clean up old Claude, Codex, and Copilot branches

echo "🧹 Cleaning up stale branches..."
echo ""
echo "This will delete the following branches:"
echo "  - claude/aesthetic-website-improvements (merged)"
echo "  - claude/fix-website-404-error"
echo "  - claude/fix-website-404-error-FCUaw"
echo "  - claude/improve-slow-code-efficiency"
echo "  - claude/normalize-project-structure-gxRuZ"
echo "  - claude/optimize-website-deployment"
echo "  - claude/update-astro-pages-workflow"
echo "  - codex/fix-404-error-website"
echo "  - codex/update-astro-github-pages-workflow"
echo "  - copilot/fix-404-error-on-website"
echo "  - copilot/fix-404-error-website"
echo "  - copilot/fix-github-actions-deployment"
echo "  - copilot/update-astro-github-pages-workflow"
echo "  - copilot/update-astro-workflow"
echo "  - copilot/update-custom-url-for-branch"
echo ""
read -p "Continue? (y/N) " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]
then
    # Delete branches
    gh api -X DELETE repos/Relay-Launch/relaylaunch-website/git/refs/heads/claude/aesthetic-website-improvements 2>/dev/null && echo "✅ Deleted claude/aesthetic-website-improvements" || echo "⚠️  Could not delete claude/aesthetic-website-improvements"
    gh api -X DELETE repos/Relay-Launch/relaylaunch-website/git/refs/heads/claude/fix-website-404-error 2>/dev/null && echo "✅ Deleted claude/fix-website-404-error" || echo "⚠️  Could not delete claude/fix-website-404-error"
    gh api -X DELETE repos/Relay-Launch/relaylaunch-website/git/refs/heads/claude/fix-website-404-error-FCUaw 2>/dev/null && echo "✅ Deleted claude/fix-website-404-error-FCUaw" || echo "⚠️  Could not delete claude/fix-website-404-error-FCUaw"
    gh api -X DELETE repos/Relay-Launch/relaylaunch-website/git/refs/heads/claude/improve-slow-code-efficiency 2>/dev/null && echo "✅ Deleted claude/improve-slow-code-efficiency" || echo "⚠️  Could not delete claude/improve-slow-code-efficiency"
    gh api -X DELETE repos/Relay-Launch/relaylaunch-website/git/refs/heads/claude/normalize-project-structure-gxRuZ 2>/dev/null && echo "✅ Deleted claude/normalize-project-structure-gxRuZ" || echo "⚠️  Could not delete claude/normalize-project-structure-gxRuZ"
    gh api -X DELETE repos/Relay-Launch/relaylaunch-website/git/refs/heads/claude/optimize-website-deployment 2>/dev/null && echo "✅ Deleted claude/optimize-website-deployment" || echo "⚠️  Could not delete claude/optimize-website-deployment"
    gh api -X DELETE repos/Relay-Launch/relaylaunch-website/git/refs/heads/claude/update-astro-pages-workflow 2>/dev/null && echo "✅ Deleted claude/update-astro-pages-workflow" || echo "⚠️  Could not delete claude/update-astro-pages-workflow"
    gh api -X DELETE repos/Relay-Launch/relaylaunch-website/git/refs/heads/codex/fix-404-error-website 2>/dev/null && echo "✅ Deleted codex/fix-404-error-website" || echo "⚠️  Could not delete codex/fix-404-error-website"
    gh api -X DELETE repos/Relay-Launch/relaylaunch-website/git/refs/heads/codex/update-astro-github-pages-workflow 2>/dev/null && echo "✅ Deleted codex/update-astro-github-pages-workflow" || echo "⚠️  Could not delete codex/update-astro-github-pages-workflow"
    git push origin --delete copilot/fix-404-error-on-website 2>/dev/null && echo "✅ Deleted copilot/fix-404-error-on-website" || echo "⚠️  Could not delete copilot/fix-404-error-on-website"
    git push origin --delete copilot/fix-404-error-website 2>/dev/null && echo "✅ Deleted copilot/fix-404-error-website" || echo "⚠️  Could not delete copilot/fix-404-error-website"
    git push origin --delete copilot/fix-github-actions-deployment 2>/dev/null && echo "✅ Deleted copilot/fix-github-actions-deployment" || echo "⚠️  Could not delete copilot/fix-github-actions-deployment"
    git push origin --delete copilot/update-astro-github-pages-workflow 2>/dev/null && echo "✅ Deleted copilot/update-astro-github-pages-workflow" || echo "⚠️  Could not delete copilot/update-astro-github-pages-workflow"
    git push origin --delete copilot/update-astro-workflow 2>/dev/null && echo "✅ Deleted copilot/update-astro-workflow" || echo "⚠️  Could not delete copilot/update-astro-workflow"
    git push origin --delete copilot/update-custom-url-for-branch 2>/dev/null && echo "✅ Deleted copilot/update-custom-url-for-branch" || echo "⚠️  Could not delete copilot/update-custom-url-for-branch"

    echo ""
    echo "✨ Cleanup complete!"
else
    echo "❌ Cancelled"
fi
