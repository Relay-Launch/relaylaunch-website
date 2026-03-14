# Security Policy

RelayLaunch takes security seriously. This policy covers the `relaylaunch-website` repository and the `relaylaunch.com` / `www.relaylaunch.com` domains.

## Reporting a Vulnerability

If you discover a security vulnerability, report it responsibly. **Do not open a public GitHub issue.**

**Email:** [security@relaylaunch.com](mailto:security@relaylaunch.com)

We acknowledge reports within 48 hours and aim to ship a fix within 7 days for critical issues.

## Supported Versions

| Version | Supported |
|---------|-----------|
| Latest (`main` branch) | Yes |
| All other branches | No |

## Security Measures

### Automated Scanning

- **Dependabot** scans dependencies daily and opens PRs for vulnerable packages
- **npm audit** runs on every CI build — high-severity findings block deploys
- **Dependency review** checks every PR for newly introduced vulnerabilities
- **CodeQL** performs static analysis on every push and PR
- **TruffleHog** scans for leaked secrets in every push

### HTTP Security Headers

All responses include:

| Header | Value |
|--------|-------|
| `Content-Security-Policy` | Restricts script, style, and connection origins |
| `Strict-Transport-Security` | Enforces HTTPS with preload |
| `X-Content-Type-Options` | `nosniff` |
| `X-Frame-Options` | `DENY` |
| `Referrer-Policy` | `strict-origin-when-cross-origin` |
| `Permissions-Policy` | Disables camera, microphone, geolocation, payment |

### Infrastructure

- Hosted on **Cloudflare Workers** with built-in DDoS protection and WAF
- Static-first architecture eliminates server-side rendering attack surface
- All environment variables use `PUBLIC_` prefix (no server secrets in client bundles)
- Form submissions route through webhook endpoints (no direct database access)
- Honeypot fields on all forms for bot prevention
- DKIM, DMARC, and SPF configured for email authentication

## Scope

This policy covers:
- The `relaylaunch-website` repository
- The `relaylaunch.com` and `www.relaylaunch.com` domains
- All CI/CD workflows in `.github/workflows/`

Out of scope: third-party services (Cloudflare, Porkbun, Google Workspace) — report those to the respective vendors.
