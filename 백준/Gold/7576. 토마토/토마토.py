import sys
from collections import deque


M, N = map(int, sys.stdin.readline().rstrip().split())
field = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
tomato = 0
for i in field:
    tomato += i.count(0)


def bfs():
    global tomato
    q = deque()
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                q.append((j, i))
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and field[ny][nx] == 0:
                tomato -= 1
                field[ny][nx] = field[y][x] + 1
                q.append((nx, ny))


bfs()
if tomato > 0:
    print(-1)
else:
    print(max(map(max, field)) - 1)
