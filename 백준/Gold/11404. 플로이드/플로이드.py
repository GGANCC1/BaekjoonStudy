import sys


def sol():
    global n
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for i in range(n):
        for j in graph[i].keys():
            dist[i][j] = graph[i][j]
    # dist[i][j]는 i에서 j까지 가는 최단비용을 뜻함.
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
graph = {node: {} for node in range(n)}
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    if b in graph[a].keys():
        graph[a][b] = min(graph[a][b], c)
    else:
        graph[a][b] = c
result = sol()
for j in result:
    for k in j:
        if k == float('inf'):
            print(0, end=' ')
        else:
            print(k, end=' ')
    print()

