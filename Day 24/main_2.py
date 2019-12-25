import numpy as np
from tqdm import tqdm


def get_adjacent(grid, x, y, z, max_x, max_y, max_z):
    adjacent = 0

    if y + 1 < max_y:
        if grid[z, y + 1, x] == 1:
            adjacent += 1
        elif grid[z, y + 1, x] == 2:
            for i in range(max_x):
                if grid[z + 1, 0, i] == 1:
                    adjacent += 1

    if y + 1 == max_y:
        if grid[z - 1, 3, 2] == 1:
            adjacent += 1

    if x + 1 < max_x:
        if grid[z, y, x + 1] == 1:
            adjacent += 1
        elif grid[z, y, x + 1] == 2:
            for i in range(max_y):
                if grid[z + 1, i, 0] == 1:
                    adjacent += 1
    if x + 1 == max_x:
        if grid[z - 1, 2, 3] == 1:
            adjacent += 1

    if y - 1 >= 0:
        if grid[z, y - 1, x] == 1:
            adjacent += 1
        elif grid[z, y - 1, x] == 2:
            for i in range(max_x):
                if grid[z + 1, max_y - 1, i] == 1:
                    adjacent += 1
    if y - 1 == -1:
        if grid[z - 1, 1, 2] == 1:
            adjacent += 1

    if x - 1 >= 0:
        if grid[z, y, x - 1] == 1:
            adjacent += 1
        elif grid[z, y, x - 1] == 2:
            for i in range(max_y):
                if grid[z + 1, i, max_x - 1] == 1:
                    adjacent += 1
    if x - 1 == -1:
        if grid[z - 1, 2, 1] == 1:
            adjacent += 1

    return adjacent


def main():
    max_x = 5
    max_y = 5
    max_z = 1000

    grid = np.zeros((max_z, max_y, max_x), dtype=int)

    with open("input.txt") as input_file:
        for y, line in enumerate(input_file):
            for x, c in enumerate(line.strip()):
                if c == "#":
                    grid[max_z // 2, y, x] = 1

    grid[1:max_z - 1, 2, 2] = 2

    for _ in tqdm(range(200)):
        grid_new = np.zeros((max_z, max_y, max_x), dtype=int)
        grid_new[1:max_z - 1, 2, 2] = 2

        for z in range(max_z):
            for y in range(max_y):
                for x in range(max_x):
                    if grid[z, y, x] == 1:
                        adjacent = get_adjacent(grid, x, y, z, max_x, max_y, max_z)

                        if adjacent == 1:
                            grid_new[z, y, x] = 1
                    elif grid[z, y, x] == 0:
                        adjacent = get_adjacent(grid, x, y, z, max_x, max_y, max_z)

                        if adjacent == 1 or adjacent == 2:
                            grid_new[z, y, x] = 1

        grid = grid_new.copy()
        grid_new[:, :, :] = 0

    print((grid == 1).sum())


if __name__ == "__main__":
    main()
