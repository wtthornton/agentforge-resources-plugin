"""Unit tests for ResourcesRunner."""

from __future__ import annotations

from agentforge_resources.agents.resources_test_agent.runner import ResourcesRunner


def test_runner_returns_resources_ok() -> None:
    runner = ResourcesRunner()
    assert runner.run("anything") == "resources:ok"


def test_runner_ignores_input() -> None:
    runner = ResourcesRunner()
    assert runner.run("") == "resources:ok"
    assert runner.run("some other input") == "resources:ok"
