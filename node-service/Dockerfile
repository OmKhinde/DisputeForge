# ── DisputeForge Node Service ────────────────────────────────
# Multi-stage build for smaller production image
# Phase 0: Health check only

FROM node:20-alpine AS base
WORKDIR /app

# ── Dependencies ─────────────────────────────────────────────
FROM base AS deps
COPY package.json package-lock.json* ./
RUN npm install

# ── Development ──────────────────────────────────────────────
FROM base AS dev
COPY --from=deps /app/node_modules ./node_modules
COPY . .
RUN npx prisma generate
EXPOSE 3000
CMD ["npx", "ts-node-dev", "--respawn", "--transpile-only", "src/index.ts"]
