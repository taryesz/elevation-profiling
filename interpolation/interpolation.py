from interpolation.lagrange import interpolate_using_lagrange
from constants import *

def interpolate(method:InterpolationMethod, interpolation_nodes_count:int, real_data_x:list, real_data_y:list, real_data_count:int) -> tuple[list, list]:
    
    def linspace(start, stop, count) -> list:
        if count == 1: return [start]  
        step = (stop - start) / (count - 1)
        return [start + i * step for i in range(count)]
    

    def select_evenly_spaced_nodes(real_data_x: list, real_data_y: list, count: int) -> tuple[list, list]:
        
        if count <= 0: return [], []

        if count == 1:
            mid_index = len(real_data_x) // 2
            return [real_data_x[mid_index]], [real_data_y[mid_index]]

        step = (len(real_data_x) - 1) / (count - 1)
        indices = [round(i * step) for i in range(count)]
        
        selected_x = [real_data_x[i] for i in indices]
        selected_y = [real_data_y[i] for i in indices]
        
        return selected_x, selected_y


    def scale(data) -> list:
        return [(x - min(data)) / (max(data) - min(data)) for x in real_data_x]
    

    def descale(data) -> list:
        return [x * (max(data) - min(data)) + min(data) for x in evaluation_points_x]


    match method:
        case method.LAGRANGE:
            
            # Uniformly select N nodes that will be used to interpolate other nodes with unknown Y-values
            interpolation_nodes_x, interpolation_nodes_y = select_evenly_spaced_nodes(scale(real_data_x), real_data_y, interpolation_nodes_count)

            # Uniformly select N nodes (specifically their indices) whose Y-values are unknown and will be calculated using interpolation
            evaluation_points_x = linspace(LINSPACE_START, LINSPACE_STOP, real_data_count)
            evaluation_points_y = []

            # For each "unknown node" evaluate its value using interpolation 
            for x in evaluation_points_x:
                evaluation_points_y.append(interpolate_using_lagrange(x, interpolation_nodes_count, interpolation_nodes_x, interpolation_nodes_y))

            # Scale the X-values back to the original scale
            evaluation_points_x = descale(real_data_x)
            
            return evaluation_points_x, evaluation_points_y

        # TODO:
        case method.CUBIC_SPLINE:
            pass
