"""
Contains high-level logic shared across managers
"""
from abc import abstractmethod

from simulation.event_bus import EventBus
from simulation.world import WorldState


class Manager:
    def __init__(self, world: WorldState, event_bus: EventBus) -> None:
        self.world = world
        self.event_bus = event_bus

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def on_agent_entered_base(self, event):
        pass
