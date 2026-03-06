# Relay Launch — relaylaunch.com

Marketing and consulting website for [Relay Launch](https://relaylaunch.com), built with [Astro](https://astro.build/).

## Quick start

```bash
npm ci          # install dependencies
npm run dev     # start local dev server at http://localhost:4321
npm run build   # production build → dist/
npm run preview # preview the production build locally
```

## Deployment

### Option A: GitHub Actions Pages deployment (`astro.yml`)

The workflow `.github/workflows/astro.yml` builds and deploys the site using the GitHub Pages API on every push to `main`.

**One-time setup:**

1. Go to **Settings → Pages → Build and deployment → Source** and select **GitHub Actions**
2. Ensure GitHub Actions is **enabled** for the account/organization (see [Troubleshooting](#github-actions-is-disabled-for-your-account) below)

### Option B: Branch-based deployment (`deploy-gh-pages.yml`) — recommended if Actions Pages is unavailable

The workflow `.github/workflows/deploy-gh-pages.yml` builds the Astro site and pushes the output to the `gh-pages` branch on every push to `main`. It can also be triggered manually via **Actions → Deploy site to gh-pages branch → Run workflow**.

**One-time setup:**

1. Go to **Settings → Pages → Build and deployment → Source** and select **Deploy from a branch**
2. Set the branch to **`gh-pages`** and folder to **`/ (root)`**

> **Note:** Options A and B are mutually exclusive. Choose one based on your account's GitHub Actions capabilities.

### Manual (local deploy script)

If GitHub Actions is unavailable, you can deploy from your local machine:

```bash
bash scripts/deploy.sh
```

This script builds the site and pushes the `dist/` output to a `gh-pages` branch. When using this method, set the Pages source to **Deploy from a branch → `gh-pages` / `/ (root)`** in repository settings.

## Troubleshooting

### "GitHub Actions is currently disabled for your account"

This message means GitHub has restricted Actions at the **account level**. This is **not** a repository or workflow configuration issue — it requires GitHub Support to resolve.

**Steps to fix:**

1. **Contact GitHub Support** at <https://support.github.com/contact> — request that GitHub Actions be re-enabled for your account
2. While waiting, use the **manual deploy script** (`bash scripts/deploy.sh`) to deploy the site
3. Once GitHub Support re-enables Actions, switch the Pages source back to **GitHub Actions** and push to `main` to trigger the automated workflow

### Site not loading after deployment

1. **Verify DNS** — Ensure the following records are configured at your registrar (Porkbun):
   - `A` records pointing to GitHub Pages IPs: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - `CNAME` record: `www` → `relay-launch.github.io`
2. **Verify custom domain** — In **Settings → Pages**, confirm the custom domain is set to `relaylaunch.com` with a green checkmark
3. **Enforce HTTPS** — Check the "Enforce HTTPS" box in **Settings → Pages** (available once the TLS certificate is provisioned)
4. **Wait for propagation** — DNS changes and TLS certificate provisioning can take up to 24 hours

### Workflow runs stuck in "queued"

- Confirm the Pages source is set to **GitHub Actions** (not "Deploy from a branch")
- Check that GitHub Actions is enabled for the account (see above)
- The workflow uses `cancel-in-progress: true`, so new pushes automatically cancel stale queued runs

## Project structure

```
├── public/           # Static assets copied to dist/ at build time
│   └── CNAME         # Custom domain for GitHub Pages
├── src/
│   ├── components/   # Reusable Astro/HTML components
│   ├── content/      # Content collections (blog posts, etc.)
│   ├── layouts/      # Page layouts
│   ├── pages/        # File-based routing
│   └── styles/       # Global styles
├── astro.config.mjs  # Astro configuration
└── package.json      # Dependencies and scripts
```

## Tech stack

- **[Astro 5](https://astro.build/)** — static site generator
- **[Tailwind CSS 4](https://tailwindcss.com/)** — utility-first CSS
- **[MDX](https://mdxjs.com/)** — Markdown with JSX for content pages
- **[@astrojs/sitemap](https://docs.astro.build/en/guides/integrations-guide/sitemap/)** — automatic sitemap generation
