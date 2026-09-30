"""
General Systems parent class for default functions/abstract methods
"""
from abc import ABC, abstractmethod


class System(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def update(self, world, event_bus, scheduler, dt) -> None:
        pass
