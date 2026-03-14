# Operational Recommendations

Items that require external service access or admin permissions.
These cannot be automated via code changes alone.

## 1. GitHub Branch Protection Rules (HIGH PRIORITY)

Set up branch protection on `main` via GitHub Settings > Branches:

- [x] Require pull request reviews before merging (1 reviewer minimum)
- [x] Require status checks to pass (build, security audit, Lighthouse)
- [x] Require branches to be up to date before merging
- [x] Do not allow bypassing the above settings

```bash
# Or via GitHub CLI:
gh api repos/Relay-Launch/relaylaunch-website/branches/main/protection \
  -X PUT \
  -f required_status_checks='{"strict":true,"contexts":["Build and deploy to Cloudflare","CodeQL analysis","Dependency audit","Lighthouse Audit"]}' \
  -f enforce_admins=true \
  -f required_pull_request_reviews='{"required_approving_review_count":1}'
```

## 2. Uptime Monitoring (MEDIUM PRIORITY)

Set up external uptime monitoring for https://www.relaylaunch.com

**Option A: Cloudflare Health Checks** (free, already in ecosystem)
- Dashboard > Traffic > Health Checks
- Monitor: `https://www.relaylaunch.com` (GET, expect 200)
- Check interval: 60 seconds
- Alert via email: hello@relaylaunch.com

**Option B: UptimeRobot** (free tier, 5-minute intervals)
- Monitor type: HTTP(s)
- URL: https://www.relaylaunch.com
- Monitoring interval: 5 minutes
- Alert contacts: hello@relaylaunch.com

**Recommended pages to monitor:**
- https://www.relaylaunch.com/ (homepage)
- https://www.relaylaunch.com/services/ (services)
- https://www.relaylaunch.com/contact/ (contact — critical for leads)

## 3. Error Rate Alerting (MEDIUM PRIORITY)

Cloudflare Workers observability is already enabled in wrangler.jsonc.

Set up alerts in Cloudflare Dashboard:
- Dashboard > Notifications > Create
- Alert type: Workers Health Alert
- Condition: Error rate > 5% over 5 minutes
- Notify: hello@relaylaunch.com

Additional recommended alerts:
- Workers CPU time exceeded (> 10ms average)
- Workers request rate anomaly (> 200% of baseline)

## 4. SRI Hashes for External Scripts (LOW PRIORITY)

Neither Google Analytics nor Cal.com currently publish stable SRI hashes.
Both serve dynamic/versioned content from their CDNs.

**Action items:**
- Monitor Cal.com documentation for SRI support
- Monitor Google Analytics documentation for SRI support
- Consider self-hosting the Cal.com embed script if SRI is critical

## 5. Founder Photo (LOW PRIORITY)

The about page references a `founder-photo-placeholder` CSS class but
no actual photo is displayed.

**Action:** Add a professional headshot to `/public/images/` and
update `/src/pages/about.astro` to display it.

## 6. Blog Content Expansion (LOW PRIORITY)

Currently 5 blog posts. For SEO authority building, aim for:
- 2 posts/month minimum
- Target keywords: "small business automation", "AI operations",
  "digital infrastructure consulting"
- Mix of case study breakdowns, thought leadership, and how-to guides
