# agentforge-resources-plugin

Test rig for the AgentForge `agentforge.resources` entry-point system.

Exercises `MemoryResourceProvider`, `ResourceRegistry.resolve_all()`, and
hot-reload semantics without any LLM provider or external service.

## Structure

```
agentforge_resources/
  plugin.json                          # plugin manifest
  plugin.py                            # register(app) — mounts router, loads agent, registers provider
  routes.py                            # GET /api/resources-test/resolve
  providers.py                         # MemoryResourceProvider
  agents/resources_test_agent/
    AGENT.md                           # declares resources: [{name: store, kind: memory}]
    runner.py                          # ResourcesRunner.run() → "resources:ok"
tests/
  test_runner.py                       # unit tests for ResourcesRunner
backend/tests/test_resources_smoke.py  # integration smoke tests (in AgentForge repo)
```

## Entry-points

```toml
[project.entry-points."agentforge.plugins"]
resources-test = "agentforge_resources"

[project.entry-points."agentforge.resources"]
memory-provider = "agentforge_resources.providers:MemoryResourceProvider"
```

## Installation

```bash
pip install -e /path/to/agentforge-resources-plugin
```

Then run the smoke tests from the AgentForge repo:

```bash
uv run pytest backend/tests/test_resources_smoke.py -v
```
