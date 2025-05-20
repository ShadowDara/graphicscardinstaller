import { mdsvex } from 'mdsvex';
import adapter from '@sveltejs/adapter-static';

const config = {
  extensions: ['.svelte', '.svx'],

  preprocess: [
    mdsvex({ extensions: ['.svx'] })
  ],

  kit: {
    adapter: adapter({
      // Option für statischen Export
      pages: 'build', // Ausgabeordner für die statischen Seiten
      paths: {
        base: '/graphicscardinstaller'
      },
      assets: 'build', // Wo die Assets (Bilder, CSS, JS) abgelegt werden
      fallback: null, // Keine SPA-Index.html, sondern jede Route als eigene HTML
      strict: true, // Überprüft, dass alle Seiten statisch sind
    })
  }
};

export default config;
