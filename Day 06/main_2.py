def bfs(graph, source, target):
    visited = {k: False for k in graph}
    distance = {k: 1000000 for k in graph}
    queue = []

    visited[source] = True
    distance[source] = 0
    queue.append(source)

    while queue:
        node = queue.pop(0)

        for n in graph[node]:
            if not visited[n]:
                visited[n] = True
                distance[n] = distance[node] + 1
                queue.append(n)

                if n == target:
                    return distance[n]


def main():
    graph = {}

    with open("input.txt") as input_file:
        for line in input_file:
            a, b = line[:-1].split(")")

            if a in graph:
                graph[a].append(b)
            else:
                graph[a] = [b]

            if b in graph:
                graph[b].append(a)
            else:
                graph[b] = [a]

    print(bfs(graph, "YOU", "SAN") - 2)


if __name__ == "__main__":
    main()
