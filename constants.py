from enum import Enum, auto

class InterpolationMethod(Enum):
    LAGRANGE = auto()
    CUBIC_SPLINE = auto()
    
LINSPACE_START = 0
LINSPACE_STOP = 1