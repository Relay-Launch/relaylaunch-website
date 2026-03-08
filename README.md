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

The workflow supports two deployment modes and runs both on every push, so you can choose whichever Pages source setting works for your repo:

| Mode | Pages Source Setting | How it works |
|------|---------------------|--------------|
| **GitHub Actions** | Settings → Pages → Source → **GitHub Actions** | `deploy-actions` job deploys the build artifact directly |
| **Branch deploy** | Settings → Pages → Source → **Deploy from a branch** → `gh-pages` / `(root)` | `build` job pushes `dist/` to the `gh-pages` branch |

#### Step 1 — Enable GitHub Pages (required, one-time manual step)

1. Go to **[Settings → Pages](https://github.com/Relay-Launch/relaylaunch-website/settings/pages)**
2. Under "Build and deployment" → **Source**: select **GitHub Actions**
3. Under **Custom domain**: enter `relaylaunch.com`
4. Click **Save**; tick **Enforce HTTPS** once the DNS check passes

#### Step 2 — Configure DNS

Point your domain registrar at GitHub Pages using **one** of these options:

**Option A — A records (apex domain)**
Add four A records for `relaylaunch.com`:
```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

**Option B — CNAME (www subdomain)**
```
www.relaylaunch.com  →  relay-launch.github.io
```

#### Step 3 — Trigger the first deployment

After enabling Pages, push any commit to `main` (e.g. merge this PR), or manually trigger the workflow:

1. Go to **[Actions → Deploy Astro site to Pages](https://github.com/Relay-Launch/relaylaunch-website/actions/workflows/astro.yml)**
2. Click **Run workflow** → select branch `main` → **Run workflow**

#### Troubleshooting: "domain already taken by another repository"

If GitHub Pages shows the error **"The custom domain 'relaylaunch.com' is already taken by another repository in your organization"**, it means the `Relay-Launch/.github` repository has a `CNAME` file that claims the same domain.

**Fix — remove the CNAME from the `.github` repo:**

1. Go to **[github.com/Relay-Launch/.github](https://github.com/Relay-Launch/.github)**
2. Open the `CNAME` file in the root of the repository
3. Delete the file (click the trash-can icon → **Commit changes**)
4. Return to **[Settings → Pages](https://github.com/Relay-Launch/relaylaunch-website/settings/pages)** for this repo
5. Enter `relaylaunch.com` in the **Custom domain** field and click **Save**
6. Once the DNS check passes, tick **Enforce HTTPS**

> The `.github` repo previously served as a placeholder site. The `relaylaunch-website` Astro project is now the authoritative site and should own the `relaylaunch.com` domain claim. The `public/CNAME` file in this repo already contains `relaylaunch.com` and will be included in every deployment automatically.

#### Troubleshooting 404 errors

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| `404` on relaylaunch.com | Pages not enabled | Complete Step 1 above |
| `404` on relay-launch.github.io | Workflow never ran | Trigger the workflow (Step 3) |
| `404` after workflow ran | DNS not configured | Complete Step 2 above |
| `NXDOMAIN` / DNS error | Domain not pointed at GitHub | Complete Step 2 above |
| `domain already taken` error | `.github` repo CNAME conflict | See "domain already taken" section above |

- Check workflow run status: **[Actions tab](https://github.com/Relay-Launch/relaylaunch-website/actions)**
- Verify `public/CNAME` contains `relaylaunch.com` (not in the repo root)
- After DNS changes, allow up to 24 hours for propagation
