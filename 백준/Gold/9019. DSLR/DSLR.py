import sys
from collections import deque

INF = sys.maxsize


def dslr(c, num):
    if c == 'D':
        return (num * 2) % 10000
    elif c == 'S':
        if num == 0:
            return 9999
        else:
            return num - 1
    elif c == 'L':
        d4 = (num % 10) // 1
        d3 = (num % 100) // 10
        d2 = (num % 1000) // 100
        d1 = num // 1000
        return d1 + d4 * 10 + d3 * 100 + d2 * 1000
    elif c == 'R':
        d4 = (num % 10) // 1
        d3 = (num % 100) // 10
        d2 = (num % 1000) // 100
        d1 = num // 1000
        return d3 + d2 * 10 + d1 * 100 + d4 * 1000
    else:
        return


def bfs(s, t):
    q = deque()
    q.append((s, ""))
    visited = [INF] * 10001
    visited[s] = 0
    dx = ['D', 'S', 'L', 'R']
    ans = "X" * 10001
    while q:
        x, cmd = q.popleft()
        if x == t and len(ans) > len(cmd):
            ans = cmd
        for i in range(len(dx)):
            nx = dslr(dx[i], x)
            if visited[nx] > len(cmd) + 1:
                visited[nx] = len(cmd) + 1
                q.append((nx, cmd + dx[i]))
    return ans


n = int(sys.stdin.readline().rstrip())
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    result = bfs(a, b)
    print("".join(map(str, result)))