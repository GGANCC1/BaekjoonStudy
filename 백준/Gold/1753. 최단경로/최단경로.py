import sys
from collections import deque
import heapq


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])
    while queue:
        current_distance, current_destination = heapq.heappop(queue)
        if distances[current_destination] < current_distance:
            continue
        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])
    return distances


V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline().rstrip())
g = {}
for i in range(1, V + 1):
    g[i] = {}
for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    if v not in g[u].keys():
        g[u][v] = w
    else:
        g[u][v] = min(g[u][v], w)

result = dijkstra(g, K)
for key in result.keys():
    if result[key] == float('inf'):
        print("INF")
    else:
        print(result[key])
