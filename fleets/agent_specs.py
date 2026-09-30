"""
Tracks and processes desired specs based on inputs
"""
from enum import Enum


class AgentState(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    MAINTENANCE = "maintenance"
    RETURNING = "returning"
    PRE_ENTRY = "pre_entry"  # Agent hasn't entered the world yet
    VOID = "void"  # Agent no longer relevant to simulation (left world)


class AgentType(Enum):
    SEARCHER = "searcher"
    TRAVELLER = "traveller"
