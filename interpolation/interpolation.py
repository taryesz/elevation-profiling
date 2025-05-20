from interpolation.lagrange import interpolate_using_lagrange
from interpolation.cubic_spline import interpolate_using_cubic_spline
from constants import *
from math import cos, pi

def interpolate(method:InterpolationMethod, interpolation_nodes_distribution:InterpolationNodesDistribution, interpolation_nodes_count:int, real_data_x:list[float], real_data_y:list[float], real_data_count:int) -> tuple[list, list]:
    
    def _linspace(start:int, stop:int, count:int) -> list[float]:
        if count == 1: return [start]  
        step = (stop - start) / (count - 1)
        return [start + i * step for i in range(count)]
    

    def _select_evenly_spaced_nodes(real_data_x: list[float], real_data_y: list[float], count: int) -> tuple[list[float], list[float]]:
        
        if count == 1:
            mid_index = len(real_data_x) // 2
            return [real_data_x[mid_index]], [real_data_y[mid_index]]

        step = (len(real_data_x) - 1) / (count - 1)
        indices = [round(i * step) for i in range(count)]
        
        selected_x = [real_data_x[i] for i in indices]
        selected_y = [real_data_y[i] for i in indices]
        
        return selected_x, selected_y


    def _select_chebyshev_nodes(real_data_x: list[float], real_data_y: list[float], count: int) -> tuple[list[float], list[float]]:
        
        # Create a Chebyshev range scaled on [0, 1]
        chebyshev_nodes = [0.5 * (1 + cos((2 * k + 1) * pi / (2 * count))) for k in range(count)]

        selected_x = []
        selected_y = []
        used_indices = set()

        for node in chebyshev_nodes:

            # Create a list of available indices of potential interpolation nodes
            candidates = [i for i in range(len(real_data_x)) if i not in used_indices]
            if not candidates: break

            # Find the closest node to the selected index
            closest_index = min(candidates, key=lambda i: abs(real_data_x[i] - node))
            
            # Use this node as a Chebyshev one (now it's scaled to the real data, not [0, 1])
            selected_x.append(real_data_x[closest_index])
            selected_y.append(real_data_y[closest_index])

            # Mark to omit repetitions
            used_indices.add(closest_index)

        return selected_x, selected_y
    

    def _scale(data) -> list[float]:
        return [(x - min(data)) / (max(data) - min(data)) for x in real_data_x]
 

    def _unscale(data) -> list[float]:
        return [x * (max(real_data_x) - min(real_data_x)) + min(real_data_x) for x in data]


    match interpolation_nodes_distribution:
        case interpolation_nodes_distribution.UNIFORM:
            # Uniformly select N nodes that will be used to interpolate other nodes with unknown Y-values
            interpolation_nodes_x, interpolation_nodes_y = _select_evenly_spaced_nodes(_scale(real_data_x), real_data_y, interpolation_nodes_count)
        case interpolation_nodes_distribution.CHEBYSHEV:
            # Select N nodes using Chebyshev method that will be used to interpolate other nodes with unknown Y-values reducing Runge effect
            interpolation_nodes_x, interpolation_nodes_y = _select_chebyshev_nodes(_scale(real_data_x), real_data_y, interpolation_nodes_count)

    # Uniformly select N nodes (specifically their indices) whose Y-values are unknown and will be calculated using interpolation
    evaluation_points_x = _linspace(LINSPACE_START, LINSPACE_STOP, real_data_count)
    evaluation_points_y = []

    # For each evaluated node find its value using interpolation 
    match method:
        case method.LAGRANGE:
            for x in evaluation_points_x:
                evaluation_points_y.append(interpolate_using_lagrange(x, interpolation_nodes_count, interpolation_nodes_x, interpolation_nodes_y))
        case method.CUBIC_SPLINE:
            for x in evaluation_points_x:
                evaluation_points_y.append(interpolate_using_cubic_spline(x, interpolation_nodes_count, interpolation_nodes_x, interpolation_nodes_y))

    # Scale the X-values and the X-interpolation nodes back to the original scale
    evaluation_points_x = real_data_x
    interpolation_nodes_x = _unscale(interpolation_nodes_x)

    return evaluation_points_x, evaluation_points_y, interpolation_nodes_x, interpolation_nodes_y
