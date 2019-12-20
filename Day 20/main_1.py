import numpy as np


def get_coord(grid, name, max_x, max_y):
    coords = []

    for y in range(max_y):
        for x in range(max_x):
            if grid[y][x] == name[0]:
                if grid[y + 1][x] == name[1]:
                    if y + 2 < max_y and grid[y + 2][x] == ".":
                        coords.append((x, y + 2))
                    elif y - 1 >= 0 and grid[y - 1][x] == ".":
                        coords.append((x, y - 1))
                elif grid[y][x + 1] == name[1]:
                    if x + 2 < max_x and grid[y][x + 2] == ".":
                        coords.append((x + 2, y))
                    elif x - 1 >= 0 and grid[y][x - 1] == ".":
                        coords.append((x - 1, y))

    return coords


def get_name(grid, x, y, max_x, max_y):
    c1 = grid[y][x]

    if c1 != "." and c1 != "#" and c1 != " ":
        if y - 1 >= 0:
            c2 = grid[y - 1][x]
            if c2 != "." and c2 != "#" and c2 != " ":
                return "".join([c2, c1])

        if y + 1 <= max_y:
            c2 = grid[y + 1][x]
            if c2 != "." and c2 != "#" and c2 != " ":
                return "".join([c1, c2])

        if x - 1 >= 0:
            c2 = grid[y][x - 1]
            if c2 != "." and c2 != "#" and c2 != " ":
                return "".join([c2, c1])

        if x + 1 <= max_x:
            c2 = grid[y][x + 1]
            if c2 != "." and c2 != "#" and c2 != " ":
                return "".join([c1, c2])

    return None


def main():
    grid = []

    with open("input.txt") as input_file:
        for line in input_file:
            grid.append(line[:-1])

    max_x, max_y = len(grid[0]) - 1, len(grid) - 1

    start = get_coord(grid, "AA", max_x, max_y)[0]
    end = get_coord(grid, "ZZ", max_x, max_y)[0]

    queue = []
    visited = np.array([[False] * (max_x + 1)] * (max_y + 1))
    dist = np.array([[10**10] * (max_x + 1)] * (max_y + 1))

    queue.append(start)
    visited[start[1], start[0]] = True
    dist[start[1], start[0]] = 0

    while queue:
        x, y = queue.pop(0)
        print(x, y)

        if ((x, y) == end):
            print(dist[y, x])
            break

        if y - 1 >= 0 and not visited[y - 1, x]:
            c = grid[y - 1][x]

            if c == ".":
                queue.append((x, y - 1))
                visited[y - 1, x] = True
                dist[y - 1, x] = dist[y, x] + 1

            name = get_name(grid, x, y - 1, max_x, max_y)
            if name:
                for cx, cy in get_coord(grid, name, max_x, max_y):
                    if not visited[cy, cx]:
                        queue.append((cx, cy))
                        visited[cy, cx] = True
                        dist[cy, cx] = dist[y, x] + 1

        if y + 1 <= max_y and not visited[y + 1, x]:
            c = grid[y + 1][x]

            if c == ".":
                queue.append((x, y + 1))
                visited[y + 1, x] = True
                dist[y + 1, x] = dist[y, x] + 1

            name = get_name(grid, x, y + 1, max_x, max_y)
            if name:
                for cx, cy in get_coord(grid, name, max_x, max_y):
                    if not visited[cy, cx]:
                        queue.append((cx, cy))
                        visited[cy, cx] = True
                        dist[cy, cx] = dist[y, x] + 1

        if x - 1 >= 0 and not visited[y, x - 1]:
            c = grid[y][x - 1]

            if c == ".":
                queue.append((x - 1, y))
                visited[y, x - 1] = True
                dist[y, x - 1] = dist[y, x] + 1

            name = get_name(grid, x - 1, y, max_x, max_y)
            if name:
                for cx, cy in get_coord(grid, name, max_x, max_y):
                    if not visited[cy, cx]:
                        queue.append((cx, cy))
                        visited[cy, cx] = True
                        dist[cy, cx] = dist[y, x] + 1

        if x + 1 <= max_x and not visited[y, x + 1]:
            c = grid[y][x + 1]

            if c == ".":
                queue.append((x + 1, y))
                visited[y, x + 1] = True
                dist[y, x + 1] = dist[y, x] + 1

            name = get_name(grid, x + 1, y, max_x, max_y)
            if name:
                for cx, cy in get_coord(grid, name, max_x, max_y):
                    if not visited[cy, cx]:
                        queue.append((cx, cy))
                        visited[cy, cx] = True
                        dist[cy, cx] = dist[y, x] + 1


if __name__ == "__main__":
    main()
