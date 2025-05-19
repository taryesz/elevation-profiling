from interpolation.interpolation import interpolate
from data.data import import_data
from plotting.plotting import plot
from constants import InterpolationMethod, InterpolationNodesDistribution

# Original data
real_data_x, real_data_y, real_data_count = import_data()

INTERPOLATION_NODES_COUNT = [6, 11, 16, 26, 52, 103]

# Interpolation (Lagrange - Uniform)

for interpolation_nodes_count in INTERPOLATION_NODES_COUNT:
    interpolated_data_x, interpolated_data_y = interpolate(InterpolationMethod.LAGRANGE, InterpolationNodesDistribution.UNIFORM, interpolation_nodes_count, real_data_x, real_data_y, real_data_count)
    plot(interpolated_data_x, interpolated_data_y, interpolation_nodes_count, real_data_x, real_data_y, InterpolationMethod.LAGRANGE)

# Interpolation (Lagrange - Chebyshev)

for interpolation_nodes_count in INTERPOLATION_NODES_COUNT:
    interpolated_data_x, interpolated_data_y = interpolate(InterpolationMethod.LAGRANGE, InterpolationNodesDistribution.CHEBYSHEV, interpolation_nodes_count, real_data_x, real_data_y, real_data_count)
    plot(interpolated_data_x, interpolated_data_y, interpolation_nodes_count, real_data_x, real_data_y, InterpolationMethod.LAGRANGE)

# Interpolation (Cubic Spline)

for interpolation_nodes_count in INTERPOLATION_NODES_COUNT:
    interpolated_data_x, interpolated_data_y = interpolate(InterpolationMethod.CUBIC_SPLINE, InterpolationNodesDistribution.UNIFORM, interpolation_nodes_count, real_data_x, real_data_y, real_data_count)
    plot(interpolated_data_x, interpolated_data_y, interpolation_nodes_count, real_data_x, real_data_y, InterpolationMethod.CUBIC_SPLINE)
