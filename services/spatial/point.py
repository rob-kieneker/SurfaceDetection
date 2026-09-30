import math
from enum import Enum
from config.settings import calculation_settings


class DistanceMetric(Enum):
    EUCLIDEAN = "euclidean"
    MANHATTAN = "manhatten"
    ADJ_MANHATTAN = "adjusted manhatten"


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance_to(self, other, metric=DistanceMetric.EUCLIDEAN):
        if metric == DistanceMetric.EUCLIDEAN:
            return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        elif metric == DistanceMetric.MANHATTAN:
            return abs(self.x - other.x) + abs(self.y - other.y)
        elif metric == DistanceMetric.ADJ_MANHATTAN:
            return abs(self.x - other.x) + (1-calculation_settings.MANHATTAN_ADJUSTMENT_FACTOR) * abs(self.y - other.y)
        raise ValueError(f"Invalid distance metric {metric}")
