# Navigator bot image: the bot code only. The guides are NOT in the image: at start, and then every
# KB_SYNC_MINUTES, the bot pulls them from GitHub (KB_REPO), so guide updates go live without a redeploy.
#   docker build -t navigator-bot navigator-bot
#   docker run --env-file navigator-bot/.env -p 8000:8000 navigator-bot

# 1. Build the web chat page.
FROM node:26-slim AS web
WORKDIR /build
COPY package.json package-lock.json ./
RUN npm ci --ignore-scripts --no-audit --no-fund
COPY web ./web
# The page shares the personal-number rules with the server (src/conversation/safeguards.ts).
COPY src/conversation/safeguards.ts ./src/conversation/safeguards.ts
COPY tsconfig.json ./
RUN npm run build:web

# 2. The server: production dependencies, the TypeScript sources (Node runs them directly) and the page.
FROM node:26-slim
ENV NODE_ENV=production \
    NPM_CONFIG_UPDATE_NOTIFIER=false
# git fetches the guides (a shallow, sparse clone without the source archives); tini forwards signals
# so a redeploy lets answers in progress finish.
RUN apt-get update \
    && apt-get install -y --no-install-recommends git ca-certificates tini \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /srv/navigator-bot
COPY package.json package-lock.json ./
RUN npm ci --omit=dev --ignore-scripts --no-audit --no-fund && npm cache clean --force
COPY src ./src
COPY drizzle ./drizzle
COPY prompts ./prompts
COPY --from=web /build/web/dist ./web/dist
# data/ holds the bot's copy of the guides (and, without DATABASE_URL, a local database).
RUN mkdir -p data && chown node:node data
USER node

EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=5s --start-period=60s --retries=3 \
    CMD ["node", "-e", "fetch('http://127.0.0.1:'+(process.env.PORT||8000)+'/health').then(r=>process.exit(r.ok?0:1),()=>process.exit(1))"]
ENTRYPOINT ["/usr/bin/tini", "--"]
CMD ["node", "src/main.ts"]
