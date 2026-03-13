# RelayLaunch Website – Architecture Document (v1)

This document describes the technical architecture of the RelayLaunch marketing website for AI agents and human developers.

---

## 1. System Overview

The RelayLaunch website is a **static-first marketing site** built with Astro 5. It generates static HTML at build time and deploys to Cloudflare Workers for global edge delivery.

```text
┌──────────────────────────────────────────────────────────┐
│                    Cloudflare CDN                         │
│  ┌────────────────────────────────────────────────────┐  │
│  │            Cloudflare Workers                       │  │
│  │  ┌──────────────────────────────────────────────┐  │  │
│  │  │  Astro Static Output (dist/)                 │  │  │
│  │  │  _worker.js/index.js                          │  │  │
│  │  └──────────────────────────────────────────────┘  │  │
│  └────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────┘
         ▲                    ▲
         │                    │
    relaylaunch.com    www.relaylaunch.com
```

---

## 2. Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Framework | Astro 5 | Static site generation, islands architecture |
| Styling | Tailwind CSS 4.2 | Utility-first CSS, CSS variables |
| Design System | Starwind | Button, Toggle, ThemeToggle components |
| Content | MDX | Blog posts via Astro Content Collections |
| Adapter | @astrojs/cloudflare | Cloudflare Workers compatibility |
| Deployment | wrangler | CLI deploy to Cloudflare Workers |
| CI/CD | GitHub Actions | Build, Lighthouse audit, deploy on push to main |
| DNS | Cloudflare | Apex + www routing, SSL, caching |
| Domain | Porkbun | Registrar (nameservers point to Cloudflare) |

---

## 3. Build Pipeline

```text
Developer pushes to main
        │
        ▼
GitHub Actions (.github/workflows/astro.yml)
        │
        ├── npm ci (install deps)
        ├── npm run build (astro build → dist/)
        ├── Verify Cloudflare secrets exist
        └── wrangler deploy (push dist/ to Workers)

PR to main triggers:
        │
        └── Lighthouse CI (.github/workflows/lighthouse.yml)
            ├── Audits 11 pages
            ├── Scores: performance, accessibility, SEO ≥ 90
            └── Posts results as PR comment
```

---

## 4. Page Architecture

### 4.1 Route Map

| Path | File | Description |
|------|------|-------------|
| `/` | `index.astro` | Homepage — hero, services overview, social proof |
| `/services` | `services.astro` | All service tiers |
| `/complete-analysis` | `complete-analysis.astro` | Entry-point diagnostic tier |
| `/about` | `about.astro` | About RelayLaunch and Victor |
| `/contact` | `contact.astro` | Contact information |
| `/how-we-work` | `how-we-work.astro` | Process and methodology |
| `/intake` | `intake.astro` | Client intake form |
| `/blog` | `blog/index.astro` | Blog listing |
| `/blog/[slug]` | `blog/[...slug].astro` | Individual blog posts (MDX) |
| `/case-studies` | `case-studies/index.astro` | Case study listing |
| `/case-studies/[slug]` | `case-studies/*.astro` | Individual case studies |
| `/privacy` | `privacy.astro` | Privacy policy |
| `/terms` | `terms.astro` | Terms of service |
| `/404` | `404.astro` | Custom 404 page |

### 4.2 Layout Hierarchy

```text
Layout.astro (Nav + Footer wrapper)
  └── BaseLayout.astro (SEO head, meta tags)
        └── Page content (.astro files)

BlogPostLayout.astro (extends BaseLayout with blog-specific markup)
  └── MDX blog post content
```

### 4.3 Component Architecture

```text
src/components/
  ├── Nav.astro              # Global navigation (responsive, mobile menu)
  ├── Footer.astro           # Global footer (links, contact, copyright)
  ├── Breadcrumbs.astro      # Breadcrumb navigation for inner pages
  ├── ArchitectureDiagram.astro  # Visual architecture diagram
  ├── ServiceIcons.astro     # Service tier icon components
  ├── seo/
  │   └── SEO.astro          # Meta tags, OG tags, structured data
  ├── layouts/
  │   ├── BaseLayout.astro   # HTML head, body wrapper
  │   └── BlogPostLayout.astro  # Blog post wrapper
  └── starwind/              # Starwind design system
      ├── button/Button.astro
      ├── toggle/Toggle.astro
      └── theme-toggle/ThemeToggle.astro
```

---

## 5. Styling Architecture

### 5.1 Design Token System

All design tokens are defined as CSS custom properties in `src/styles/global.css`:

```css
/* Brand Colors */
--color-navy: #0F172A;
--color-accent: #007AFF;
--color-white: #FFFFFF;
--color-gray-light: #F8FAFC;

/* Typography */
font-family: Arial, Helvetica, sans-serif;

/* Spacing, borders, shadows — defined as CSS variables */
```

### 5.2 Tailwind Integration

- Tailwind CSS 4.2 is configured via `@tailwindcss/vite` plugin.
- Starwind theme variables in `src/styles/starwind.css`.
- Custom utilities extend Tailwind for brand-specific patterns.

### 5.3 Responsive Breakpoints

| Breakpoint | Width | Target |
|-----------|-------|--------|
| Default | 0px+ | Mobile (single column) |
| `sm` | 640px+ | Large phones, small tablets |
| `md` | 768px+ | Tablets |
| `lg` | 1024px+ | Desktop |

---

## 6. Content System

### 6.1 Blog Posts (MDX)

- Located in `src/content/blog/*.mdx`.
- Schema defined in `src/content.config.ts`.
- Required frontmatter: `title`, `description`, `pubDate`, `author`.
- Rendered through `BlogPostLayout.astro`.
- Utility functions in `src/utils/blog.ts`.

### 6.2 Case Studies

- Static `.astro` pages in `src/pages/case-studies/`.
- Not content-collection driven (manually authored pages).

---

## 7. External Integrations

| Integration | Purpose | Config |
|------------|---------|--------|
| n8n Webhook | Lead magnet capture | `PUBLIC_LEAD_MAGNET_WEBHOOK_URL` |
| Cal.com | Meeting scheduling | `PUBLIC_CAL_LINK` |
| Google Analytics 4 | Production analytics | `PUBLIC_GA_MEASUREMENT_ID` |
| External intake form | Client onboarding | `PUBLIC_INTAKE_FORM_URL` |

All integrations use environment variables. See `.env.example` for the full list.

---

## 8. Performance Targets

| Metric | Target | Enforcement |
|--------|--------|------------|
| Lighthouse Performance | 95+ | CI/CD audit on PRs |
| Lighthouse Accessibility | 95+ | CI/CD audit on PRs |
| Lighthouse SEO | 95+ | CI/CD audit on PRs |
| First Contentful Paint | < 1s | Static generation |
| Total Blocking Time | 0ms | No client-side JS |
| Cumulative Layout Shift | < 0.1 | Lazy-loaded images with dimensions |

---

## 9. Security Considerations

- No server-side rendering in production (static output only).
- No user-generated content or database connections.
- Environment variables are build-time only (`PUBLIC_` prefix).
- Cloudflare provides DDoS protection, SSL, and edge caching.
- CSP headers managed via Cloudflare Workers configuration.

---

## 10. Future Considerations

- Integration with Control Center API for dynamic client dashboard links.
- Webhook contracts for lead capture → Control Center pipeline.
- Shared authentication if client portal links are added to the marketing site.
- See `docs/blueprints/` for cross-repo integration specs.
