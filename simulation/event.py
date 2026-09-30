"""
Different event types
"""

from dataclasses import dataclass


@dataclass
class AgentEnteredBase:
    agent_id: int


@dataclass
class AgentDetected:
    searcher_id: int
    target_id: int


@dataclass
class AgentCompletedMaintenance:
    agent_id: int

