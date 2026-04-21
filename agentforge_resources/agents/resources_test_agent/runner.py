"""Deterministic runner for resources-test-agent. No side effects."""

from __future__ import annotations


class ResourcesRunner:
    def run(self, input_text: str) -> str:
        return "resources:ok"
