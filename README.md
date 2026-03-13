# RelayLaunch Website

[![Astro](https://img.shields.io/badge/Astro-5-BC52EE?logo=astro&logoColor=white)](https://astro.build/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-4-06B6D4?logo=tailwindcss&logoColor=white)](https://tailwindcss.com/)
[![Cloudflare Pages](https://img.shields.io/badge/Cloudflare-Pages-F6821F?logo=cloudflare&logoColor=white)](https://pages.cloudflare.com/)
[![MDX](https://img.shields.io/badge/MDX-Blog-1B1F24?logo=mdx&logoColor=white)](https://mdxjs.com/)
[![Lighthouse](https://img.shields.io/badge/Lighthouse-90%2B-4285F4?logo=lighthouse&logoColor=white)](https://developer.chrome.com/docs/lighthouse)

**RelayLaunch LLC** — Digital infrastructure consultancy for small businesses.

[relaylaunch.com](https://relaylaunch.com) · [hello@relaylaunch.com](mailto:hello@relaylaunch.com) · Watertown, MA

---

## About

RelayLaunch replaces the 5–8 disconnected tools most small businesses juggle — website, email, CRM, social, scheduling, analytics, payments — with one integrated system built on real infrastructure. Veteran-owned, Fortune 500 experience, small business budget.

## Service Tiers

| Package | Description | Investment |
|---------|-------------|------------|
| **Complete Analysis** | 8-area business infrastructure diagnostic — 20–30 page report with prioritized roadmap | $1,500–$3,000 |
| **Launch** | One-time full infrastructure build — website, automations, email, social, dashboard | $2,500–$5,000 |
| **Run** | Monthly operations retainer — content, SEO, automation monitoring, strategy calls | $500–$1,000/mo · 3-month min |
| **Scale** | Premium growth retainer — expanded deliverables, priority support, advanced builds | $1,000–$2,500/mo · 6-month min |

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Framework | [Astro 5](https://astro.build/) — static-first, islands architecture |
| Styling | [Tailwind CSS 4.2](https://tailwindcss.com/) + Starwind components |
| Content | MDX blog posts via Astro Content Collections |
| Deployment | [Cloudflare Pages/Workers](https://pages.cloudflare.com/) via `wrangler` |
| CI/CD | GitHub Actions → `wrangler deploy` on push to `main` |
| Quality | Lighthouse CI on PRs — Performance, Accessibility, SEO ≥ 90 |
| Domain | relaylaunch.com — Registrar: Porkbun, DNS: Cloudflare |

## Local Development

```bash
npm ci            # install dependencies (use ci, not install)
npm run dev       # dev server → http://localhost:4321
npm run build     # production build → dist/
npm run preview   # build + wrangler dev (local Cloudflare preview)
```

## Project Structure

```
src/
├── pages/            # Astro page routes
│   ├── index.astro
│   ├── services.astro
│   ├── complete-analysis.astro
│   ├── about.astro
│   ├── contact.astro
│   ├── how-we-work.astro
│   ├── intake.astro
│   ├── 404.astro
│   ├── blog/
│   └── case-studies/
├── components/
│   ├── Nav.astro
│   ├── Footer.astro
│   ├── seo/SEO.astro
│   ├── layouts/      # BaseLayout, BlogPostLayout
│   └── starwind/     # Design system (Button, Toggle, ThemeToggle)
├── content/
│   └── blog/         # MDX blog posts
├── layouts/
│   └── Layout.astro  # Page wrapper (Nav + Footer)
└── styles/
    ├── global.css    # Design tokens + component styles
    └── starwind.css  # Tailwind v4 theme variables
public/
├── favicon.svg
├── og-default.png
└── robots.txt
```

## Deployment

Deployments are fully automated via GitHub Actions.

**Trigger:** Any push to `main`
**Pipeline:** Build Astro → Lighthouse CI → `wrangler deploy` → Cloudflare Pages

```
git push origin main  →  GitHub Actions  →  wrangler deploy  →  relaylaunch.com
```

To deploy manually from your machine:

```bash
npm run deploy   # npm run build + wrangler deploy
```

### Environment Variables

Set in Cloudflare Pages dashboard or `.env` locally (see `.env.example`):

| Variable | Purpose |
|----------|---------|
| `PUBLIC_GA_MEASUREMENT_ID` | Google Analytics 4 measurement ID |
| `PUBLIC_LEAD_MAGNET_WEBHOOK_URL` | n8n webhook for lead magnet form |
| `PUBLIC_CONTACT_WEBHOOK_URL` | n8n webhook for Complete Analysis booking form |

## Brand Standards

| Token | Value | Usage |
|-------|-------|-------|
| Navy | `#0F172A` | Headers, nav, footer, dark sections |
| Electric Blue | `#007AFF` | CTAs, links, hover states only |
| White | `#FFFFFF` | Page backgrounds |
| Light Gray | `#F8FAFC` | Alternating section backgrounds |

- **Font:** Arial, Helvetica, sans-serif
- **Dark mode:** Supported via ThemeToggle component
- **Accessibility:** WCAG AA — skip-to-content, focus-visible, keyboard navigation

## Ecosystem

RelayLaunch uses a multi-repo architecture:

| Repository | Purpose |
|------------|---------|
| **relaylaunch-website** (this repo) | Public-facing marketing site — services, blog, lead capture |
| [**relaylaunch-control-center**](https://github.com/Relay-Launch/relaylaunch-control-center) | Internal Command Center — client dashboard, operations tools |

### Blueprints for AI-Assisted Development

Both repos maintain a `docs/blueprints/` folder for architecture documents,
API contracts, and feature specs. When starting an AI-assisted build session:

1. Add your spec documents to `docs/blueprints/`
2. Point the AI tool at the folder (e.g., `@docs/blueprints` in Claude Code)
3. The AI uses those documents as context for implementation

See [`docs/blueprints/README.md`](docs/blueprints/README.md) for full details.

## Contributing

1. Create a feature branch: `git checkout -b claude/description-XXXXX`
2. Follow [conventional commits](https://www.conventionalcommits.org/): `feat:`, `fix:`, `chore:`
3. Ensure `npm run build` passes with zero errors
4. Lighthouse CI runs automatically on PRs (thresholds: 90+ perf, a11y, SEO)
5. Open a PR against `main`

## Links

- **Live site:** [relaylaunch.com](https://relaylaunch.com)
- **Complete Analysis:** [relaylaunch.com/complete-analysis](https://relaylaunch.com/complete-analysis)
- **Services:** [relaylaunch.com/services](https://relaylaunch.com/services)
- **Case Studies:** [relaylaunch.com/case-studies](https://relaylaunch.com/case-studies)
- **Blog:** [relaylaunch.com/blog](https://relaylaunch.com/blog)
- **Contact:** [relaylaunch.com/contact](https://relaylaunch.com/contact)

---

Built by **Victor David Medina** | [RelayLaunch LLC](https://relaylaunch.com) · USMC Sergeant (E-5) · Watertown, MA
