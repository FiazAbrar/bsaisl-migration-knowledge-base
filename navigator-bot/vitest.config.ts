import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    include: ["test/**/*.test.ts"],
    environment: "node",
    testTimeout: 20_000,
    // Starting an embedded Postgres (PGlite) per test can take over 10 s on a busy machine.
    hookTimeout: 30_000,
    // Tests never read the real .env: each test sets the settings it needs.
    env: { NODE_ENV: "test", LOG_LEVEL: "silent" },
  },
});
