def interpolate_using_lagrange(x:float, interpolation_nodes_count:int, interpolation_nodes_x:list[float], interpolation_nodes_y:list[float]) -> float:

    def _lagrange_basis_polynomial(x:float, i:int, interpolation_nodes_count:int, interpolation_nodes_x:list[float]) -> float:

        result = 1.0

        for j in range(interpolation_nodes_count):
            if j == i: continue
            result *= (x - interpolation_nodes_x[j]) / (interpolation_nodes_x[i] - interpolation_nodes_x[j])

        return result


    result = 0.0

    for sum_counter, interpolation_node_y in enumerate(interpolation_nodes_y):
        result += interpolation_node_y * _lagrange_basis_polynomial(x, sum_counter, interpolation_nodes_count, interpolation_nodes_x)

    return result
