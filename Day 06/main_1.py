def dfs(graph, visited, node, count):
    if node not in visited:
        visited.append(node)
        for neighbour in graph[node]:
            dfs(graph, visited, neighbour, count)
            count[0] += 1


def main():
    graph = {}

    with open("input.txt") as input_file:
        for line in input_file:
            a, b = line[:-1].split(")")

            if a in graph:
                graph[a].append(b)
            else:
                graph[a] = [b]

            if b not in graph:
                graph[b] = []

    result = 0

    for node in graph:
        visited = []
        count = [0]
        dfs(graph, visited, node, count)
        result += count[0]

    print(result)


if __name__ == "__main__":
    main()
