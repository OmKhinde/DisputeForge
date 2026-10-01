import express, { Request, Response } from "express";
import dotenv from "dotenv";

dotenv.config();

const app = express();
const PORT = process.env.NODE_PORT || 3000;

app.use(express.json());

// ── Health Check ────────────────────────────────────────────
// Phase 0: Only route. All other routes added in later phases.
app.get("/health", (_req: Request, res: Response) => {
  res.status(200).json({
    status: "ok",
    service: "disputeforge-node-service",
    timestamp: new Date().toISOString(),
  });
});

// ── Start Server ────────────────────────────────────────────
app.listen(PORT, () => {
  console.log(`[node-service] Running on port ${PORT}`);
});

export default app;
