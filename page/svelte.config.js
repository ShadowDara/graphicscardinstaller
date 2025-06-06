import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const config = {
  // Consult https://svelte.dev/docs/kit/integrations
  // for more information about preprocessors
  preprocess: vitePreprocess(),
  kit: {
    prerender: {
      entries: ['/graphicscardinstaller/'], // keine Startseite auf /
      handleHttpError: ({ status, path }) => {
        if (status === 404) return; // Fehler ignorieren
        throw new Error(`${status} at ${path}`);
      }
    },
    adapter: adapter({
      // default options are shown. On some platforms
      // these options are set automatically — see below
      pages: 'build',
      assets: 'build',
      fallback: undefined,
      precompress: false,
      strict: true,
    }),
    paths: {
      base: '/graphicscardinstaller',
      relative: false
    }
  }
};

export default config;
