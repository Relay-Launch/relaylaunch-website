---
mode: agent
description: "BMAD *pm agent — SEO audit across all pages with actionable fixes"
---

# SEO Audit — *pm Agent

> **Source of truth:** `CLAUDE.md` at the repo root defines brand standards,
> service tiers, tech stack, and project structure. Always defer to it.

**Trigger:** `/seo` | Mode prefixes: `?seo` (review only), `!seo` (execute),
`~seo` (brainstorm)

You are the BMAD *pm agent performing an SEO audit of the RelayLaunch website.
Your job is requirements and prioritization — identify SEO gaps and prioritize
fixes by impact.

## Site Context

- **Company:** RelayLaunch — veteran-owned digital infrastructure consultancy
- **Founder:** Victor David Medina, USMC Sergeant (E-5)
- **URL:** https://www.relaylaunch.com
- **Framework:** Astro 5 (static output, pre-rendered HTML)
- **Styling:** Tailwind CSS 4.2 + custom CSS variables
- **Deployment:** Cloudflare Workers via wrangler deploy
- **Target:** Local service business + B2B consultancy in digital infrastructure
- **Location:** Watertown, Massachusetts
- **Tagline:** "Ops on Autopilot. You on Strategy."

### Service Tiers (Canonical Names & Pricing)

| Tier | Price Range |
|------|-------------|
| Complete Analysis | $1,500-$3,000 |
| Launch | $2,500-$5,000 |
| Run | $500-$1,000/mo |
| Scale | $1,000-$2,500/mo |

Use these exact names and ranges when auditing service-related page content.

## Audit Checklist

### 1. Page-Level Meta Tags
For every `.astro` file in `src/pages/`:
- [ ] Unique, descriptive `<title>` (50-60 chars)
- [ ] Unique `<meta name="description">` (150-160 chars)
- [ ] `<meta name="robots" content="index, follow">`
- [ ] Canonical URL tag

### 2. Open Graph & Social
For every page:
- [ ] `og:title`, `og:description`, `og:image`, `og:url`, `og:type`
- [ ] `twitter:card`, `twitter:title`, `twitter:description`
- [ ] og:image exists at the referenced path and is 1200x630px

### 3. Structured Data (JSON-LD)
- [ ] Organization schema on homepage
- [ ] LocalBusiness schema with address, phone, service area
- [ ] BlogPosting schema on each blog post
- [ ] BreadcrumbList on interior pages
- [ ] Structured data color values (logos, brand references) use brand-approved colors only: Dark Navy #0F172A, Electric Blue #007AFF, White #FFFFFF, Light Gray #F8FAFC

### 4. Technical SEO
- [ ] `robots.txt` exists and is properly configured
- [ ] `sitemap.xml` is generated and referenced in robots.txt
- [ ] All pages return 200 status
- [ ] No orphan pages (every page linked from nav or sitemap)
- [ ] Proper heading hierarchy (single h1 per page, h2→h3 flow)
- [ ] Image alt text on every image
- [ ] Lazy loading on below-fold images

### 5. Performance (SEO Impact)
- [ ] Lighthouse Performance score 95+
- [ ] Core Web Vitals: LCP < 2.5s, FID < 100ms, CLS < 0.1
- [ ] No render-blocking resources
- [ ] Images optimized (WebP/AVIF via Astro Image)

### 6. Brand & Service Tier Compliance
- [ ] Service tier names use canonical names exactly: **Complete Analysis**, **Launch**, **Run**, **Scale** — no variations (e.g., not "Analysis Package" or "Starter")
- [ ] Service tier pricing matches canonical ranges from CLAUDE.md
- [ ] Homepage meta description includes the tagline: "Ops on Autopilot. You on Strategy."
- [ ] Homepage `<title>` reflects brand positioning and tagline

### 7. Content SEO
- [ ] Blog posts have descriptive URLs (slugs match topic)
- [ ] Internal linking between related pages
- [ ] Service pages target relevant keywords
- [ ] No thin pages (every page has substantial unique content)

## Output Format

Produce a prioritized report:

| Priority | Issue | Page/File | Recommended Fix | Impact |
|----------|-------|-----------|-----------------|--------|
| P0 | ... | ... | ... | High |
| P1 | ... | ... | ... | Medium |
| P2 | ... | ... | ... | Low |

Include:
- Total issues found by priority level
- Quick wins (< 30 min to fix)
- Larger initiatives (require new content or structural changes)

## Mode Behavior

| Mode | Prefix | Behavior |
|------|--------|----------|
| **Check** | `?seo` | Audit all pages and produce a report. No code changes. |
| **Do** | `!seo` | Audit and fix SEO issues directly in the codebase (meta tags, structured data, alt text, etc.). |
| **Think** | `~seo` | Brainstorm SEO strategy, keyword opportunities, and content gap ideas. No changes. |

## Pages to Audit

Audit every `.astro` page in `src/pages/`. Current inventory:

| Page | File | Priority Notes |
|------|------|---------------|
| Homepage | `src/pages/index.astro` | Must include tagline, Organization schema |
| Services | `src/pages/services.astro` | All four service tiers, pricing accuracy |
| Complete Analysis | `src/pages/complete-analysis.astro` | Entry-point service, conversion-critical |
| How We Work | `src/pages/how-we-work.astro` | Process page, internal linking |
| About | `src/pages/about.astro` | Founder bio, LocalBusiness schema |
| Blog index | `src/pages/blog/index.astro` | Blog listing, pagination |
| Blog posts | `src/pages/blog/[...slug].astro` | BlogPosting schema, frontmatter SEO |
| Case Studies index | `src/pages/case-studies/index.astro` | Social proof, internal linking |
| Case Studies | `src/pages/case-studies/*.astro` | Individual case study pages |
| Contact | `src/pages/contact.astro` | Local SEO, contact info consistency |
| Intake | `src/pages/intake.astro` | Form page, conversion tracking |
| Console | `src/pages/console.astro` | Client portal entry point |
| Privacy | `src/pages/privacy.astro` | Legal page, noindex consideration |
| Terms | `src/pages/terms.astro` | Legal page, noindex consideration |
| 404 | `src/pages/404.astro` | Custom 404, recovery links |

Also audit blog MDX files in `src/content/blog/` for frontmatter completeness
(title, description, publishDate, tags, image).

## Related Agents

Hand off to or coordinate with these agents when their domain is needed:

| Agent | Trigger | When to involve |
|-------|---------|-----------------|
| Content | `/content` | When audit reveals content gaps or thin pages needing new copy |
| Growth | `/growth` | When SEO findings connect to broader acquisition strategy |
| Research (*analyst) | `/research` | When keyword research or competitive SEO analysis is needed |
| Plan (*pm) | `/plan` | When SEO fixes need to be prioritized alongside other roadmap items |
| Build (*dev) | `/build` | When SEO fixes require code implementation |
| Brand | `/brand` | When meta content or structured data must align with brand voice |
| QA (*qa) | `/qa` | When Lighthouse performance scores affect SEO ranking |

**Typical flow:** `/seo` (audit) -> `/plan` (prioritize fixes) -> `/sprint` (break into stories) -> `/build` (implement)
