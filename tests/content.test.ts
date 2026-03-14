import { describe, it, expect } from 'vitest';
import { readdirSync, readFileSync } from 'fs';
import { join } from 'path';

const BLOG_DIR = 'src/content/blog';

describe('Blog content', () => {
  const posts = readdirSync(BLOG_DIR).filter(f => f.endsWith('.mdx'));

  it('has at least one blog post', () => {
    expect(posts.length).toBeGreaterThan(0);
  });

  posts.forEach(post => {
    describe(post, () => {
      const content = readFileSync(join(BLOG_DIR, post), 'utf-8');
      const frontmatter = content.split('---')[1];

      it('has a title', () => {
        expect(frontmatter).toMatch(/title:\s*.+/);
      });

      it('has a description', () => {
        expect(frontmatter).toMatch(/description:\s*.+/);
      });

      it('has a pubDate', () => {
        expect(frontmatter).toMatch(/pubDate:\s*.+/);
      });
    });
  });
});
