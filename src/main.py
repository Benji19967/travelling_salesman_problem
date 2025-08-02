def read_data(filepath: str):
    with open(filepath, "r") as f:
        for line in f:
            if line[0].isdigit():
                v, x, y = line.strip().split(" ")
                print(v, x, y)


def main():
    read_data(filepath="./data/dj38.tsp")


if __name__ == "__main__":
    main()
