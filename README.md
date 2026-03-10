# RelayLaunch Website

[![Astro](https://img.shields.io/badge/Astro-5-BC52EE?logo=astro&logoColor=white)](https://astro.build/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-4-06B6D4?logo=tailwindcss&logoColor=white)](https://tailwindcss.com/)
[![Cloudflare Pages](https://img.shields.io/badge/Cloudflare-Pages-F6821F?logo=cloudflare&logoColor=white)](https://pages.cloudflare.com/)
[![MDX](https://img.shields.io/badge/MDX-Blog-1B1F24?logo=mdx&logoColor=white)](https://mdxjs.com/)

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
| Styling | [Tailwind CSS 4](https://tailwindcss.com/) + Starwind components |
| Content | MDX blog posts via Astro Content Collections |
| Deployment | [Cloudflare Pages/Workers](https://pages.cloudflare.com/) via `wrangler` |
| CI/CD | GitHub Actions → `wrangler deploy` on push to `main` |
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
│   ├── blog/
│   └── case-studies/
├── components/
│   ├── Nav.astro
│   ├── Footer.astro
│   ├── seo/SEO.astro
│   ├── layouts/      # BaseLayout, BlogPostLayout
│   └── starwind/     # Design system components (Button, Toggle)
├── content/
│   └── blog/         # MDX blog posts
├── layouts/
│   └── Layout.astro  # Page wrapper (Nav + Footer)
└── styles/
    ├── global.css
    └── starwind.css
public/
├── favicon.svg
├── og-default.png
└── robots.txt
```

## Deployment

Deployments are fully automated via GitHub Actions.

**Trigger:** Any push to `main`
**Pipeline:** Build Astro → `wrangler deploy` → Cloudflare Pages

```
git push origin main  →  GitHub Actions  →  wrangler deploy  →  relaylaunch.com
```

To deploy manually from your machine:

```bash
npm run deploy   # npm run build + wrangler deploy
```

Cloudflare environment variables (set in Cloudflare Pages dashboard or `wrangler.toml`):

| Variable | Purpose |
|----------|---------|
| `PUBLIC_GA_MEASUREMENT_ID` | Google Analytics 4 measurement ID |
| `PUBLIC_LEAD_MAGNET_WEBHOOK_URL` | n8n webhook for lead magnet form |
| `PUBLIC_CONTACT_WEBHOOK_URL` | n8n webhook for Complete Analysis booking form |

## Brand Standards

- **Primary:** Dark Navy `#0F172A` — headers, nav, footer, dark sections
- **Accent:** Electric Blue `#007AFF` — CTAs, links, hover states only
- **Background:** White `#FFFFFF`
- **Alt sections:** Light Gray `#F8FAFC`
- **Font:** Arial, Helvetica, sans-serif

Design is **light mode only** — no dark mode toggle. Brand requires consistent presentation.

## Links

- **Live site:** [relaylaunch.com](https://relaylaunch.com)
- **Complete Analysis (primary conversion page):** [relaylaunch.com/complete-analysis](https://relaylaunch.com/complete-analysis)
- **Services:** [relaylaunch.com/services](https://relaylaunch.com/services)
- **Case Studies:** [relaylaunch.com/case-studies](https://relaylaunch.com/case-studies)
- **Blog:** [relaylaunch.com/blog](https://relaylaunch.com/blog)
- **Contact:** [relaylaunch.com/contact](https://relaylaunch.com/contact)

---

Built by **Victor David Medina** | [RelayLaunch LLC](https://relaylaunch.com) · USMC Sergeant (E-5) · Watertown, MA
