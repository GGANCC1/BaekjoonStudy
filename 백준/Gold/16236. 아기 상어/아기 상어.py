import sys
from collections import deque


def bfs(pos_x, pos_y, current_t):
    global n, pos, size
    q = deque()
    q.append((pos_x, pos_y, current_t, 0))
    visited = [[False] * n for _ in range(n)]
    dx = [0, -1, 1, 0]
    dy = [-1, 0, 0, 1]
    goal = (n, n, sys.maxsize)
    while q:
        x, y, t, d = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx]:
                if fishes[ny][nx] == 0 or fishes[ny][nx] == size:
                    visited[ny][nx] = True
                    q.append((nx, ny, t + 1, d + 1))
                elif fishes[ny][nx] < size:
                    if goal[2] == d + 1:
                        if ny < goal[1]:
                            goal = (nx, ny, d + 1)
                        elif ny == goal[1] and nx < goal[0]:
                            goal = (nx, ny, d + 1)
                        else:
                            pass
                    elif goal[2] > d + 1:
                        goal = (nx, ny, d + 1)
                    else:
                        pass
                else:
                    continue
    if goal[2] == sys.maxsize:
        return 0
    pos = [goal[0], goal[1]]
    fishes[goal[1]][goal[0]] = 0
    return current_t + goal[2]


n = int(sys.stdin.readline().rstrip())
fishes = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
pos = [0, 0]
size = 2
eat = 0
ans = 0
for i in range(n):
    for j in range(n):
        if fishes[i][j] == 9:
            fishes[i][j] = 0
            pos = [j, i]
            break
while True:
    tmp = bfs(pos[0], pos[1], ans)
    if tmp == 0:
        print(ans)
        break
    eat += 1
    if eat == size:
        eat = 0
        size += 1
    ans = tmp
