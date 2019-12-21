import math


def main():
    with open("input.txt") as input_file:
        data = input_file.read().strip()
        min_zeros = math.inf
        result = math.inf
        for i in range(len(data) // (25 * 6)):
            layer = data[25 * 6 * i: 25 * 6 * (i + 1)]
            if layer.count("0") < min_zeros:
                min_zeros = layer.count("0")
                result = layer.count("1") * layer.count("2")
        print(result)


if __name__ == "__main__":
    main()
