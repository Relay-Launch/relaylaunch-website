# RelayLaunch Website – AI Agent Instructions (v1)

This document tells **AI agents (e.g., Claude, Copilot)** exactly how to work on the RelayLaunch website repo without breaking core assumptions.

Agents should treat this as the **system guide** when editing or generating code/content for this project.

---

## 1. Project Context

- Project: **RelayLaunch Website** – the public-facing marketing site for RelayLaunch LLC.
- Stack: **Astro 5 + Tailwind CSS 4.2 + MDX**, deployed to **Cloudflare Workers**.
- Owner: Victor David Medina, RelayLaunch LLC.
- Live URL: https://www.relaylaunch.com

### 1.1 Technology Decisions

Agents must assume the following unless a newer document explicitly changes them:

- **Framework:** Astro 5 with static output and islands architecture.
- **Styling:** Tailwind CSS 4.2 + custom CSS variables + Starwind design system.
- **Content:** MDX blog posts via Astro Content Collections.
- **Deployment:** Cloudflare Workers via `wrangler deploy`.
- **CI/CD:** GitHub Actions (`.github/workflows/astro.yml`).
- **DNS:** Cloudflare (nameservers managed there, domain registered at Porkbun).

Reference docs:
- `CLAUDE.md` – canonical project instructions, brand standards, and code standards.
- `docs/agents.md` – The Relay Method™ agent registry and triggers.
- `.github/copilot-instructions.md` – GitHub Copilot instructions (mirrors CLAUDE.md).

Agents must **not** change hosting, deployment, or framework decisions unless a human explicitly requests it.

---

## 2. Repository Layout

```text
relaylaunch-website/
  src/
    pages/               # Astro page routes (index, services, about, blog, etc.)
    content/
      blog/              # MDX blog posts with frontmatter schema
    components/
      Nav.astro          # Site navigation
      Footer.astro       # Site footer
      seo/SEO.astro      # SEO meta tag component
      layouts/           # BaseLayout.astro, BlogPostLayout.astro
      starwind/          # Starwind design system components (Button, Toggle, etc.)
    layouts/
      Layout.astro       # Page wrapper (Nav + Footer)
    styles/
      global.css         # Design tokens + component styles
      starwind.css       # Tailwind v4 theme CSS variables
    utils/
      blog.ts            # Blog helper functions
  public/                # Static assets (favicon, robots.txt, og-default.png)
  docs/
    agents.md            # The Relay Method™ agent registry
    blueprints/          # Architecture docs, specs, and AI reference materials
  .github/
    workflows/           # CI/CD (astro.yml, lighthouse.yml)
    prompts/             # BMAD prompt files for Copilot
    ISSUE_TEMPLATE/      # Bug report, feature request templates
    PULL_REQUEST_TEMPLATE.md
    copilot-instructions.md
    dependabot.yml
  .claude/               # Claude Code configuration
  CLAUDE.md              # Project instructions for Claude Code
```

When writing file paths, follow this layout unless the repo shows otherwise.

---

## 3. Brand Standards (Non-Negotiable)

These are **locked**. Agents must never introduce colors, fonts, or styling outside this system.

| Token | Hex | Usage |
|-------|-----|-------|
| Navy | `#0F172A` | Headers, nav, footer, dark sections |
| Electric Blue | `#007AFF` | CTAs, links, hover states ONLY |
| White | `#FFFFFF` | Page backgrounds |
| Light Gray | `#F8FAFC` | Alternating section backgrounds |

- Font: `Arial, Helvetica, sans-serif` — NO other fonts.
- **Exception:** Third-party logos in the tool marquee on `index.astro` may use their own brand colors.
- All new CSS should use CSS variables defined in `global.css`, not hardcoded hex values.

---

## 4. Rules for Agents

### 4.1 Do not change canonical content casually

- Treat the following as **source of truth**:
  - Brand colors and font: `CLAUDE.md` Brand Standards section.
  - Service tiers and pricing: `CLAUDE.md` Service Tiers section.
  - Tagline and voice: `CLAUDE.md` Brand Standards section.
