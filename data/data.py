def import_data() -> tuple[list[float], list[float], int]:

    x = []
    y = []
    line_count = 0

    with open("data/data.txt", "r") as file:
        for line in file:
            if line.strip():  # pomija puste linie
                xi, yi = map(float, line.strip().split())
                x.append(xi)
                y.append(yi)
                line_count += 1

    return x, y, line_count
