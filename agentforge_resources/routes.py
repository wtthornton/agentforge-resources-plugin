"""Resources test plugin HTTP routes — GET /api/resources-test/resolve."""

from __future__ import annotations

from fastapi import APIRouter, HTTPException, Request

router = APIRouter(prefix="/api/resources-test", tags=["resources-test"])


@router.get("/resolve")
async def resolve(request: Request) -> dict:
    """Resolve all resources declared by resources-test-agent and return names."""
    agent_loader = getattr(request.app.state, "agent_loader", None)
    if agent_loader is None:
        raise HTTPException(status_code=503, detail="agent_loader not available")

    config = agent_loader.resolve("project.resources-test.resources-test-agent")
    if config is None:
        raise HTTPException(status_code=404, detail="resources-test-agent not loaded")

    resource_registry = getattr(request.app.state, "resource_registry", None)
    if resource_registry is None:
        raise HTTPException(status_code=503, detail="resource_registry not available")

    resolved = resource_registry.resolve_all(config.resources)
    return {"resolved": True, "names": list(resolved.keys())}
