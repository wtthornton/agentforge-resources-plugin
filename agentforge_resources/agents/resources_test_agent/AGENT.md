---
name: resources-test-agent
namespace: project.resources-test.resources-test-agent
description: Test agent for agentforge.resources entry-point rig.
keywords: [resources, test]
runner: agentforge_resources.agents.resources_test_agent.runner:ResourcesRunner
resources:
  - name: store
    kind: memory
---

# Resources Test Agent

Deterministic test fixture for the AgentForge resources entry-point system.

Declares a single `memory` resource named `store`. Exists to exercise
`ResourceRegistry.resolve_all()`, `MemoryResourceProvider`, and the
`GET /api/resources-test/resolve` route without any LLM provider or external
service.
