"""
Collects metrics on the simulation
"""
from system import System


class StatisticsSystem(System):
    def __init__(self):
        super().__init__()

    def update(self, world, event_bus, scheduler, dt) -> None:
        pass

