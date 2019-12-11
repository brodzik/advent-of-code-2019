import copy
import itertools
from collections import defaultdict


class IntcodeVM:
    def __init__(self, data):
        self.data = copy.copy(data)
        self.ip = 0
        self.rel = 0

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
            elif opcode == 9:
                self.rel += self.get_param(1)
                self.ip += 2
            else:
                raise Exception("Unknown instruction: {}".format(opcode))

        return 0

    def is_running(self):
        return self.data[self.ip] != 99

    def get_param(self, index):
        mode = self.data[self.ip] // 10**(index + 1) % 10

        if mode == 0:
            return self.data[self.data[self.ip + index]]
        elif mode == 1:
            return self.data[self.ip + index]
        elif mode == 2:
            return self.data[self.rel + self.data[self.ip + index]]

    def set_param(self, index, value):
        mode = self.data[self.ip] // 10**(index + 1) % 10

        if mode == 0:
            self.data[self.data[self.ip + index]] = value
        elif mode == 1:
            self.data[self.ip + index] = value
        elif mode == 2:
            self.data[self.rel + self.data[self.ip + index]] = value


def main():
    with open("input.txt") as input_file:
        data = [int(x) for x in input_file.readline().split(",")]
        data.extend([0] * 10 * len(data))

    machine = IntcodeVM(data)
    grid = defaultdict(int)
    grid[(0, 0)] = 1
    x, y = (0, 0)
    angle = 0

    while machine.is_running():
        if (x, y) not in grid:
            grid[(x, y)] = machine.run(0)
            direction = machine.run(0)
        else:
            old_color = grid[(x, y)]
            new_color = machine.run(old_color)
            direction = machine.run(old_color)
            grid[(x, y)] = new_color

        if direction == 0:
            angle = (angle + 270) % 360
        elif direction == 1:
            angle = (angle + 90) % 360

        if angle == 0:
            y += 1
        elif angle == 90:
            x += 1
        elif angle == 180:
            y -= 1
        elif angle == 270:
            x -= 1

    min_x = min([p[0] for p in grid])
    max_x = max([p[0] for p in grid])

    min_y = min([p[1] for p in grid])
    max_y = max([p[1] for p in grid])

    for y in range(max_y, min_y - 1, -1):
        line = ""

        for x in range(min_x, max_x):
            line += "#" if grid[(x, y)] == 1 else " "

        print(line)


if __name__ == "__main__":
    main()
