import matplotlib.pyplot as plt

from constants import *

def plot(interpolated_data_x, interpolated_data_y, interpolation_nodes_count, real_data_x, real_data_y, method:InterpolationMethod):
    
    plt.figure(figsize=(12, 6))
    
    plt.plot(real_data_x, real_data_y, color='orange', label='Original Data')
    
    match method:
        case method.LAGRANGE:
            description = "Lagrange"
        case method.CUBIC_SPLINE:
            description = "Cubic Spline"
    
    plt.plot(interpolated_data_x, interpolated_data_y, label=f'{description} Interpolation', color='blue')

    plt.yscale('log')
    plt.title(f'Elevation Profile [{description} Interpolation, {interpolation_nodes_count} Interpolation Nodes]')
    plt.xlabel('Distance')
    plt.ylabel('Elevation [Logarithmic Scale]')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()