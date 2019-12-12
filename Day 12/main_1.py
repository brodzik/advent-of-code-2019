import itertools


class Moon:
    def __init__(self):
        self.position = [0, 0, 0]
        self.velocity = [0, 0, 0]

    def get_energy(self):
        return sum([abs(p) for p in self.position]) * sum([abs(v) for v in self.velocity])


def main():
    moons = []

    with open("input.txt") as input_file:
        for line in input_file:
            moon = Moon()
            for i, coord in enumerate(line[1:-2].split(",")):
                moon.position[i] = int(coord.split("=")[1])
            moons.append(moon)

    for t in range(1000):
        for m1, m2 in itertools.combinations(moons, 2):
            for i in range(3):
                if m1.position[i] > m2.position[i]:
                    m1.velocity[i] -= 1
                    m2.velocity[i] += 1
                elif m1.position[i] < m2.position[i]:
                    m1.velocity[i] += 1
                    m2.velocity[i] -= 1

        for m in moons:
            for i in range(3):
                m.position[i] += m.velocity[i]

    for m in moons:
        print(m.position, m.velocity)

    print(sum([m.get_energy() for m in moons]))


if __name__ == "__main__":
    main()
