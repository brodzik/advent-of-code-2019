import copy


def main():
    with open("input.txt") as input_file:
        data = [int(x) for x in input_file.readline().split(",")]

        for noun in range(100):
            for verb in range(100):
                try:
                    temp = copy.deepcopy(data)
                    temp[1] = noun
                    temp[2] = verb

                    i = 0
                    while i < len(temp):
                        if temp[i] == 1:
                            temp[temp[i + 3]] = temp[temp[i + 1]] + temp[temp[i + 2]]
                        elif temp[i] == 2:
                            temp[temp[i + 3]] = temp[temp[i + 1]] * temp[temp[i + 2]]
                        elif temp[i] == 99:
                            break
                        i += 4

                    if temp[0] == 19690720:
                        print(100 * noun + verb)
                        return
                except:
                    pass


if __name__ == "__main__":
    main()
