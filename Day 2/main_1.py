def main():
    with open("input.txt") as input_file:
        data = [int(x) for x in input_file.readline().split(",")]
        data[1] = 12
        data[2] = 2

        i = 0
        while i < len(data):
            if data[i] == 1:
                data[data[i + 3]] = data[data[i + 1]] + data[data[i + 2]]
            elif data[i] == 2:
                data[data[i + 3]] = data[data[i + 1]] * data[data[i + 2]]
            elif data[i] == 99:
                break
            i += 4

        print(data)


if __name__ == "__main__":
    main()
