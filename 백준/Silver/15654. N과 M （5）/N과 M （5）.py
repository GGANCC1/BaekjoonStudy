import sys

# sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
result = []
idx = []


def sol(n, m):
    if m == M:
        print(" ".join(map(str, result)))
        return
    for i in range(len(arr)):
        result.append(arr[i])
        if i not in idx:
            idx.append(i)
            sol(i, m + 1)
            idx.pop()
        result.pop()

sol(-1, 0)
