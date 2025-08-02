import numpy as np


def read_data(filepath: str):
    x_coords = []
    y_coords = []
    with open(filepath, "r") as f:
        for line in f:
            if line[0].isdigit():
                v, x, y = line.strip().split(" ")
                x_coords.append(float(x))
                y_coords.append(float(y))

    return np.array([x_coords, y_coords])


def main():
    cities = read_data(filepath="./data/dj38.tsp")
    print(cities)
    print(cities[:, 0])


if __name__ == "__main__":
    main()
