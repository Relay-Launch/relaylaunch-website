# Relay Launch

**Build Smarter. Launch Faster. Grow With Purpose.**

[relaylaunch.com](https://relaylaunch.com) | [hello@relaylaunch.com](mailto:hello@relaylaunch.com) | Watertown, MA

---

Relay Launch is a digital infrastructure consultancy for small businesses. We replace the 5-8 disconnected tools most businesses juggle — website, email, CRM, social, scheduling, analytics, payments — with one integrated system that actually talks to itself.

## The Problem We Solve

Small businesses spend $300-500/month on disconnected software and lose 5-10 hours per week on manual data entry between them. You became a business owner, not a software administrator.

## What We Do

We design and build unified, connected business systems — infrastructure-first, not bolted together after the fact. One system, one dashboard, everything connected.

### Service Packages

| Package | What You Get | Investment |
|---------|-------------|------------|
| **Signal** | Visibility & Ops Audit — 4 deliverables, no commitment | $500 - $900 |
| **Blueprint** | Systems Strategy — 90-day growth roadmap, automation map | $1,200 - $2,000 |
| **Relay** | Build & Connect — Full infrastructure build (most popular) | $1,800 - $6,000 |
| **Sustain** | Monthly Growth Support — Content, automation, ongoing support | $300 - $500/mo |

We also offer Complete Analysis engagements, AI Agent Setup, Workflow Automation, Systems Integration, and Fractional AI Ops Officer services.

## How We Work

Discovery Call &#8594; Client Intake &#8594; Complete Analysis &#8594; Presentation &#8594; Proposal &#8594; Implementation &#8594; Training & Handoff &#8594; Retainer Onboarding

Every engagement starts with understanding your operations, not selling you a template. We build in sprints, train your team, and hand off a system you fully own — zero vendor lock-in.

## Who We Serve

Service-based small businesses: spas, wellness, trades, professional services, retail, restaurants, fitness studios. Primarily Boston & the Northeast, but we work remotely with clients anywhere.

## About the Founder

**Victor David Medina** — Cloud engineer with Fortune 500 experience (ezCater, Blue Matter), USMC Sergeant (E-5, Honorable Discharge). Enterprise-grade thinking applied to small business budgets.

## Get Started

- **Start a project:** [Contact us](https://relaylaunch.com/contact)
- **Quick question:** [hello@relaylaunch.com](mailto:hello@relaylaunch.com)
- **See our work:** [Case Studies](https://relaylaunch.com/case-studies)

---

### Development

Built with [Astro](https://astro.build/) + [Tailwind CSS](https://tailwindcss.com/). Hosted on GitHub Pages.

```bash
npm ci          # install dependencies
npm run dev     # local dev server at localhost:4321
npm run build   # production build to dist/
```

### Deployment

The site deploys automatically to GitHub Pages via `.github/workflows/astro.yml` on every push to `main`.

**GitHub Pages Settings** (Required):
1. Go to repository Settings → Pages
2. Set **Source** to: **GitHub Actions**
3. **Custom domain**: relaylaunch.com (configured via `public/CNAME`)

The workflow:
- Builds the Astro site (`npm run build` → `dist/`)
- Uploads the `dist/` directory as a Pages artifact
- Deploys to GitHub Pages

**DNS Configuration** (for custom domain):
- Add a CNAME record pointing `relaylaunch.com` to `relay-launch.github.io`
- Or use A records pointing to GitHub Pages IPs (see [GitHub docs](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site))

**Troubleshooting**:
- If you see 404 errors, verify Pages source is set to "GitHub Actions" (not "Deploy from a branch")
- Check workflow runs at: Actions → Deploy Astro site to Pages
- Verify the CNAME file exists in `public/CNAME` (not repository root)
