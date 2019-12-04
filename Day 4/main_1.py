def main():
    results = []

    for x in range(197487, 673251 + 1):
        x = str(x)
        never_decreases = True
        has_double_digits = False

        for i in range(len(x) - 1):
            if x[i] > x[i + 1]:
                never_decreases = False
                break

            if x[i] == x[i + 1]:
                has_double_digits = True

        if never_decreases and has_double_digits:
            results.append(x)

    print(len(results))


if __name__ == "__main__":
    main()
