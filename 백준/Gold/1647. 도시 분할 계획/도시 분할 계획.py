import sys


def getParent(parent, x):
    if parent[x] == x:
        return x
    else:
        parent[x] = getParent(parent, parent[x])
        return parent[x]


def unionParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def findParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if a == b:
        return 1
    return 0


V, E = map(int, sys.stdin.readline().split())
edges = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(E)], key=lambda x: x[2])
p = [0]
ans = 0
for i in range(1, V + 1):
    p.append(i)
cnt = V
for edge in edges:
    if cnt == 2:
        break
    if findParent(p, edge[0], edge[1]):
        continue
    ans += edge[2]
    unionParent(p, edge[0], edge[1])
    cnt -= 1
print(ans)
