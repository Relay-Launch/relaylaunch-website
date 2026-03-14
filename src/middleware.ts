import { defineMiddleware } from 'astro:middleware';

const securityHeaders: Record<string, string> = {
  'X-Content-Type-Options': 'nosniff',
  'X-Frame-Options': 'SAMEORIGIN',
  'Referrer-Policy': 'strict-origin-when-cross-origin',
  'Permissions-Policy':
    'camera=(), microphone=(), geolocation=(), payment=(), usb=(), magnetometer=(), gyroscope=(), accelerometer=()',
  'X-XSS-Protection': '1; mode=block',
  'Strict-Transport-Security':
    'max-age=31536000; includeSubDomains; preload',
  'Content-Security-Policy': [
    "default-src 'self'",
    "script-src 'self' 'unsafe-inline' https://app.cal.com https://cal.com https://www.googletagmanager.com https://www.google-analytics.com",
    "style-src 'self' 'unsafe-inline' https://app.cal.com https://cal.com",
    "img-src 'self' data: https: blob:",
    "font-src 'self' data:",
    "connect-src 'self' https://hooks.zapier.com https://hook.us2.make.com https://www.google-analytics.com https://region1.google-analytics.com https://cal.com https://app.cal.com",
    "frame-src https://cal.com https://app.cal.com",
    "frame-ancestors 'self'",
    "base-uri 'self'",
    "form-action 'self' https://hooks.zapier.com https://hook.us2.make.com",
    "object-src 'none'",
    'upgrade-insecure-requests',
  ].join('; '),
};

export const onRequest = defineMiddleware(async (_context, next) => {
  const response = await next();
  for (const [key, value] of Object.entries(securityHeaders)) {
    response.headers.set(key, value);
  }
  return response;
});
