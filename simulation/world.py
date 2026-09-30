"""
Tracks World state
"""
from collections import defaultdict

from entities.agent import Agent
from entities.patrol_location import PatrolLocation
from fleets.agent_specs import AgentType
from fleets.fleet import Fleet, initiate_search_fleet, initiate_traveller_fleet
from input.extract_input import extract_searcher_data, extract_traveller_data
from utils.logging_utils import get_logger

logger = get_logger(__name__)


class WorldState:
    """
    Tracks general world state and owns all entities
    """

    def __init__(self):

        # World
        self.time = 0
        self.bases = {}

        # Entities
        self.agents: list[Agent] = []
        self.fleets: dict[AgentType: Fleet] = {}
        self.patrol_locations: list[PatrolLocation] = []

        # Agent slices
        self.agents_by_state = defaultdict(list)

    def tick(self, dt: float):
        self.time += dt

    def initialize_world_state(self) -> None:
        logger.info("Initialising entities...")
        searcher_data = extract_searcher_data()
        search_fleet = initiate_search_fleet(searcher_data)

        traveller_data = extract_traveller_data()
        travel_fleet = initiate_traveller_fleet(traveller_data)

        self.fleets = {
            AgentType.SEARCHER: search_fleet,
            AgentType.TRAVELLER: travel_fleet,
        }
        self.agents = search_fleet.agents + travel_fleet.agents

        for agent in self.agents:
            self.agents_by_state[agent.state].append(agent)


def create_world_state() -> WorldState:
    logger.info("Creating world state...")
    w = WorldState()
    w.initialize_world_state()
    return w
