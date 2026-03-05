import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const blog = defineCollection({
  loader: glob({ pattern: '**/*.mdx', base: './src/content/blog' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.string(),
    author: z.string().default('Victor David Medina'),
    ogImage: z.string().optional(),
    tags: z.array(z.string()).default([]),
  }),
});

export const collections = { blog };
