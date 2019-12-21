from tqdm import tqdm


def main():
    data = open("input.txt").readline().strip()
    data_new = ""
    pattern = [0, 1, 0, -1]

    for phase in tqdm(range(100)):
        for i in range(len(data)):
            k = 0
            l = 1
            m = 0

            for j in range(len(data)):
                if l >= i + 1:
                    k = (k + 1) % len(pattern)
                    l = 0

                m += int(data[j]) * pattern[k]

                l += 1

            data_new += str(abs(m) % 10)

        data = data_new
        data_new = ""

    print(data[:8])


if __name__ == "__main__":
    main()
