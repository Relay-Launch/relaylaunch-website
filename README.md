# RelayLaunch

[![Astro](https://img.shields.io/badge/Astro-5-BC52EE?logo=astro&logoColor=white)](https://astro.build/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-4.2-06B6D4?logo=tailwindcss&logoColor=white)](https://tailwindcss.com/)
[![Cloudflare Workers](https://img.shields.io/badge/Cloudflare-Workers-F6821F?logo=cloudflare&logoColor=white)](https://workers.cloudflare.com/)
[![MDX](https://img.shields.io/badge/MDX-Blog-1B1F24?logo=mdx&logoColor=white)](https://mdxjs.com/)
[![Lighthouse](https://img.shields.io/badge/Lighthouse-95%2B-4285F4?logo=lighthouse&logoColor=white)](https://developer.chrome.com/docs/lighthouse)

**Ops on Autopilot. You on Strategy.**

RelayLaunch is a veteran-owned digital infrastructure consultancy. We replace the 5-8 disconnected tools most small businesses juggle with one integrated system built on real infrastructure. Fortune 500 experience, small business budget.

[relaylaunch.com](https://relaylaunch.com) | [hello@relaylaunch.com](mailto:hello@relaylaunch.com) | Watertown, MA

---

## What We Do

We build and run the digital infrastructure that growing businesses need but rarely have the team to manage. Websites, automations, email, CRM, social, scheduling, analytics, and payments, wired together and working.

### Service Tiers

| Tier | What You Get | Investment |
|------|-------------|------------|
| **Complete Analysis** | 8-area business infrastructure diagnostic with a 20-30 page prioritized roadmap | $1,500-$3,000 |
| **Launch** | Full infrastructure build — website, automations, email, social, dashboard | $2,500-$5,000 |
| **Run** | Monthly operations retainer — content, SEO, automation monitoring, strategy calls | $500-$1,000/mo (3-month min) |
| **Scale** | Premium growth retainer — expanded deliverables, priority support, advanced builds | $1,000-$2,500/mo (6-month min) |

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Framework | [Astro 5](https://astro.build/) — static-first, islands architecture |
| Styling | [Tailwind CSS 4.2](https://tailwindcss.com/) + Starwind design system |
| Content | MDX blog posts via Astro Content Collections |
| Hosting | [Cloudflare Workers](https://workers.cloudflare.com/) via `wrangler` |
| CI/CD | GitHub Actions — build, Lighthouse CI, `wrangler deploy` on push to `main` |
| Quality | Lighthouse CI on every PR (Performance, Accessibility, SEO targets: 95+) |
| Domain | relaylaunch.com (Registrar: Porkbun, DNS: Cloudflare) |

## Local Development

```bash
npm ci            # Install dependencies (use ci, not install)
npm run dev       # Dev server at http://localhost:4321
npm run build     # Production build to dist/
npm run preview   # Build + local Cloudflare preview via wrangler
npm run deploy    # Build + deploy to production
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

---

## Deployment

Deployments run automatically through GitHub Actions on every push to `main`.

**Pipeline:** Astro build > Lighthouse CI > `wrangler deploy` > Cloudflare Workers

```
git push origin main  →  GitHub Actions  →  wrangler deploy  →  relaylaunch.com
```

Manual deploy from your machine:

```bash
npm run deploy   # Runs build + wrangler deploy
```

### Environment Variables

Set in the Cloudflare dashboard or locally in `.env` (see `.env.example`):

| Variable | Purpose |
|----------|---------|
| `PUBLIC_GA_MEASUREMENT_ID` | Google Analytics 4 measurement ID |
| `PUBLIC_LEAD_MAGNET_WEBHOOK_URL` | n8n webhook for lead magnet form |
| `PUBLIC_CONTACT_WEBHOOK_URL` | n8n webhook for Complete Analysis booking form |

---

## Brand Standards

RelayLaunch uses a strict 4-color system across all pages and components.

| Token | Value | Usage |
|-------|-------|-------|
| **Navy** | `#0F172A` | Headers, nav, footer, dark sections |
| **Electric Blue** | `#007AFF` | CTAs, links, hover states only |
| **White** | `#FFFFFF` | Page backgrounds |
| **Light Gray** | `#F8FAFC` | Alternating section backgrounds |

- **Font:** Arial, Helvetica, sans-serif — no other fonts
- **Dark mode:** Supported via ThemeToggle component
- **Accessibility:** WCAG AA — skip-to-content, focus-visible, keyboard navigation
- **Voice:** Direct, confident, accessible, action-oriented, team-first ("we" not "I")

---

## The Relay Method

This repository uses **The Relay Method** — RelayLaunch's AI agent orchestration framework that unifies three open-source frameworks (BMAD Method, The Agency, Superpowers) into one coordinated system. Seven default agents run automatically on every code change:

| Agent | Role |
|-------|------|
| **Build** | Code quality, testing, PR review |
| **Security** | Threat detection, CSP, dependency audit |
| **Brand** | Colors, fonts, voice, visual identity |
| **QA** | Accessibility, Lighthouse, responsive |
| **Prose** | Human language, AI-ism detection |
| **Infra** | DNS, CDN, CI/CD, hosting |
| **GitHub** | Workflows, Actions, branch protection |

See [`docs/agents.md`](docs/agents.md) for the full agent registry, triggers, and specialist roles.

---

## Repositories

RelayLaunch operates as a multi-repo architecture:

| Repository | Purpose |
|------------|---------|
| **relaylaunch-website** (this repo) | Public marketing site — services, blog, lead capture |
| [**relaylaunch-control-center**](https://github.com/Relay-Launch/relaylaunch-control-center) | Internal Command Center — client dashboard, operations tools |

### Blueprints

Both repos maintain a `docs/blueprints/` folder with architecture documents, API contracts, and feature specs for AI-assisted development. See [`docs/blueprints/README.md`](docs/blueprints/README.md) for the full index.

---

## Contributing

1. Create a feature branch: `git checkout -b claude/description-XXXXX`
2. Follow [conventional commits](https://www.conventionalcommits.org/): `feat:`, `fix:`, `chore:`
3. Run `npm run build` — zero errors required
4. Lighthouse CI runs on PRs (targets: 95+ performance, accessibility, SEO)
5. Open a PR against `main`

See [SECURITY.md](SECURITY.md) for vulnerability reporting.

---

## Links

- [relaylaunch.com](https://relaylaunch.com) — Live site
- [Complete Analysis](https://relaylaunch.com/complete-analysis) — Start here
- [Services](https://relaylaunch.com/services) — Full service breakdown
- [Case Studies](https://relaylaunch.com/case-studies) — Client work
- [Blog](https://relaylaunch.com/blog) — Insights and guides
- [Contact](https://relaylaunch.com/contact) — Get in touch

---

**RelayLaunch LLC** | Built by Victor David Medina, USMC Sergeant (E-5) | Watertown, MA
