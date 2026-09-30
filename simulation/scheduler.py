"""
Delayed action scheduler
Ensures planned actions take place at a later moment
"""
from simulation.event_bus import EventBus
from simulation.world import WorldState


class Scheduler:
    def __init__(self):
        self.time = 0
        self.queue = []

    def tick(self, dt: float) -> None:
        self.time += dt

    def dispatch(self, world: WorldState, event_bus: EventBus) -> None:
        pass
