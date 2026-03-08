/**
 * Blog utilities for efficient content collection and filtering
 */
import { getCollection } from 'astro:content';

/**
 * Get all published blog posts, sorted by publication date (newest first)
 * Uses optimized filtering during collection query instead of post-processing
 */
export async function getPublishedPosts() {
  // Filter during collection query for better performance
  const posts = await getCollection('blog', ({ data }) => !data.draft);

  // Cache timestamp calculations to avoid duplicate getTime() calls
  return posts.sort((a, b) => {
    const aTime = a.data.pubDate.getTime();
    const bTime = b.data.pubDate.getTime();
    return bTime - aTime;
  });
}

/**
 * Get a limited number of recent published posts
 * @param limit Maximum number of posts to return
 */
export async function getRecentPosts(limit: number) {
  const posts = await getPublishedPosts();
  return posts.slice(0, limit);
}
