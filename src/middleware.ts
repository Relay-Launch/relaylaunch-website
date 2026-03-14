import { defineMiddleware } from 'astro:middleware';

const securityHeaders: Record<string, string> = {
  'X-Content-Type-Options': 'nosniff',
  'X-Frame-Options': 'SAMEORIGIN',
  'Referrer-Policy': 'strict-origin-when-cross-origin',
  'Permissions-Policy': [
    'camera=()',
    'microphone=()',
    'geolocation=()',
    'payment=()',
    'usb=()',
    'magnetometer=()',
    'gyroscope=()',
    'accelerometer=()',
    'autoplay=()',
    'document-domain=()',
    'encrypted-media=()',
    'fullscreen=(self)',
    'picture-in-picture=()',
    'screen-wake-lock=()',
    'xr-spatial-tracking=()',
  ].join(', '),
  'X-XSS-Protection': '0',
  'Strict-Transport-Security':
    'max-age=63072000; includeSubDomains; preload',
  'Cross-Origin-Opener-Policy': 'same-origin',
  'Cross-Origin-Resource-Policy': 'same-origin',
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
    "worker-src 'none'",
    "manifest-src 'self'",
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
