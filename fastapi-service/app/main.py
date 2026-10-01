"""
DisputeForge — FastAPI Service
Phase 0: Health check only. No business logic.

This service is STATELESS (AGENTS.md rule #2).
It receives context, returns resolution proposals, never executes actions,
and never writes to any datastore.
"""

from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI(
    title="DisputeForge Agent Service",
    description="Stateless LangGraph agent for marketplace dispute resolution",
    version="0.1.0",
)


@app.get("/health")
async def health_check():
    """Phase 0: Only route. All other endpoints added in later phases."""
    return {
        "status": "ok",
        "service": "disputeforge-fastapi-service",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
