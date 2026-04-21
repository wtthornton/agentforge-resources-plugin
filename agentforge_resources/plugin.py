"""AgentForge plugin entry point for agentforge-resources-plugin.

`register(app)` is called by `PluginRegistry.register_plugin()`:
1. Mounts the resources-test router onto the host FastAPI app.
2. Loads the resources-test-agent into the host's AgentLoader (if present).
3. Registers MemoryResourceProvider with the host's ResourceRegistry (if present).
"""

from __future__ import annotations

import logging
from pathlib import Path

from fastapi import FastAPI

logger = logging.getLogger(__name__)

_AGENT_DIR = Path(__file__).parent / "agents" / "resources_test_agent"
_NAMESPACE = "project.resources-test"


def register(app: FastAPI) -> None:
    from agentforge_resources.routes import router

    app.include_router(router)

    agent_loader = getattr(app.state, "agent_loader", None)
    if agent_loader is None:
        logger.debug(
            "resources plugin: no agent_loader on app.state — skipping agent load"
        )
    else:
        try:
            newly_loaded = agent_loader.load_external(_AGENT_DIR.parent, _NAMESPACE)
            logger.info(
                "resources plugin: loaded %d agent(s) from %s",
                len(newly_loaded),
                _AGENT_DIR,
            )
        except Exception:
            logger.exception("resources plugin: agent load failed")

    resource_registry = getattr(app.state, "resource_registry", None)
    if resource_registry is None:
        logger.debug(
            "resources plugin: no resource_registry on app.state — skipping provider registration"
        )
    else:
        from agentforge_resources.providers import MemoryResourceProvider

        resource_registry.register_provider(MemoryResourceProvider())
        logger.info("resources plugin: registered MemoryResourceProvider")
