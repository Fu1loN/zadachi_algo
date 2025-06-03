from heapq import heappop, heappush
def deikstra(graph: list[list[tuple[int, float]]], start: int):
    priority_queue = []
    dist = [-1] * len(graph)
    heappush(priority_queue, (0, start))
    while priority_queue:
        distance_t, u = heappop(priority_queue)
        if dist[u] < 0:
            dist[u] = distance_t
            for v, w in graph[u]:
                if dist[v] < 0:
                    heappush(priority_queue, (distance_t + w, v))
    return dist

def main():
    graph = None
    with open("graph.txt", "r") as f:
        n = int(f.readline())
        graph = [[] for _ in range(n + 1)]
        line = f.readline()
        while line:
            splitted_line = line.strip().split(" ")
            u,v, w = int(splitted_line[0]), int(splitted_line[1]), float(splitted_line[2])
            graph[u].append((v, w))
            graph[v].append((u, w))
            line = f.readline()
    for vertex in graph:
        print(vertex)
    assert graph is not None
    print(deikstra(graph, 1))

if __name__ == "__main__":
    main()
