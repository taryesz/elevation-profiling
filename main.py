from interpolation.interpolation import interpolate
from data.data import import_data
from plotting.plotting import plot
from constants import *

# Original data
real_data_x, real_data_y, real_data_count = import_data()

# Interpolation
interpolation_nodes_count = [6, 11, 16, 26, 52, 103]

for current_interpolation_nodes_count in interpolation_nodes_count:
    interpolated_data_x, interpolated_data_y = interpolate(InterpolationMethod.LAGRANGE, current_interpolation_nodes_count, real_data_x, real_data_y, real_data_count)
    plot(interpolated_data_x, interpolated_data_y, current_interpolation_nodes_count, real_data_x, real_data_y)
