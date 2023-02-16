import sys
sys.setrecursionlimit(10**5)
tc = int(sys.stdin.readline().rstrip())


def dfs(current_x, current_y):
    visited.append([current_x, current_y])
    search = []
    if current_y - 1 >= 0 and field[current_y - 1][current_x] == 1:
        search.append([current_x, current_y - 1])
    if current_y + 1 < n and field[current_y + 1][current_x] == 1:
        search.append([current_x, current_y + 1])
    if current_x + 1 < m and field[current_y][current_x + 1] == 1:
        search.append([current_x + 1, current_y])
    if current_x - 1 >= 0 and field[current_y][current_x - 1] == 1:
        search.append([current_x - 1, current_y])
    for pos in search:
        if pos not in visited:
            dfs(pos[0], pos[1])


for i in range(tc):
    m, n, k = map(int, sys.stdin.readline().rstrip().split())
    field = [[0] * m for _ in range(n)]
    for j in range(k):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        field[y][x] = 1
    visited = []
    cnt = 0
    for j in range(n):
        for l in range(m):
            if field[j][l] == 1 and [l, j] not in visited:
                dfs(l, j)
                cnt += 1
    print(cnt)
