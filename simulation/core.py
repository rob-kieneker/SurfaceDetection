"""
Main simulation loop management
"""

import logging

from world import create_world_state

from managers.search_manager import SearchManager
from managers.travel_manager import TravelManager
from simulation.event_bus import EventBus
from simulation.scheduler import Scheduler
from simulation.world import WorldState
from systems.detection import DetectionSystem
from systems.endurance import EnduranceSystem
from systems.maintenance import MaintenanceSystem
from systems.movement import MovementSystem
from systems.statistics import StatisticsSystem

logger = logging.getLogger(__name__)


class SimulationEngine:
    """
    Orchestrates the simulation tick loop.

    Responsibilities:
    - Define system execution order
    - Move through the simulation steps
    - Manage world + event bus through systems
    """

    def __init__(self, world: WorldState):
        self.world = world
        self.event_bus = EventBus()
        self.scheduler = Scheduler()

        self.managers = [
            SearchManager(self.world, self.event_bus),
            TravelManager(self.world, self.event_bus),
        ]

        self.systems = [
            EnduranceSystem(),
            MovementSystem(),
            DetectionSystem(),
            MaintenanceSystem(),
            StatisticsSystem(),
        ]

        logger.info("Simulation initialized")

    def step(self, dt: float = 1.0) -> None:
        """
        Advance simulation by one tick and process updates.
        """
        self.world.tick(dt)
        self.scheduler.tick(dt)

        logger.debug(f"Processing Tick {self.world.time}")

        self.scheduler.dispatch(self.world, self.event_bus)

        for system in self.systems:
            system.update(
                world=self.world,
                event_bus=self.event_bus,
                scheduler=self.scheduler,
                dt=dt,
            )

        for manager in self.managers:
            manager.update()

    def run(self, steps: int, dt: float = 1.0):
        for i in range(steps):
            self.step(dt)

        logger.info("Simulation complete")


def initiate_simulation() -> SimulationEngine:
    world = create_world_state()
    return SimulationEngine(world)
