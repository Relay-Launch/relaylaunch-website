/**
 * Webhook URL validation and rate limiting utilities.
 * Used by all form submission handlers across the site.
 */

const ALLOWED_WEBHOOK_DOMAINS = [
  'hooks.zapier.com',
  'hook.us2.make.com',
  'hook.eu1.make.com',
  'hook.us1.make.com',
];

/** Validate that a webhook URL is HTTPS and on an allowed domain. */
export function isValidWebhookUrl(url: string): boolean {
  try {
    const parsed = new URL(url);
    if (parsed.protocol !== 'https:') return false;
    return ALLOWED_WEBHOOK_DOMAINS.some(domain => parsed.hostname === domain);
  } catch {
    return false;
  }
}

const RATE_LIMIT_MS = 60_000; // 1 minute between submissions

/** Check if a form submission is rate-limited. Returns true if allowed. */
export function checkRateLimit(formKey: string): boolean {
  const key = `rl_${formKey}_submitted`;
  const last = sessionStorage.getItem(key);
  if (last && Date.now() - parseInt(last) < RATE_LIMIT_MS) return false;
  return true;
}

/** Record a successful form submission for rate limiting. */
export function recordSubmission(formKey: string): void {
  const key = `rl_${formKey}_submitted`;
  sessionStorage.setItem(key, String(Date.now()));
}
