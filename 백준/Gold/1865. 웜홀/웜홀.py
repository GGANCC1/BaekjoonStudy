import sys


def bellmanFord(start):
    dist = [INF] * (n + 2)
    dist[start] = 0
    for i in range(n + 1):
        for j in range(1, n + 2):
            for k in graph[j].keys():
                cur = j
                next_node = k
                cost = graph[j][k]
                if dist[cur] != INF and dist[next_node] > dist[cur] + cost:
                    dist[next_node] = dist[cur] + cost
                    if i == n:
                        return True
    return False


tc = int(sys.stdin.readline().rstrip())
INF = sys.maxsize
for i in range(tc):
    n, m, w = map(int, sys.stdin.readline().split())
    graph = {node: {} for node in range(1, n + 2)}
    for j in range(m):
        s, e, t = map(int, sys.stdin.readline().split())
        if e in graph[s].keys():
            graph[s][e] = min(graph[s][e], t)
            graph[e][s] = min(graph[e][s], t)
        else:
            graph[s][e] = t
            graph[e][s] = t

    for j in range(w):
        s, e, t = map(int, sys.stdin.readline().split())
        if e in graph[s].keys():
            graph[s][e] = min(graph[s][e], -t)
        else:
            graph[s][e] = -t
    # 모든 정점과 연결될 하나의 노드를 생성
    start_node = n + 1
    for i in range(1, n + 1):
        graph[start_node][i] = 0
    # 해당 노드를 출발점으로 bellman-Ford 알고리즘을 실행
    if bellmanFord(start_node):
        print("YES")
    else:
        print("NO")
