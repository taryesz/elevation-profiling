from interpolation.interpolation import interpolate
from data.data import import_data
from plotting.plotting import plot
from constants import InterpolationMethod, InterpolationNodesDistribution, INTERPOLATION_NODES_COUNT

DATA_FILES = input("File name that contains data (with the extention): ")

# Original data
real_data_x, real_data_y, real_data_count = import_data(DATA_FILES)

# Interpolation (Lagrange - Uniform)

for interpolation_nodes_count in INTERPOLATION_NODES_COUNT:
    interpolated_data_x, interpolated_data_y, interpolation_nodes_x, interpolation_nodes_y = interpolate(InterpolationMethod.LAGRANGE, InterpolationNodesDistribution.UNIFORM, interpolation_nodes_count, real_data_x, real_data_y, real_data_count)
    plot(interpolated_data_x, interpolated_data_y, interpolation_nodes_x, interpolation_nodes_y, interpolation_nodes_count, real_data_x, real_data_y, InterpolationMethod.LAGRANGE, InterpolationNodesDistribution.UNIFORM)

# Interpolation (Lagrange - Chebyshev)

for interpolation_nodes_count in INTERPOLATION_NODES_COUNT:
    interpolated_data_x, interpolated_data_y, interpolation_nodes_x, interpolation_nodes_y = interpolate(InterpolationMethod.LAGRANGE, InterpolationNodesDistribution.CHEBYSHEV, interpolation_nodes_count, real_data_x, real_data_y, real_data_count)
    plot(interpolated_data_x, interpolated_data_y, interpolation_nodes_x, interpolation_nodes_y, interpolation_nodes_count, real_data_x, real_data_y, InterpolationMethod.LAGRANGE, InterpolationNodesDistribution.CHEBYSHEV)

# Interpolation (Cubic Spline)

for interpolation_nodes_count in INTERPOLATION_NODES_COUNT:
    interpolated_data_x, interpolated_data_y, interpolation_nodes_x, interpolation_nodes_y = interpolate(InterpolationMethod.CUBIC_SPLINE, InterpolationNodesDistribution.UNIFORM, interpolation_nodes_count, real_data_x, real_data_y, real_data_count)
    plot(interpolated_data_x, interpolated_data_y, interpolation_nodes_x, interpolation_nodes_y, interpolation_nodes_count, real_data_x, real_data_y, InterpolationMethod.CUBIC_SPLINE)
