import { defineMiddleware } from 'astro:middleware';

/**
 * Security headers middleware.
 * Adds defense-in-depth HTTP headers to every response served by the
 * Cloudflare Worker. CSP is intentionally kept practical — it allows
 * Google Analytics, Cal.com embed, and Google Fonts (if ever used)
 * while blocking everything else.
 */
export const onRequest = defineMiddleware(async (_context, next) => {
  const response = await next();

  // Content-Security-Policy — allow only known origins
  const csp = [
    "default-src 'self'",
    "script-src 'self' 'unsafe-inline' https://www.googletagmanager.com https://www.google-analytics.com https://app.cal.com",
    "style-src 'self' 'unsafe-inline'",
    "img-src 'self' data: https://www.google-analytics.com https://www.googletagmanager.com https://*.cal.com",
    "font-src 'self'",
    "connect-src 'self' https://www.google-analytics.com https://analytics.google.com https://region1.google-analytics.com https://app.cal.com https://*.n8n.cloud",
    "frame-src https://app.cal.com",
    "object-src 'none'",
    "base-uri 'self'",
    "form-action 'self' https://*.n8n.cloud",
    "frame-ancestors 'none'",
    "upgrade-insecure-requests",
  ].join('; ');

  response.headers.set('Content-Security-Policy', csp);
  response.headers.set('Strict-Transport-Security', 'max-age=63072000; includeSubDomains; preload');
  response.headers.set('X-Content-Type-Options', 'nosniff');
  response.headers.set('X-Frame-Options', 'DENY');
  response.headers.set('Referrer-Policy', 'strict-origin-when-cross-origin');
  response.headers.set('Permissions-Policy', 'camera=(), microphone=(), geolocation=(), payment=()');
  response.headers.set('X-XSS-Protection', '0'); // Modern browsers use CSP; legacy header can cause issues

  return response;
});
