# Infrastructure Change Validation Checklist — RelayLaunch

Use this checklist before any production deployment or infrastructure change.
Adapted from BMAD Infrastructure & DevOps Expansion Pack for the RelayLaunch stack.

---

## 1. Security & Compliance

- [ ] API tokens scoped to minimum permissions (Workers Edit, Workers Routes Edit, Zone Read, DNS Edit)
- [ ] No secrets in source code, environment variables, or build output
- [ ] CSP headers configured and validated
- [ ] HTTPS enforced on all routes (Cloudflare automatic)
- [ ] DKIM/DMARC/SPF records intact after DNS changes
- [ ] Dependencies scanned for known CVEs (`npm audit`)
- [ ] No sensitive data in client-side JavaScript bundles

## 2. Infrastructure as Code

- [ ] `wrangler.jsonc` changes are intentional and reviewed
- [ ] GitHub Actions workflow syntax validates (`astro.yml`)
- [ ] Environment variables documented in CLAUDE.md or `.env.example`
- [ ] Custom domain configuration matches production (relaylaunch.com + www)
- [ ] Cloudflare Zone ID unchanged unless migrating

## 3. Resilience & Availability

- [ ] Cloudflare Workers deployment succeeds on both custom domains
- [ ] Static assets cached at edge (Cloudflare CDN)
- [ ] No single point of failure in build pipeline
- [ ] Fallback behavior defined for edge cases (404, 500)

## 4. Backup & Recovery

- [ ] Git history preserved (no force-pushes to main)
- [ ] Previous deployment rollback path documented
- [ ] DNS records backed up before changes
- [ ] Email routing (MX records) verified after DNS changes

## 5. Monitoring & Observability

- [ ] Cloudflare Analytics accessible and tracking
- [ ] Build status visible in GitHub Actions
- [ ] Error pages return proper HTTP status codes
- [ ] Core Web Vitals measurable (Lighthouse CI or manual)

## 6. Performance & Optimization

- [ ] Lighthouse scores 95+ across all categories
- [ ] Sub-1-second page load verified
- [ ] No render-blocking resources introduced
- [ ] Images optimized through Astro Image pipeline
- [ ] Bundle size checked — no unnecessary JS shipped

## 7. Operations & Governance

- [ ] CLAUDE.md updated if stack or config changed
- [ ] agents.md updated if new agents or triggers added
- [ ] Conventional commit messages used
- [ ] PR description documents all infrastructure changes

## 8. CI/CD & Deployment

- [ ] `npm run build` passes locally before push
- [ ] GitHub Actions workflow runs successfully
- [ ] Wrangler deploy targets correct Workers project
- [ ] Custom domains resolve correctly post-deploy
- [ ] No deployment secrets exposed in logs

## 9. Networking & DNS

- [ ] Cloudflare nameservers unchanged (lindsey.ns, steven.ns)
- [ ] Apex and www records point to Workers custom domains
- [ ] MX records intact (fwd1/fwd2.porkbun.com + smtp.google.com)
- [ ] No CNAME conflicts with Workers custom domains
- [ ] TTL values appropriate for the change type

## 10. Cross-Repo Coordination

- [ ] Changes compatible with relaylaunch-control-center if applicable
- [ ] Shared data models or API contracts updated in both repos
- [ ] Blueprint documents updated in `docs/blueprints/`
- [ ] Cross-repo sync spec followed (`docs/blueprints/cross-repo-sync.md`)

## 11. Brand Compliance Gate

- [ ] No new colors introduced outside 4-color system
- [ ] Font stack unchanged (Arial, Helvetica, sans-serif)
- [ ] Voice guidelines followed in any new copy
- [ ] Prose Agent scan clean (no AI-isms)

## 12. Accessibility Gate

- [ ] WCAG AA compliance maintained
- [ ] Heading hierarchy preserved (h1 → h2 → h3)
- [ ] Alt text on all images
- [ ] Focus states on interactive elements
- [ ] Color contrast ratios meet minimum thresholds

---

## Pre-Deploy Summary

- [ ] All 12 sections reviewed
- [ ] No critical issues remaining
- [ ] `/ship` gate ready to run
