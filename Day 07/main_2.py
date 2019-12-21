import copy
import itertools


class IntcodeVM:
    def __init__(self, data, phase):
        self.data = copy.copy(data)
        self.ip = 0
        self.set_param(1, phase)
        self.ip += 2

    def run(self, input_data):
        while self.data[self.ip] != 99:
            opcode = self.data[self.ip] % 100

            if opcode == 1:
                self.set_param(3, self.get_param(1) + self.get_param(2))
                self.ip += 4
            elif opcode == 2:
                self.set_param(3, self.get_param(1) * self.get_param(2))
                self.ip += 4
            elif opcode == 3:
                self.set_param(1, input_data)
                self.ip += 2
            elif opcode == 4:
                output = self.get_param(1)
                self.ip += 2
                return output
            elif opcode == 5:
                self.ip = self.get_param(2) if self.get_param(1) else self.ip + 3
            elif opcode == 6:
                self.ip = self.get_param(2) if not self.get_param(1) else self.ip + 3
            elif opcode == 7:
                self.set_param(3, self.get_param(1) < self.get_param(2))
                self.ip += 4
            elif opcode == 8:
                self.set_param(3, self.get_param(1) == self.get_param(2))
                self.ip += 4
            else:
                raise Exception("Unknown instruction: {}".format(opcode))

        return 0

    def is_running(self):
        return self.data[self.ip] != 99

    def get_param(self, index):
        if (self.data[self.ip] // (10**(index + 1))) % 10:
            return self.data[self.ip + index]
        else:
            return self.data[self.data[self.ip + index]]

    def set_param(self, index, value):
        if (self.data[self.ip] // (10**(index + 1))) % 10:
            self.data[self.ip + index] = value
        else:
            self.data[self.data[self.ip + index]] = value


def main():
    with open("input.txt") as input_file:
        data = [int(x) for x in input_file.readline().split(",")]

    result = 0

    for phases in itertools.permutations([5, 6, 7, 8, 9]):
        machines = [IntcodeVM(data, phase) for phase in phases]
        signal = 0

        while machines[0].is_running():
            for machine in machines:
                signal = machine.run(signal)
                result = max(result, signal)

    print(result)


if __name__ == "__main__":
    main()
