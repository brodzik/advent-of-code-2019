import copy
import math


def get_distance(p, q):
    return math.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)


def get_phase(p, q):
    t = math.atan2(p[0] - q[0], p[1] - q[1]) - math.pi / 2
    return t if t >= 0 else t + 2 * math.pi


def is_collinear(p, q, r):
    return p[0] * (q[1] - r[1]) + q[0] * (r[1] - p[1]) + r[0] * (p[1] - q[1]) == 0


def get_visible(asteroids, p):
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

    return visible


def main():
    asteroids = []
    X = (29, 23)

    with open("input.txt") as input_file:
        data = input_file.readlines()
        for x in range(len(data)):
            for y in range(len(data[x])):
                if data[x][y] == "#" and (x, y) != X:
                    asteroids.append((x, y))

    counter = 1

    while asteroids:
        visible = sorted(get_visible(asteroids, X), key=lambda p: get_phase(X, p))
        while visible:
            p = visible.pop(0)

            if counter == 200:
                print(counter, p, p[0] + 100 * p[1])
                return

            asteroids.remove(p)
            counter += 1


if __name__ == "__main__":
    main()
