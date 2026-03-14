# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in this project, please report it
responsibly. **Do not open a public GitHub issue.**

Email: **security@relaylaunch.com**

We will acknowledge your report within 48 hours and aim to provide a fix or
mitigation within 7 days for critical issues.

## Supported Versions

| Version | Supported |
|---------|-----------|
| Latest (main branch) | Yes |

## Security Measures

### Dependencies
- **Dependabot** runs daily scans and opens PRs for vulnerable packages.
- **npm audit** runs on every CI build — high-severity findings block deploys.
- **Dependency review** checks every PR for newly introduced vulnerabilities.
- **CodeQL** performs static analysis on every push and PR.
- **TruffleHog** scans for leaked secrets in every push.

### HTTP Security Headers
All responses include:
- `Content-Security-Policy` — restricts script, style, and connection origins
- `Strict-Transport-Security` — enforces HTTPS with preload
- `X-Content-Type-Options: nosniff`
- `X-Frame-Options: DENY`
- `Referrer-Policy: strict-origin-when-cross-origin`
- `Permissions-Policy` — disables camera, microphone, geolocation, payment

### Infrastructure
- Hosted on **Cloudflare Workers** with DDoS protection and WAF
- Static-first architecture (no server-side rendering attack surface)
- All environment variables are `PUBLIC_` prefixed (no server secrets in client)
- Form submissions use webhook endpoints (no direct database access)
- Honeypot fields on all forms for bot prevention

## Scope

This policy covers the `relaylaunch-website` repository and the
`relaylaunch.com` / `www.relaylaunch.com` domains.
