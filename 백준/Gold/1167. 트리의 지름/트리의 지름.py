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
    arr = list(map(int, sys.stdin.readline().split()))
    a = arr[0]
    a -= 1
    idx = 1
    while arr[idx] != -1:
        b = arr[idx] - 1
        c = arr[idx + 1]
        graph[a][b] = c
        graph[b][a] = c
        idx += 2
ans = 0
start_node = 0
for i in range(2):
    visited = [False] * n
    visited[start_node] = True
    dfs(start_node, 0)
print(ans)
