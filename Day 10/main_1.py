import copy
import math


def get_distance(p, q):
    return math.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)


def is_collinear(p, q, r):
    return p[0] * (q[1] - r[1]) + q[0] * (r[1] - p[1]) + r[0] * (p[1] - q[1]) == 0


def main():
    asteroids = []

    with open("input.txt") as input_file:
        data = input_file.readlines()
        for x in range(len(data)):
            for y in range(len(data[x])):
                if data[x][y] == "#":
                    asteroids.append((x, y))

    result = 0
    result_p = (0, 0)

    for p in asteroids:
        queue = sorted(asteroids, key=lambda q: get_distance(p, q))[1:]
        visible = []

        while queue:
            q = queue.pop(0)
            ok = True

            for r in visible:
                if is_collinear(p, q, r) and get_distance(q, r) != max(get_distance(p, q), get_distance(q, r), get_distance(p, r)):
                    ok = False
                    break

            if ok:
                visible.append(q)

        if len(visible) > result:
            result = len(visible)
            result_p = p

    print(result, result_p)


if __name__ == "__main__":
    main()
