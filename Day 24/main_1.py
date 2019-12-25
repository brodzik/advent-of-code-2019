import numpy as np


def get_adjacent(grid, x, y, max_x, max_y):
    adjacent = 0

    if y + 1 < max_y and grid[y + 1, x]:
        adjacent += 1

    if x + 1 < max_x and grid[y, x + 1]:
        adjacent += 1

    if y - 1 >= 0 and grid[y - 1, x]:
        adjacent += 1

    if x - 1 >= 0 and grid[y, x - 1]:
        adjacent += 1

    return adjacent


def get_biodiversity_rating(grid, max_x, max_y):
    rating = 0

    for y in range(max_y):
        for x in range(max_x):
            if grid[y, x]:
                rating += 2**(y * max_y + x)

    return rating


def main():
    max_x = 5
    max_y = 5
    grid = np.zeros((max_y, max_x), dtype=int)

    with open("input.txt") as input_file:
        for i, line in enumerate(input_file):
            for j, c in enumerate(line.strip()):
                if c == "#":
                    grid[i, j] = 1

    hashes = []

    while True:
        grid_new = np.zeros((max_y, max_x), dtype=int)

        for y in range(max_y):
            for x in range(max_x):
                if grid[y, x]:
                    adjacent = get_adjacent(grid, x, y, max_x, max_y)

                    if adjacent == 1:
                        grid_new[y, x] = 1
                else:
                    adjacent = get_adjacent(grid, x, y, max_x, max_y)

                    if adjacent == 1 or adjacent == 2:
                        grid_new[y, x] = 1

        grid = grid_new.copy()
        grid_new[:, :] = 0

        hash_grid = hash(grid.data.tobytes())
        if hash_grid in hashes:
            print(grid)
            break
        else:
            hashes.append(hash_grid)

    print(get_biodiversity_rating(grid, max_x, max_y))


if __name__ == "__main__":
    main()
