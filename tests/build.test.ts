import { describe, it, expect } from 'vitest';
import { existsSync } from 'fs';
import { resolve } from 'path';

const dist = resolve(import.meta.dirname, '..', 'dist');

describe('Build', () => {
  it('produces dist output', () => {
    expect(existsSync(dist)).toBe(true);
  });

  it('generates HTML pages', () => {
    expect(existsSync(resolve(dist, 'index.html'))).toBe(true);
  });

  it('generates sitemap', () => {
    expect(existsSync(resolve(dist, 'sitemap-index.xml'))).toBe(true);
  });

  it('includes robots.txt', () => {
    expect(existsSync(resolve(dist, 'robots.txt'))).toBe(true);
  });
});
