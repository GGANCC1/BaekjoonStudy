import sys
from collections import deque


def bfs(pos, mode):
    q = deque()
    q. append(pos)
    color = []
    if mode == 1 and (arr[pos[1]][pos[0]] == 'R' or arr[pos[1]][pos[0]] == 'G'):
        color = ['R', 'G']
    else:
        color = [arr[pos[1]][pos[0]]]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and arr[ny][nx] in color and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((nx, ny))


N = int(sys.stdin.readline().rstrip())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
for m in range(2):
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                bfs((j, i), m)
                cnt += 1
    print(cnt, end=' ')
