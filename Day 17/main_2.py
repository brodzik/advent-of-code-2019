import copy


class IntcodeVM:
    def __init__(self, data, inputs=None):
        self.data = copy.copy(data)
        self.ip = 0
        self.rel = 0
        self.inputs = inputs

    def run(self, input_data=0):
        while self.data[self.ip] != 99:
            opcode = self.data[self.ip] % 100

            if opcode == 1:
                self.set_param(3, self.get_param(1) + self.get_param(2))
                self.ip += 4
            elif opcode == 2:
                self.set_param(3, self.get_param(1) * self.get_param(2))
                self.ip += 4
            elif opcode == 3:
                #self.set_param(1, input_data)
                if self.inputs:
                    self.set_param(1, self.inputs.pop(0))
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


def get_start(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "^":
                return (x, y)


def get_dir_change(direction, prev_direction):
    if (prev_direction == "U" and direction == "R") or (prev_direction == "R" and direction == "D") or (prev_direction == "D" and direction == "L") or (prev_direction == "L" and direction == "U"):
        return "R"
    else:
        return "L"


def main():
    with open("input.txt") as input_file:
        data = [int(x) for x in input_file.readline().split(",")]
        data.extend([0] * 10 * len(data))
        data[0] = 2

    machine = IntcodeVM(data)

    grid = []
    line = ""

    while machine.is_running():
        output = machine.run(0)

        if output == 35:
            line += "#"
        elif output == 46:
            line += "."
        elif output == 94:
            line += "^"
        elif output == 10:
            grid.append(line)
            line = ""
        else:
            print(chr(output))

    grid = grid[:-4]

    for line in grid:
        print(line)

    max_x, max_y = len(grid[0]) - 1, len(grid) - 1
    min_x, min_y = 0, 0
    x, y = get_start(grid)
    prev_x, prev_y = None, None
    direction = None
    prev_direction = "U"

    commands = []
    count = 0

    while True:
        if direction == "U":
            if y - 1 >= min_y and grid[y - 1][x] == "#":
                count += 1
                prev_x, prev_y = x, y
                y -= 1
            else:
                commands.append("{},{}".format(get_dir_change(direction, prev_direction), count))
                prev_direction = direction
                direction = None
                count = 0
        elif direction == "R":
            if x + 1 <= max_x and grid[y][x + 1] == "#":
                count += 1
                prev_x, prev_y = x, y
                x += 1
            else:
                commands.append("{},{}".format(get_dir_change(direction, prev_direction), count))
                prev_direction = direction
                direction = None
                count = 0
        elif direction == "D":
            if y + 1 <= max_y and grid[y + 1][x] == "#":
                count += 1
                prev_x, prev_y = x, y
                y += 1
            else:
                commands.append("{},{}".format(get_dir_change(direction, prev_direction), count))
                prev_direction = direction
                direction = None
                count = 0
        elif direction == "L":
            if x - 1 >= min_x and grid[y][x - 1] == "#":
                count += 1
                prev_x, prev_y = x, y
                x -= 1
            else:
                commands.append("{},{}".format(get_dir_change(direction, prev_direction), count))
                prev_direction = direction
                direction = None
                count = 0
        else:
            if y - 1 >= min_y and grid[y - 1][x] == "#" and y - 1 != prev_y:
                direction = "U"
            elif x + 1 <= max_x and grid[y][x + 1] == "#" and x + 1 != prev_x:
                direction = "R"
            elif y + 1 <= max_y and grid[y + 1][x] == "#" and y + 1 != prev_y:
                direction = "D"
            elif x - 1 >= min_x and grid[y][x - 1] == "#" and x - 1 != prev_x:
                direction = "L"
            else:
                break

    print(",".join(commands))
    inputs = [ord(c) for c in "A,B,A,C,B,A,B,C,C,B\nL,12,L,12,R,4\nR,10,R,6,R,4,R,4\nR,6,L,12,L,12\nn\n"]
    machine = IntcodeVM(data, inputs)

    while machine.is_running():
        print(machine.run())


if __name__ == "__main__":
    main()
