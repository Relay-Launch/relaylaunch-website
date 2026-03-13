# RelayLaunch Website – Build Framework (v1)

This document defines the development workflow, quality gates, and operational cadence for the RelayLaunch marketing website.

---

## 1. Development Workflow

### 1.1 Local Development

```bash
# Install dependencies
npm ci

# Start dev server (http://localhost:4321)
npm run dev

# Production build (outputs to dist/)
npm run build

# Local Cloudflare preview (build + wrangler dev)
npm run preview
```

### 1.2 Branch Strategy

| Branch | Purpose | Deploy Target |
|--------|---------|--------------|
| `main` | Production-ready code | Cloudflare Workers (auto-deploy) |
| `claude/*` | AI agent feature branches | PR → review → merge to main |
| `feat/*` | Human feature branches | PR → review → merge to main |
| `fix/*` | Bug fix branches | PR → review → merge to main |

All changes go through pull requests. Direct pushes to `main` trigger immediate production deployment.

### 1.3 Commit Convention

Use conventional commits:

```
feat: add new service tier landing page
fix: correct mobile nav overflow on services page
chore: update Astro to 5.x
docs: add website architecture blueprint
style: align CTA button spacing across pages
```

---

## 2. Quality Gates

### 2.1 Pre-Merge Checklist

Every PR must pass:

1. **Build check:** `npm run build` completes with zero errors.
2. **Brand audit:** Only Navy `#0F172A`, Blue `#007AFF`, White `#FFFFFF`, Gray `#F8FAFC`.
3. **No hardcoded values:** CSS uses variables from `global.css`.
4. **Responsive:** Tested at 640px, 768px, 1024px breakpoints.
5. **Accessibility:** Proper heading hierarchy, alt text, focus states.
6. **Conventional commits:** All commit messages follow the convention.

### 2.2 Lighthouse CI (Automated)

The `lighthouse.yml` workflow runs on every PR to `main`:

**Audited pages:**
- `/` (Homepage)
- `/services`
- `/complete-analysis`
- `/about`
- `/contact`
- `/how-we-work`
- `/blog`
- `/case-studies`
- `/intake`
- `/privacy`
- `/terms`

**Thresholds:** 90+ for performance, accessibility, and SEO.

Results are posted as a PR comment with pass/fail scoring.

### 2.3 Adding New Pages to Audits

When creating a new page, add it to the Lighthouse audit list in `.github/workflows/lighthouse.yml` to maintain quality coverage.

---

## 3. Content Operations

### 3.1 Blog Post Workflow

1. Create `.mdx` file in `src/content/blog/`.
2. Add required frontmatter (`title`, `description`, `pubDate`, `author`).
3. Write content using MDX (Markdown + JSX components).
4. Run `npm run build` to verify the post renders correctly.
5. Submit PR and verify blog index page shows the new post.

### 3.2 Case Study Workflow

1. Create `.astro` file in `src/pages/case-studies/`.
2. Use the Layout wrapper and SEO component.
3. Follow the structure of existing case studies.
4. Add to the case studies index page.
5. Add to the Lighthouse audit list.

### 3.3 Service Page Updates

Service pages are critical brand assets. When modifying:

1. Verify service tier names match CLAUDE.md canonical names.
2. Verify pricing matches CLAUDE.md ranges.
3. Run `/audit` to check brand compliance.
4. Test all CTAs and links.

---

## 4. Deployment Pipeline

### 4.1 Production Deploy (Automatic)

```text
Push to main → GitHub Actions → npm ci → npm build → wrangler deploy
```

**Required secrets:**
- `CLOUDFLARE_API_TOKEN` — Workers API access.
- `CLOUDFLARE_ACCOUNT_ID` — Account identifier.

### 4.2 Manual Deploy

```bash
# From local machine (requires wrangler auth)
npm run deploy
```

This runs `astro build && wrangler deploy`.

### 4.3 Rollback

Cloudflare Workers maintains version history. To rollback:
1. Use the Cloudflare dashboard to select a previous deployment.
2. Or push a revert commit to `main` for automatic redeploy.

---

## 5. Environment Variables

| Variable | Purpose | Required |
|----------|---------|----------|
| `PUBLIC_LEAD_MAGNET_WEBHOOK_URL` | n8n webhook for lead capture | Optional |
| `PUBLIC_INTAKE_FORM_URL` | External intake form link | Optional |
| `PUBLIC_GA_MEASUREMENT_ID` | Google Analytics 4 (production only) | Optional |
| `PUBLIC_CAL_LINK` | Cal.com scheduling link | Optional |

All variables use the `PUBLIC_` prefix (Astro build-time only). See `.env.example`.

---

## 6. Working Style for AI Agents

### 6.1 Before Starting Work

1. Read `CLAUDE.md` for brand standards and project context.
2. Read `docs/blueprints/rl-website-agent-instructions-v1.md` for agent rules.
3. Check `docs/blueprints/` for any relevant specs.
4. Run `npm run build` to verify the current state compiles.

### 6.2 During Work

1. Make focused, incremental changes.
2. Verify `npm run build` succeeds after each significant change.
3. Use conventional commit messages.
4. Stay within the 4-color brand system.

### 6.3 After Completing Work

1. Run `npm run build` one final time.
2. Verify no new Lighthouse regressions (check the PR CI results).
3. Summarize all changes in the PR description.
4. Reference any blueprint docs that guided the implementation.

---

## 7. Website Evolution Roadmap

### Current State
- Static marketing site with blog and case studies.
- Complete Analysis as the entry-point service tier.
- Lead capture via n8n webhooks.

### Near-Term
- Homepage alignment with Control Center positioning (see `rl-site-audit-v1.md`).
- Updated messaging system (see `rl-slogan-system-v1.md`).
- Client portal links to Control Center dashboard.

### Future
- API integration with Control Center for dynamic content.
- Client-specific dashboard previews on the marketing site.
- Automated case study generation from Control Center metrics.

See `docs/blueprints/` for detailed specs on upcoming work.
