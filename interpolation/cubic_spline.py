import numpy as np

def cubic_spline_segment(x, x_i):
    element = x - x_i
    return element**0, element**1, element**2, element**3


def cubic_spline_segment_derivative(x, x_i, x_i2):
    element = x - x_i
    element2 = x - x_i2
    return [0, 1, 2*element, 3*(element**2), 0, -1, -2*element2, -3*(element2**2)]


def cubic_spline_segment_secondary_derivative(x, x_i, x_i2):
    element = x - x_i
    element2 = x - x_i2
    return [0, 0, 2, 6*element, 0, 0, -2, -6*element2]


def temp(x, x_i):
    element = x - x_i
    return [0, 0, 2, 6*element]

def evaluate(interpolation_nodes_count, interpolation_nodes_x, interpolation_nodes_y):

    # 3 wezly -> 2 przedzialy -> macierz 8x8
    # 4 wezly -> 3 przedzialy -> macierz 12x12
    # x wezlow -> x-1 przedzialow -> macierz 4*(x-1)

    matrix_size = 4 * (interpolation_nodes_count - 1)
    matrix = [[0 for _ in range(matrix_size)] for _ in range(matrix_size)]
    y = [0 for _ in range(matrix_size)]

    # wartosc Y w kazdym wezle interpolacji wynosi Sx()
    # ale nie oznacza to to ze liczymy tylko raz
    # liczymy dla kazdego przedzialu, wiec wezly beda sie powtarzac

    # 3 wezly -> S0(x0), S0(x1) oraz S1(x1), S1(x2)
    # 4 wezly -> S0(x0), S0(x1) oraz S1(x1), S1(x2) oraz S2(x2), S2(x3)
    # itd...

    # na kazdy przedzial policzyc po 2 funkcji Sx(...):
    spline = 0
    row = 0
    for _ in range(interpolation_nodes_count - 1):
        matrix[row][spline*4:spline*4+4] = cubic_spline_segment(interpolation_nodes_x[spline], interpolation_nodes_x[spline])
        y[row] = interpolation_nodes_y[spline]
        row += 1
        matrix[row][spline*4:spline*4+4] = cubic_spline_segment(interpolation_nodes_x[spline+1], interpolation_nodes_x[spline])
        y[row] = interpolation_nodes_y[spline + 1]
        row += 1
        spline += 1

    # na kazdy wezel WEWNETRZNY policzyc ciaglosc pierwszej pochodnej
    spline = 0
    inner_interpolation_point = 1
    for _ in range(interpolation_nodes_count - 2):
        matrix[row][spline*4:spline*4+8] = cubic_spline_segment_derivative(interpolation_nodes_x[inner_interpolation_point], interpolation_nodes_x[spline], interpolation_nodes_x[spline+1])
        y[row] = 0
        row += 1
        spline += 1
        inner_interpolation_point += 1

    # na kazdy wezel WEWNETRZNY policzyc ciaglosc drugiej pochodnej
    spline = 0
    inner_interpolation_point = 1
    for _ in range(interpolation_nodes_count - 2):
        matrix[row][spline*4: spline*4+8] = cubic_spline_segment_secondary_derivative(interpolation_nodes_x[inner_interpolation_point], interpolation_nodes_x[spline], interpolation_nodes_x[spline+1])
        y[row] = 0
        row += 1
        spline += 1
        inner_interpolation_point += 1

    # warunki brzegowe (pierwszy i ostatni wezel)
    spline = 0
    matrix[row][spline*4:spline*4+4] = temp(interpolation_nodes_x[0], interpolation_nodes_x[spline])
    y[row] = 0
    row += 1
    spline = interpolation_nodes_count - 2
    matrix[row][spline*4:spline*4+4] = temp(interpolation_nodes_x[-1], interpolation_nodes_x[spline])
    y[row] = 0

    matrix_np = np.array(matrix, dtype=float)
    y_np = np.array(y, dtype=float)

    return np.linalg.solve(matrix_np, y_np)


def interpolate_using_cubic_spline(x, interpolation_nodes_count, interpolation_nodes_x, interpolation_nodes_y):
    coefficients = evaluate(interpolation_nodes_count, interpolation_nodes_x, interpolation_nodes_y)
    for i in range(interpolation_nodes_count - 1):
        if interpolation_nodes_x[i] <= x <= interpolation_nodes_x[i+1]:
            a0, a1, a2, a3 = coefficients[i*4:(i+1)*4]
            dx = x - interpolation_nodes_x[i]
            return a0 + a1*dx + a2*dx**2 + a3*dx**3
    # Jeśli x poza zakresem, zwróć None albo wartość krańcową
    return None
