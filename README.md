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

The workflow `.github/workflows/astro.yml` builds and deploys the site automatically on every push to `main`. It supports **both** GitHub Pages deployment methods so it works regardless of your Pages source setting:

- **GitHub Actions source** — deploys directly via `actions/deploy-pages`
- **Deploy from a branch source** — pushes built files to the `gh-pages` branch

### One-time setup (required)

1. Ensure **GitHub Actions is enabled** for the repository (Settings → Actions → General → Allow all actions)
2. Go to **Settings → Pages → Build and deployment → Source** and select one of:
   - **GitHub Actions** (recommended), OR
   - **Deploy from a branch** → **`gh-pages`** / `/ (root)`
3. Set **Custom domain** to `relaylaunch.com` and check **Enforce HTTPS**
4. Push any change to `main` (or click **Actions → Deploy Astro site to Pages → Run workflow**) to trigger the first deployment

### Manual deploy (fallback)

If GitHub Actions is unavailable, deploy from your local machine:

```bash
bash scripts/deploy.sh
```

This builds the site and pushes the `dist/` output to a `gh-pages` branch. After running:

1. Go to **Settings → Pages → Source** → **Deploy from a branch** → **`gh-pages` / `(root)`**

## Troubleshooting

### Site not loading / 404 after deployment

1. **Check that the workflow ran successfully** — Go to **Actions** tab and verify the latest "Deploy Astro site to Pages" run is green
2. **Check the Pages source** — In **Settings → Pages**, confirm:
   - Source = **GitHub Actions** or **Deploy from a branch → `gh-pages` / `(root)`**
   - Custom domain = `relaylaunch.com` with a **green checkmark ✅**
   - "Enforce HTTPS" is **checked**
3. **Verify DNS** at your registrar (e.g. Porkbun):
   - `A` records → `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - `CNAME` record: `www` → `relay-launch.github.io`
4. **Wait for propagation** — DNS changes and TLS certificate provisioning can take up to 24 hours

### "GitHub Actions is currently disabled for your account"

Actions has been restricted at the account or organization level.

1. Contact GitHub Support at <https://support.github.com/contact> and request Actions be re-enabled
2. While waiting, run `bash scripts/deploy.sh` locally, then set Pages source to **Deploy from a branch → `gh-pages` / `(root)`**

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
