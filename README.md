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

The workflow `.github/workflows/astro.yml` builds and deploys the site automatically on every push to `main`.

### One-time setup (required)

1. Go to **Settings → Pages → Build and deployment → Source** and select **GitHub Actions**
   - ⚠️ If it is currently set to "Deploy from a branch", change it — that setting causes GitHub's Jekyll builder to fail on Astro source files
2. Ensure **GitHub Actions is enabled** for the repository (Settings → Actions → General → Allow all actions)
3. Confirm that the **`github-pages` environment** exists in Settings → Environments (GitHub creates it automatically when you enable the Actions source)

After merging this PR, push any change to `main` (or click **Actions → Deploy Astro site to Pages → Run workflow**) to trigger the first deployment.

### Manual deploy (fallback)

If GitHub Actions is unavailable, deploy from your local machine:

```bash
bash scripts/deploy.sh
```

This builds the site and pushes the `dist/` output to a `gh-pages` branch. After running:

1. Go to **Settings → Pages → Source** → **Deploy from a branch** → **`gh-pages` / `(root)`**

## Troubleshooting

### Jekyll build failing ("Invalid YAML front matter")

This error appears when GitHub Pages Source is set to **Deploy from a branch** pointing to a branch that contains raw Astro source files. Fix:

1. Go to **Settings → Pages → Build and deployment → Source** → select **GitHub Actions**
2. Merge this PR so `astro.yml` is on `main`, then push (or use `workflow_dispatch`) to trigger a fresh deployment

### "GitHub Actions is currently disabled for your account"

Actions has been restricted at the account or organization level. This requires GitHub Support to resolve.

**Steps:**

1. Contact GitHub Support at <https://support.github.com/contact> and request Actions be re-enabled
2. While waiting, run `bash scripts/deploy.sh` locally, then set Pages source to **Deploy from a branch → `gh-pages` / `(root)`**
3. Once Actions is re-enabled, switch Pages source back to **GitHub Actions**

### Site not loading / 404 after deployment

1. **Check the Pages source** — In **Settings → Pages**, confirm:
   - Source = **GitHub Actions** (not "Deploy from a branch")
   - Custom domain = `relaylaunch.com` with a **green checkmark ✅**
   - "Enforce HTTPS" is **checked**
2. **Verify DNS** at your registrar (e.g. Porkbun):
   - `A` records → `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - `CNAME` record: `www` → `relay-launch.github.io`
3. **Wait for propagation** — DNS changes and TLS certificate provisioning can take up to 24 hours

### Workflow stuck in "queued" / never runs

1. Confirm Pages source is set to **GitHub Actions** (not "Deploy from a branch")
2. Confirm GitHub Actions is enabled (Settings → Actions → General)
3. Check Settings → Environments → `github-pages` exists and has no blocking protection rules
4. Try triggering manually: Actions → Deploy Astro site to Pages → Run workflow

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
