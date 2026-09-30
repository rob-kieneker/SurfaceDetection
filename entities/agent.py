"""
Dataclass containing core agent state information
"""
from fleets.agent_specs import AgentState, AgentType
from services.spatial import point

agent_id = 0


def assign_id() -> int:
    """
    Assigns a unique agent ID
    :return: Integer agent ID
    """
    global agent_id
    agent_id += 1
    return agent_id


class Agent:
    def __init__(
            self,
            location: point.Point,
            model: str,
            speed: float,
            endurance: float,
            agent_type: AgentType,
            agent_state: AgentState = AgentState.INACTIVE,
            spawn_time: float = 0
    ):
        """
        :param location: Point object containing coordinates
        :param model: str describing model name for outputs
        :param speed: Speed in km/h
        :param endurance: Endurance in km
        :param agent_type: Pre-defined type of the agent
        :param agent_state: Current pre-defined type of State for the agent
        :param spawn_time: Time it entered the world
        """
        self.agent_id = assign_id()
        self.agent_type = agent_type

        self.model = model
        self.speed = speed
        self.endurance = endurance
        self.spawn_time = spawn_time

        self.remaining_endurance = endurance
        self.remaining_maintenance = 0
        self.location = location
        self.route = None
        self.state = agent_state
