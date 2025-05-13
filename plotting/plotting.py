import matplotlib.pyplot as plt

def plot(interpolated_data_x, interpolated_data_y, interpolation_nodes_count, real_data_x=None, real_data_y=None):
    
    plt.figure(figsize=(12, 6))
    
    if real_data_x is not None and real_data_y is not None: plt.plot(real_data_x, real_data_y, color='orange', label='Original Data')
    
    plt.plot(interpolated_data_x, interpolated_data_y, label='Lagrange Interpolation', color='blue')

    plt.yscale('log')
    plt.title(f'Elevation Profile [Lagrange Interpolation, {interpolation_nodes_count} Interpolation Nodes]')
    plt.xlabel('Distance')
    plt.ylabel('Elevation [Logarithmic Scale]')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()