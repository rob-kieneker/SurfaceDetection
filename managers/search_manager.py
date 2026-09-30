"""
Coordinates searcher strategy and resource utilisation
"""
from base_manager import Manager
from simulation.event_bus import EventBus
from simulation.world import WorldState


class SearchManager(Manager):
    def __init__(self, world: WorldState, event_bus: EventBus):
        super().__init__(world, event_bus)

    def update(self):
        pass

    def on_agent_entered_base(self, event):
        pass
