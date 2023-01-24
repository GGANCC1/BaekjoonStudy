import sys

n, m = list(map(int, sys.stdin.readline().rstrip().split()))
s = []


def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(1, n + 1):
        s.append(i)
        dfs()
        s.pop()

dfs()