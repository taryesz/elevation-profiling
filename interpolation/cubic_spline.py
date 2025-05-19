from numpy.linalg import solve
from numpy import array, ndarray, float64

def interpolate_using_cubic_spline(x:float, interpolation_nodes_count:int, interpolation_nodes_x:list[float], interpolation_nodes_y:list[float]) -> float:
    
    def _calculate_spline_coefficients(interpolation_nodes_count:int, interpolation_nodes_x:list[float], interpolation_nodes_y:list[float]) -> ndarray[float64]:

        # Define helper functions
        def _cubic_spline_segment(x:float, x_i:float):
            h = x - x_i
            return h**0, h**1, h**2, h**3


        def _cubic_spline_segment_derivative(x:float, x_i:float, x_j:float):
            h_1 = x - x_i
            h_2 = x - x_j
            return [0, 1, 2*h_1, 3*(h_1**2), 0, -1, -2*h_2, -3*(h_2**2)]


        def _cubic_spline_segment_secondary_derivative(x:float, x_i:float, x_j:float):
            h_1 = x - x_i
            h_2 = x - x_j
            return [0, 0, 2, 6*h_1, 0, 0, -2, -6*h_2]


        def _natural_boundary_conditions(x:float, x_i:float):
            h = x - x_i
            return [0, 0, 2, 6*h]
        

        # Create a matrix and a vector that store splines conditions
        matrix_size = 4 * (interpolation_nodes_count - 1)
        matrix = [[0 for _ in range(matrix_size)] for _ in range(matrix_size)]
        y = [0 for _ in range(matrix_size)]

        # Calculate polynomials for each pair of interpolation nodes
        spline = 0
        row = 0
        for _ in range(interpolation_nodes_count - 1):

            # S_{i}(x_{j}), where x_{j} is the first interpolation node from the current range:
            matrix[row][spline*4:spline*4+4] = _cubic_spline_segment(interpolation_nodes_x[spline], interpolation_nodes_x[spline])
            y[row] = interpolation_nodes_y[spline]
            
            row += 1

            # S_{i}(x_{j+1}), where x_{j+1} is the second interpolation node from the current range:
            matrix[row][spline*4:spline*4+4] = _cubic_spline_segment(interpolation_nodes_x[spline+1], interpolation_nodes_x[spline])
            y[row] = interpolation_nodes_y[spline + 1]
            
            row += 1
            spline += 1

        # Calculate continuity of the first derivative for each inner interpolation node
        spline = 0
        inner_interpolation_point = 1
        for _ in range(interpolation_nodes_count - 2):

            # S_{i}'(x_{j}) = S_{i+1}'(x_{j}), where x_{j} is an inner interpolation node:
            matrix[row][spline*4:spline*4+8] = _cubic_spline_segment_derivative(interpolation_nodes_x[inner_interpolation_point], interpolation_nodes_x[spline], interpolation_nodes_x[spline+1])
            y[row] = 0

            row += 1
            spline += 1
            inner_interpolation_point += 1

        # Calculate continuity of the second derivative for each inner interpolation node
        spline = 0
        inner_interpolation_point = 1
        for _ in range(interpolation_nodes_count - 2):

            # S_{i}''(x_{j}) = S_{i+1}''(x_{j}), where x_{j} is an inner interpolation node:
            matrix[row][spline*4: spline*4+8] = _cubic_spline_segment_secondary_derivative(interpolation_nodes_x[inner_interpolation_point], interpolation_nodes_x[spline], interpolation_nodes_x[spline+1])
            y[row] = 0
            
            row += 1
            spline += 1
            inner_interpolation_point += 1

        # Calculate natural boundary conditions (only for the first and the last interpolation nodes)
        spline = 0
        matrix[row][spline*4:spline*4+4] = _natural_boundary_conditions(interpolation_nodes_x[0], interpolation_nodes_x[spline])
        y[row] = 0
        
        row += 1
        
        spline = interpolation_nodes_count - 2
        matrix[row][spline*4:spline*4+4] = _natural_boundary_conditions(interpolation_nodes_x[-1], interpolation_nodes_x[spline])
        y[row] = 0

        # Convert the resulting lists to NumPy's arrays for the convenience
        matrix = array(matrix, dtype=float)
        y = array(y, dtype=float)

        # Solve the matrix equation (AKA find the coefficients)
        return solve(matrix, y)


    coefficients = _calculate_spline_coefficients(interpolation_nodes_count, interpolation_nodes_x, interpolation_nodes_y)
    
    # Find a range to which the current evaluated node belongs to
    for i in range(interpolation_nodes_count - 1):
        if interpolation_nodes_x[i] <= x <= interpolation_nodes_x[i+1]:
            a, b, c, d = coefficients[i*4:(i+1)*4]
            dx = x - interpolation_nodes_x[i]
            return a + b*dx + c*dx**2 + d*dx**3
    
    # If x is out of bounds ...
    return None
