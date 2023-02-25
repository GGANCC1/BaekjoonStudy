import sys
sys.setrecursionlimit(10 ** 5)


def dfs(node, length):
    global ans
    if len(graph[node]) == 1 and length != 0:
        ans = max(ans, length)
        return
    for next_node in graph[node]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node, length + graph[node][next_node])
            visited[next_node] = False


n = int(sys.stdin.readline().rstrip())
graph = {node: {} for node in range(n)}
for i in range(n - 1):
    a, b, c = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    graph[a][b] = c
    graph[b][a] = c
start = []
for i in range(n):
    if len(graph[i]) == 1:
        start.append(i)
ans = 0
for i in start:
    visited = [False] * n
    visited[i] = True
    dfs(i, 0)
print(ans)
