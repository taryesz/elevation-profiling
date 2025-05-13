def lagrange_basis_polynomial(x, i, interpolation_nodes_count, interpolation_nodes_x):

    result = 1.0

    for j in range(interpolation_nodes_count):
        if j == i: continue
        result *= (x - interpolation_nodes_x[j]) / (interpolation_nodes_x[i] - interpolation_nodes_x[j])

    return result


def interpolate_using_lagrange(x, interpolation_nodes_count, interpolation_nodes_x, interpolation_nodes_y):

    result = 0.0

    for sum_counter, interpolation_node_y in enumerate(interpolation_nodes_y):
        result += interpolation_node_y * lagrange_basis_polynomial(x, sum_counter, interpolation_nodes_count, interpolation_nodes_x)

    return result
