import sys
import heapq


def dijkstra(start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    q = []
    heapq.heappush(q, [dist[start], start])
    while q:
        cur_dist, cur_node = heapq.heappop(q)
        if dist[cur_node] < cur_dist:
            continue
        for next_node, next_dist in graph[cur_node].items():
            if dist[next_node] > cur_dist + next_dist:
                dist[next_node] = cur_dist + next_dist
                heapq.heappush(q, [dist[next_node], next_node])
    return dist


N, M, X = map(int, sys.stdin.readline().split())
graph = {node: {} for node in range(1, N + 1)}
for i in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = c
result = [0]
for i in range(1, N + 1):
    result.append(dijkstra(i))
max_value = 0
for i in range(1, N + 1):
    if i == X:
        continue
    distance = result[i][X] + result[X][i]
    if distance > max_value:
        max_value = distance
print(max_value)