- If you believe a change is needed, propose it in a **new versioned doc** (e.g., `rl-website-agent-instructions-v2.md`) rather than silently editing v1.

### 4.2 Maintain site quality

- Every page must have unique `<title>`, `<meta description>`, and Open Graph tags.
- Target Lighthouse 95+ across performance, accessibility, and SEO.
- Mobile-first responsive design with breakpoints at 640px, 768px, 1024px.
- WCAG AA accessibility: heading hierarchy, alt text, focus states.
- Use Astro `<Image>` with lazy loading for all images.
- Zero unnecessary client-side JavaScript — Astro static-first.

### 4.3 Follow code conventions

- Internal links use root-relative paths (`/services`, `/contact`).
- Commit messages: conventional commits (`feat:`, `fix:`, `chore:`).
- Use CSS variables from `global.css` instead of hardcoded values.
- Prefer editing existing files over creating new ones.

### 4.4 Respect the CI/CD pipeline

- Do NOT modify `.github/workflows/` unless explicitly asked.
- Run `npm run build` to verify changes before committing.
- The Lighthouse CI workflow runs on PRs — target 90+ on all audited pages.
- Production deploys happen automatically on push to `main` via GitHub Actions.

---

## 5. How to Generate or Edit Code Safely

### 5.1 When adding new pages

1. Create the `.astro` file in `src/pages/`.
2. Use the `Layout.astro` wrapper for consistent nav/footer.
3. Add unique SEO metadata via the `SEO` component.
4. Update `robots.txt` and sitemap if the page should be indexed.
5. Add the page to the Lighthouse CI audit list in `.github/workflows/lighthouse.yml`.

### 5.2 When editing components

1. Check if the component is used across multiple pages before changing its interface.
2. Maintain existing prop contracts — don't break pages that consume the component.
3. Keep styling within the 4-color brand system.
4. Test responsiveness at all three breakpoints.

### 5.3 When adding blog posts

1. Create an `.mdx` file in `src/content/blog/`.
2. Include all required frontmatter fields defined in `src/content.config.ts`.
3. Use the existing blog layout (`BlogPostLayout.astro`).
4. Verify the post appears correctly in the blog index.

### 5.4 When modifying styles

1. Add new design tokens to `src/styles/global.css` as CSS variables.
2. Use Tailwind utility classes where possible.
3. Never introduce colors outside the 4-color brand system.
4. Keep the Starwind component styles in `src/styles/starwind.css`.

---

## 6. What Not to Do

Agents should **not**:

- Change the **hosting/deployment** (Cloudflare Workers) without explicit sign-off.
- Introduce additional frameworks (no React, Vue, Svelte) — Astro islands only where needed.
- Modify **brand language, pricing, or tier names** without explicit approval.
- Add unnecessary client-side JavaScript — this is a static-first site.
- Use colors outside the 4-color system (Navy, Blue, White, Light Gray).
- Create hidden magic or undocumented behavior — everything should be discoverable.

---

## 7. Cross-Repo Context

This repo (`relaylaunch-website`) works alongside the **Control Center** (`relaylaunch-control-center`). Some blueprints in `docs/blueprints/` describe the Control Center's architecture and data model for cross-repo context.

When a feature spans both repos (e.g., API integrations, shared data models, webhook contracts), check `docs/blueprints/` for cross-repo specs. The website repo is the source of truth for:
- Brand standards and color system
- Service tier names and pricing
- The Relay Method™ agent registry (`docs/agents.md`)
- Public-facing copy and messaging

---

## 8. When in Doubt

If an agent is unsure about a change:

1. Prefer **proposing** a new `.md` document under `docs/blueprints/` that explains:
   - The problem.
   - The proposed change.
   - Impact on existing pages, SEO, or brand compliance.
2. Wait for human confirmation before making architectural changes.
3. When in doubt about brand compliance, run `/audit` to check.

This keeps the website coherent as multiple agents and humans work on it over time.
