import matplotlib.pyplot as plt

from constants import *

def plot(interpolated_data_x, interpolated_data_y, interpolation_nodes_x, interpolation_nodes_y, interpolation_nodes_count, real_data_x, real_data_y, method:InterpolationMethod, interpolation_nodes_distribution:InterpolationNodesDistribution = InterpolationNodesDistribution.UNIFORM):
    
    plt.figure(figsize=(12, 6))
    
    plt.plot(real_data_x, real_data_y, color='orange', label='Original Data')
    
    match method:
        case method.LAGRANGE:
            description = f"Lagrange {interpolation_nodes_distribution.value.capitalize()}" 
        case method.CUBIC_SPLINE:
            description = "Cubic Spline"
    
    plt.plot(interpolated_data_x, interpolated_data_y, label=f'{description} Interpolation', color='blue')

    plt.plot(interpolation_nodes_x, interpolation_nodes_y, 'go', label='Interpolation Nodes')  

    plt.yscale('log')
    plt.title(f'Elevation Profile [{description} Interpolation, {interpolation_nodes_count} Interpolation Nodes]')
    plt.xlabel('Distance')
    plt.ylabel('Elevation [Logarithmic Scale]')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"data/results/{description.lower().replace(" ", "-")}-{interpolation_nodes_count}.png")
    plt.show()