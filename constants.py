from enum import Enum, auto

class InterpolationMethod(Enum):
    LAGRANGE = auto()
    CUBIC_SPLINE = auto()

class InterpolationNodesDistribution(Enum):
    UNIFORM = "uniform"
    CHEBYSHEV = "chebyshev"
    
LINSPACE_START = 0
LINSPACE_STOP = 1

INTERPOLATION_NODES_COUNT = [5, 15, 50, 111]
