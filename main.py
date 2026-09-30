import logging

from utils.logging_utils import setup_logging
from simulation.core import initiate_simulation
from config.settings import simulation_settings

setup_logging(level=logging.DEBUG)


if __name__ == "__main__":
    simulation = initiate_simulation()
    simulation.run(steps=100, dt=simulation_settings.TIMEDELTA)
