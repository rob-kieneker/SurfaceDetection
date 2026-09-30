"""
General Agent movement updates
"""
from system import System


class MovementSystem(System):
    def __init__(self):
        super().__init__()

    def update(self, world, event_bus, scheduler, dt) -> None:
        pass
