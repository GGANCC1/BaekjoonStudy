import sys
sys.setrecursionlimit(10 ** 5)


def dfs(node, length):
    global ans, start_node
    if len(graph[node]) == 1 and length != 0:
        if ans < length:
            ans = length
            start_node = node
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
ans = 0
start_node = 0
for i in range(2):
    visited = [False] * n
    visited[start_node] = True
    dfs(start_node, 0)
print(ans)
