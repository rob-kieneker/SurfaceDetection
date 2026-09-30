"""
Handles repair, maintenance and availability of agents
"""
from system import System


class MaintenanceSystem(System):
    def __init__(self):
        super().__init__()

    def update(self, world, event_bus, scheduler, dt) -> None:
        pass
