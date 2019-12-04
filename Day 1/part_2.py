def main():
    result = 0
    with open("input.txt") as input_file:
        for x in input_file:
            x = int(x)
            while True:
                x = x // 3 - 2
                if x < 0:
                    break
                result += x
    print(result)


if __name__ == "__main__":
    main()
