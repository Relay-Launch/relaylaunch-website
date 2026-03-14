import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';

import cloudflare from '@astrojs/cloudflare';

export default defineConfig({
  site: 'https://www.relaylaunch.com',
  output: 'static',
  trailingSlash: 'always',
  redirects: {
    '/case-studies/hrc': '/case-studies/luxury-wellness-spa/',
    '/control-center': '/console/',
  },
  integrations: [mdx(), sitemap({
    lastmod: new Date(),
  })],

  vite: {
    plugins: [tailwindcss()],
  },

  adapter: cloudflare(),
});