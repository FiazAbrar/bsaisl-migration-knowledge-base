import { defineConfig } from "drizzle-kit";

// `npm run db:generate` writes a new migration into drizzle/ after src/db/schema.ts changes.
// The bot applies migrations itself at start-up (src/db/client.ts).
export default defineConfig({
  dialect: "postgresql",
  schema: "./src/db/schema.ts",
  out: "./drizzle",
});
