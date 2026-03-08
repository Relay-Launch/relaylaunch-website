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

## Development

Built with [Astro](https://astro.build/) + [Tailwind CSS](https://tailwindcss.com/). Hosted on GitHub Pages.

```bash
npm ci          # install dependencies
npm run dev     # local dev server at localhost:4321
npm run build   # production build to dist/
```

## Deployment

The website deploys automatically via `.github/workflows/astro.yml` on every push to `main`. The workflow builds the Astro site, pushes the output to the `gh-pages` branch, and also attempts a direct GitHub Actions Pages deployment.

### Resolving the 404 / Blocked Actions

The deployment workflow (`astro.yml`) has **never run** because GitHub Actions is blocked for this repository. The built-in Jekyll Pages workflow runs instead, but fails because this is an Astro project (not Jekyll). Follow the steps below in order.

#### Step 1 — Unblock GitHub Actions

GitHub Actions must be allowed for user-defined workflows in the **Relay-Launch** organization before any deployment can happen.

1. Go to **[Organization Settings → Actions → General](https://github.com/organizations/Relay-Launch/settings/actions)**
2. Under **Actions permissions**, select **Allow all actions and reusable workflows** (or at minimum "Allow select actions" including `actions/*`)
3. Under **Workflow permissions**, select **Read and write permissions**
4. Click **Save**

> If these settings are already correct and the workflow still shows "blocked", contact [GitHub Support](https://support.github.com/) to resolve the block on your account.

#### Step 2 — Disable GitHub Pages on the `.github` repository

The `Relay-Launch/.github` repo also has GitHub Pages enabled with its own HTML files (`index.html`, etc.) and a deploy workflow. This can conflict with this repo's custom domain claim.

1. Go to **[Relay-Launch/.github → Settings → Pages](https://github.com/Relay-Launch/.github/settings/pages)**
2. Set **Source** to **None** (disable Pages)
3. If a custom domain is set, remove it and click **Save**

#### Step 3 — Configure GitHub Pages on this repository

1. Go to **[Settings → Pages](https://github.com/Relay-Launch/relaylaunch-website/settings/pages)**
2. Under **Source**: select **GitHub Actions**
3. Under **Custom domain**: enter `relaylaunch.com` and click **Save**
4. Tick **Enforce HTTPS** once the DNS check passes

#### Step 4 — Trigger the first deployment

Once Actions are unblocked:

- **Automatic**: push or merge any commit to `main`
- **Manual**: go to [Actions → Deploy Astro site to Pages](https://github.com/Relay-Launch/relaylaunch-website/actions/workflows/astro.yml) → **Run workflow** → select `main` → **Run workflow**

### DNS Configuration (Porkbun)

Point `relaylaunch.com` at GitHub Pages with **A records** for the apex domain:

```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

Optionally add a **CNAME** for `www`:

```
www  →  relay-launch.github.io
```

### Troubleshooting

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| `404` on relaylaunch.com | Workflow never ran / Actions blocked | Complete Steps 1-4 above |
| Workflow shows "blocked" | Actions disabled at org level | Step 1 |
| `domain already taken` error | `.github` repo claims the domain | Step 2 |
| `NXDOMAIN` / DNS error | Domain not pointed at GitHub | See DNS section |

Run `./scripts/check-deployment.sh` to verify deployment health.
