WIDTH = 25
HEIGHT = 6


def main():
    layers = []

    with open("input.txt") as input_file:
        data = input_file.read().strip()
        for i in range(len(data) // (WIDTH * HEIGHT)):
            layers.append(data[WIDTH * HEIGHT * i: WIDTH * HEIGHT * (i + 1)])

    image = [" "] * WIDTH * HEIGHT

    for i in range(WIDTH * HEIGHT):
        for layer in layers:
            if layer[i] == "0":
                image[i] = " "
                break
            elif layer[i] == "1":
                image[i] = "#"
                break

    image = "".join(image)

    for i in range(HEIGHT):
        print(image[WIDTH * i: WIDTH * (i + 1)])


if __name__ == "__main__":
    main()
