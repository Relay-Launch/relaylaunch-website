# RelayLaunch Website

## Project Overview
RelayLaunch (relaylaunch.com) is a digital infrastructure consultancy website for small businesses. Built with Astro 5 + Tailwind CSS 4 + MDX, deployed to GitHub Pages.

## Tech Stack
- **Framework**: Astro 5 (static site generator)
- **Styling**: Tailwind CSS 4.2 + custom CSS variables
- **Content**: MDX blog posts via Astro Content Collections
- **Components**: Starwind design system (button, theme-toggle, toggle)
- **Deployment**: GitHub Pages via GitHub Actions (.github/workflows/astro.yml)
- **Domain**: relaylaunch.com (DNS via Porkbun, A records to GitHub Pages IPs)

## Commands
- `npm ci` — install dependencies
- `npm run dev` — start dev server at localhost:4321
- `npm run build` — production build to dist/
- `npm run preview` — preview built site locally

## Project Structure
- `src/pages/` — Astro page routes (index, services, about, contact, etc.)
- `src/content/blog/` — MDX blog posts with frontmatter schema
- `src/components/` — Reusable Astro components (Nav, Footer, SEO, layouts)
- `src/components/starwind/` — Starwind design system components
- `src/layouts/` — Page layout wrapper (Layout.astro)
- `src/components/layouts/` — Base layouts (BaseLayout.astro, BlogPostLayout.astro)
- `src/styles/` — Global CSS and Starwind CSS variables
- `src/utils/` — Utility functions (blog.ts for post sorting/filtering)
- `public/` — Static assets (CNAME, favicon, robots.txt, og-default.png)
- `scripts/` — Deployment and maintenance shell scripts

## Environment Variables
See `.env.example` for required variables:
- `PUBLIC_LEAD_MAGNET_WEBHOOK_URL` — webhook for lead magnet form
- `PUBLIC_INTAKE_FORM_URL` — external intake form URL
- `PUBLIC_GA_MEASUREMENT_ID` — Google Analytics 4 ID

## Design System
- CSS custom properties defined in `src/styles/global.css` and `src/styles/starwind.css`
- Key colors: `--color-green` (primary), `--color-orange` (accent)
- Dark mode via `.dark` class on `<html>`, toggled by ThemeToggle component
- Typography: system font stack, clamp() for fluid sizing

## Blog Content
- Blog posts are `.mdx` files in `src/content/blog/`
- Schema defined in `src/content.config.ts`
- Required frontmatter: title, description, pubDate
- Optional: tags, author, heroImage, draft, updatedDate, ogImage

## Key Conventions
- All pages use the Layout.astro wrapper (which includes Nav + Footer)
- SEO component (src/components/seo/SEO.astro) handles meta tags and JSON-LD
- Buttons use the Starwind Button component with variant="primary" or variant="outline"
- Internal links use root-relative paths (e.g., /services, /contact)
- External links always have target="_blank" rel="noopener"

## Deployment
- Pushes to `main` trigger GitHub Actions workflow
- Workflow builds Astro site and pushes to `gh-pages` branch
- Also attempts direct GitHub Actions Pages deployment
- CNAME file in public/ claims relaylaunch.com domain
