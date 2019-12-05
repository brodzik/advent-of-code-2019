def main():
    with open("input.txt") as input_file:
        data = [int(x) for x in input_file.readline().split(",")]
        inputs = [5]
        outputs = []

        i = 0
        while i < len(data):
            if data[i] == 99:
                break

            opcode = data[i] % 100
            modes = [data[i] // 100 % 10, data[i] // 1000 % 10, data[i] // 10000 % 10]

            if opcode == 1:
                data[data[i + 3]] = (data[i + 1] if modes[0] else data[data[i + 1]]) + (data[i + 2] if modes[1] else data[data[i + 2]])
                i += 4
            elif opcode == 2:
                data[data[i + 3]] = (data[i + 1] if modes[0] else data[data[i + 1]]) * (data[i + 2] if modes[1] else data[data[i + 2]])
                i += 4
            elif opcode == 3:
                data[data[i + 1]] = inputs.pop(0)
                i += 2
            elif opcode == 4:
                outputs.append(data[i + 1] if modes[0] else data[data[i + 1]])
                i += 2
            elif opcode == 5:
                if (data[i + 1] if modes[0] else data[data[i + 1]]) != 0:
                    i = data[i + 2] if modes[1] else data[data[i + 2]]
                else:
                    i += 3
            elif opcode == 6:
                if (data[i + 1] if modes[0] else data[data[i + 1]]) == 0:
                    i = data[i + 2] if modes[1] else data[data[i + 2]]
                else:
                    i += 3
            elif opcode == 7:
                if (data[i + 1] if modes[0] else data[data[i + 1]]) < (data[i + 2] if modes[1] else data[data[i + 2]]):
                    data[data[i + 3]] = 1
                else:
                    data[data[i + 3]] = 0
                i += 4
            elif opcode == 8:
                if (data[i + 1] if modes[0] else data[data[i + 1]]) == (data[i + 2] if modes[1] else data[data[i + 2]]):
                    data[data[i + 3]] = 1
                else:
                    data[data[i + 3]] = 0
                i += 4
            else:
                raise Exception("Unknown instruction: {}".format(data[i]))

        print(outputs)


if __name__ == "__main__":
    main()
