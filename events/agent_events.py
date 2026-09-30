"""
Events specific to agent operational activity
"""

from events.events import Event


class AgentEvent(Event):
    DETECTED = "Detected"
    RETURN = "Return"
