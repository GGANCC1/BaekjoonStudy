import sys
# import heapq

from collections import deque

# sys.setrecursionlimit(10 ** 5)

n, m, v = map(int, sys.stdin.readline().rstrip().split())
graph = {}
for i in range(m):
    node1, node2 = map(int, sys.stdin.readline().rstrip().split())
    if node1 in graph.keys():
        graph[node1].append(node2)
    else:
        graph[node1] = [node2]
    if node2 in graph.keys():
        graph[node2].append(node1)
    else:
        graph[node2] = [node1]
for key in graph.keys():
    graph[key].sort()
visited = [False] * (n + 1)


def dfs(num):
    if visited[num]:
        return
    visited[num] = True
    print(num, end=' ')
    if num in graph.keys():
        for node in graph[num]:
            dfs(node)
    return


def bfs(num):
    visited = [False] * (n + 1)
    visited[num] = True
    q = deque()
    q.append(num)
    while q:
        current_pos = q.popleft()
        print(current_pos, end=' ')
        if current_pos in graph.keys():
            for node in graph[current_pos]:
                if not visited[node]:
                    q.append(node)
                    visited[node] = True


dfs(v)
print('')
bfs(v)
