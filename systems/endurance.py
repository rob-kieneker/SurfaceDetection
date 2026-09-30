"""
Checks operational availability based on agent states
"""
from system import System


class EnduranceSystem(System):
    def __init__(self):
        super().__init__()

    def update(self, world, event_bus, scheduler, dt) -> None:
        pass
