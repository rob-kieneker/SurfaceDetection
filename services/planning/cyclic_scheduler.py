import numpy as np


def create_valid_offsets(uptime: int, downtime: int, horizon: int) -> list[np.ndarray]:
    """
    Create a list of np.ndarrays containing all valid scheduling offsets
    :param uptime: Number of periods that the agent is able to stay active
    :param downtime: Number of periods that the agent is inactive due to maintenance
    :param horizon: Time horizon of the simulation
    :return: List of valid phase offsets for active/inactive cycles
    """
    c = uptime + downtime

    tile = np.concatenate([np.ones(uptime), np.zeros(downtime)])
    # if not horizon % len(tile) == 0:
    #     raise ValueError(f"Time Horizon {horizon} is not perfectly divisible by tile length {len(tile)}")

    strip = np.tile(tile, int(horizon // len(tile)) + 1)

    offsets = []
    for i in range(min(c, horizon)):
        offset = np.roll(strip, i)
        offsets.append(offset[:horizon])

    return offsets
