"""
Grouping of Agent types by similar characteristics
"""

import numpy as np
import pandas as pd

from config.settings.simulation_settings import SIMULATION_TIME
from entities.agent import Agent
from fleets.agent_specs import AgentState, AgentType
from services.spatial.point import Point

fleet_id = 0


def assign_fleet_id() -> int:
    global fleet_id
    fleet_id += 1
    return fleet_id


class Fleet:
    """
    Fleets contain set of agents with shared characteristics
    """

    def __init__(self, agent_type: AgentType, agents: list[Agent]):
        self.fleet_id = assign_fleet_id()
        self.agent_type = agent_type
        self.agents = agents


def initiate_search_fleet(df: pd.DataFrame) -> Fleet:
    """
    Creates the search fleet based on the passed dataframe
    :param df: DataFrame with:
     - "model" str
     - "speed" float in km/h
     - "endurance" float in km
    :return:
    """
    agent_type = AgentType.SEARCHER
    agents = []
    base_location = Point(0, 0)

    for row in df.itertuples():
        agent = Agent(
            location=base_location,
            model=row.model,
            speed=row.speed,
            endurance=row.endurance,
            agent_type=agent_type,
        )
        agents.append(agent)

    return Fleet(agent_type, agents)


def initiate_traveller_fleet(df: pd.DataFrame) -> Fleet:
    """
    Creates the search fleet based on the passed dataframe
    :param df: DataFrame with:
     - "model" str
     - "speed" float in km/h
     - "endurance" float in km
     - "arrival_rate" float poisson arrival rate (lambda), arrivals per timestep
    :return:
        Fleet
    """
    agent_type = AgentType.TRAVELLER
    agents = []
    base_location = Point(0, 0)

    for row in df.itertuples():
        model: str = row.model
        speed: float = row.speed
        endurance: float = row.endurance
        arrival_rate: float = row.arrival_rate

        for a_t in sample_arrivals(arrival_rate):
            agent = Agent(
                location=base_location,
                model=model,
                speed=speed,
                endurance=endurance,
                agent_type=agent_type,
                agent_state=AgentState.PRE_ENTRY,
                spawn_time=a_t,
            )
            agents.append(agent)

    return Fleet(agent_type, agents)


def sample_arrivals(arrival_rate: float) -> list[float]:
    """
    Generates a list of arrival times within the simulation window
    based on the provided arrival rate.
    :param arrival_rate:
    :return:
    """
    arrival_time = 0
    arrival_times = []

    while arrival_time < SIMULATION_TIME:
        inter_arrival_time = np.random.exponential(scale=1 / arrival_rate)
        arrival_time += inter_arrival_time
        arrival_times.append(arrival_time)

    return arrival_times
