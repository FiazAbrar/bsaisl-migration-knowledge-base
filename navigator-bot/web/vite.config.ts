import path from "node:path";
import { defineConfig } from "vite";

// The web chat page: plain TypeScript, no framework, so it stays small for cheap phones on slow data.
// `npm run build:web` writes web/dist, which the bot serves at /. `npm run dev:web` serves the page with
// live reload and passes /api to the bot running on port 8000 (`npm run dev`).
export default defineConfig({
  root: path.resolve(import.meta.dirname),
  publicDir: "public",
  build: {
    outDir: "dist",
    emptyOutDir: true,
    target: "es2020",
    sourcemap: false,
    rollupOptions: {
      input: {
        index: path.resolve(import.meta.dirname, "index.html"),
        privacy: path.resolve(import.meta.dirname, "privacy.html"),
      },
    },
  },
  server: { proxy: { "/api": "http://localhost:8000" } },
});
