import sys

n, pair = map(int, sys.stdin.readline().rstrip().split())
graph = {}
for i in range(pair):
    node1, node2 = map(int, sys.stdin.readline().rstrip().split())
    if node1 in graph.keys():
        graph[node1].append(node2)
    else:
        graph[node1] = [node2]
    if node2 in graph.keys():
        graph[node2].append(node1)
    else:
        graph[node2] = [node1]
visited = []


def dfs(num):
    if num not in graph.keys():
        return
    visited.append(num)
    for node in graph[num]:
        if node not in visited:
            dfs(node)


cnt = 0
for node in range(1, n + 1):
    if node not in visited:
        dfs(node)
        cnt += 1
print(cnt)

