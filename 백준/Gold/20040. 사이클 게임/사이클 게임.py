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


n, m = map(int, sys.stdin.readline().split())
p = []
ans = 1
for i in range(n):
    p.append(i)
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    if findParent(p, x, y):
        break
    unionParent(p, x, y)
    ans += 1
    if i == m - 1:
        ans = 0
print(ans)
