def import_data(file_name:str) -> tuple[list[float], list[float], int]:

    x = []
    y = []
    line_count = 0

    with open(f"data/{file_name}", "r") as file:
        for line in file:
            if line.strip(): 
                x_i, y_i = map(float, line.strip().split())
                x.append(x_i)
                y.append(y_i)
                line_count += 1

    return x, y, line_count
