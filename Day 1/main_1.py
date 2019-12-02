def main():
    with open("input.txt") as input_file:
        result = sum([int(x) // 3 - 2 for x in input_file])
        print(result)


if __name__ == "__main__":
    main()
