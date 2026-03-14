import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const blog = defineCollection({
  loader: glob({ pattern: '**/*.mdx', base: './src/content/blog' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    tags: z.array(z.string()).default([]),
    heroImage: z.string().optional(),
    draft: z.boolean().default(false),
    author: z.string().default('Victor David Medina'),
    ogImage: z.string().optional(),
  }),
});

const caseStudies = defineCollection({
  loader: glob({ pattern: '**/*.json', base: './src/content/case-studies' }),
  schema: z.object({
    title: z.string(),
    client: z.string(),
    industry: z.string(),
    description: z.string(),
    slug: z.string(),
    metrics: z.array(z.object({
      label: z.string(),
      value: z.string(),
    })),
    services: z.array(z.string()),
    pubDate: z.coerce.date(),
    featured: z.boolean().default(false),
  }),
});

export const collections = { blog, caseStudies };
