import { describe, it, expect } from 'vitest';
import { existsSync } from 'fs';

describe('Build', () => {
  it('produces dist output', () => {
    expect(existsSync('dist')).toBe(true);
  });

  it('generates HTML pages', () => {
    const indexExists = existsSync('dist/index.html');
    expect(indexExists).toBe(true);
  });

  it('generates sitemap', () => {
    expect(existsSync('dist/sitemap-index.xml')).toBe(true);
  });

  it('includes robots.txt', () => {
    expect(existsSync('dist/robots.txt')).toBe(true);
  });
});
