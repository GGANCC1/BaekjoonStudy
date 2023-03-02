import sys
from collections import deque


def bfs(x, y, num):
    global N, M, arr, group_arr, dx, dy, dt
    q = deque()
    q.append((x, y))
    dt[num] = 1
    group_arr[y][x] = num
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx] and arr[ny][nx] != 1:
                visited[ny][nx] = True
                group_arr[ny][nx] = num
                dt[num] += 1
                q.append((nx, ny))
    return


N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
group_arr = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        group_arr[i][j] = arr[i][j]
visited = [[False] * M for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
dt = {}
group = -1
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            bfs(j, i, group)
            group -= 1
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            temp = []
            for k in range(4):
                nx = j + dx[k]
                ny = i + dy[k]
                if 0 <= nx < M and 0 <= ny < N and arr[ny][nx] == 0 and group_arr[ny][nx] not in temp:
                    arr[i][j] += dt[group_arr[ny][nx]]
                    temp.append(group_arr[ny][nx])
for line in arr:
    for x in line:
        print(x % 10, end='')
    print()
