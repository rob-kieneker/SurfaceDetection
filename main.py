import logging

from config.settings import simulation_settings
from simulation.core import initiate_simulation
from utils.logging_utils import setup_logging

setup_logging(level=logging.DEBUG)


if __name__ == "__main__":
    simulation = initiate_simulation()
    simulation.run(steps=100, dt=simulation_settings.TIMEDELTA)
