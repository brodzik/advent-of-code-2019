def main():
    points = []

    with open("input.txt") as input_file:
        for wire in input_file:
            wire = [(x[0], int(x[1:])) for x in wire.split(",")]

            x, y = 0, 0
            points_local = [(x, y)]

            for direction, value in wire:
                if direction == "U":
                    y += value
                elif direction == "D":
                    y -= value
                elif direction == "R":
                    x += value
                elif direction == "L":
                    x -= value
                else:
                    raise Exception("Invalid direction: " + direction)

                points_local.append((x, y))

            points.append(points_local)

    results = []

    for i in range(len(points[0]) - 1):
        px1, py1 = points[0][i][0], points[0][i][1]
        px2, py2 = points[0][i + 1][0], points[0][i + 1][1]
        for j in range(len(points[1]) - 1):
            qx1, qy1 = points[1][j][0], points[1][j][1]
            qx2, qy2 = points[1][j + 1][0], points[1][j + 1][1]

            if px1 == px2 and qy1 == qy2:
                if px1 <= max(qx1, qx2) and px1 >= min(qx1, qx2) and px2 <= max(qx1, qx2) and px2 >= min(qx1, qx2):
                    if max(py1, py2) >= qy1 and min(py1, py2) <= qy2:
                        results.append(abs(px1) + abs(qy1))
            elif py1 == py2 and qx1 == qx2:
                if qx1 <= max(px1, px2) and qx1 >= min(px1, px2) and qx2 <= max(px1, px2) and qx2 >= min(px1, px2):
                    if max(qy1, qy2) >= py1 and min(qy1, qy2) <= py2:
                        results.append(abs(qx1) + abs(py1))

    print(min(results))


if __name__ == "__main__":
    main()
