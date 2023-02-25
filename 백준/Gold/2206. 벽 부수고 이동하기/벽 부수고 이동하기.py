import sys
from collections import deque


def bfs():
    visited = [[[False, False] for _ in range(m)] for _ in range(n)]
    visited[0][0] = [True, True]
    dist = [[0] * m for _ in range(n)]
    dist[0][0] = 1
    q = deque()
    q.append((0, 0, 1, True))
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    while q:
        x, y, d, w = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx == m - 1 and ny == n - 1:
                return d + 1
            if 0 <= nx < m and 0 <= ny < n:
                if not visited[ny][nx][0]:
                    if board[ny][nx] == '1':
                        if w:
                            dist[ny][nx] = d + 1
                            visited[ny][nx] = [True, False]
                            q.append((nx, ny, d + 1, False))
                        else:
                            pass
                    else:
                        dist[ny][nx] = d + 1
                        visited[ny][nx] = [True, w]
                        q.append((nx, ny, d + 1, w))
                elif w and not visited[ny][nx][1] and board[ny][nx] != '1':
                    dist[ny][nx] = d + 1
                    visited[ny][nx] = [True, True]
                    q.append((nx, ny, d + 1, w))
    return -1


n, m = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
if n == 1 and m == 1:
    print(1)
else:
    print(bfs())
