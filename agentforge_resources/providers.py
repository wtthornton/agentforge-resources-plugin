"""Resource providers for agentforge-resources-plugin."""

from __future__ import annotations

from backend.resources.base import ResourceSpec, ResourceProvider


class MemoryResourceProvider:
    """Provides kind='memory' — returns a plain dict as the resource value."""

    def provides(self, kind: str) -> bool:
        return kind == "memory"

    def resolve(self, spec: ResourceSpec) -> dict:
        return {"store": spec.name, "kind": spec.kind}
