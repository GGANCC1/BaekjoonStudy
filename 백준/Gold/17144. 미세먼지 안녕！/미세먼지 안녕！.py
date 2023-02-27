import sys
from collections import deque
# import heapq


def move(row, direction):
    if direction == 0:
        for i in range(row - 1, -1, -1):
            arr[i][0] = arr[i - 1][0]
        del arr[0][0]
        arr[0].append(0)
        for i in range(row):
            arr[i][-1] = arr[i + 1][-1]
        del arr[row][-1]
        arr[row].insert(1, 0)
    else:
        for i in range(row + 1, R - 1):
            arr[i][0] = arr[i + 1][0]
        del arr[-1][0]
        arr[-1].append(0)
        for i in range(R - 1, row, -1):
            arr[i][-1] = arr[i - 1][-1]
        del arr[row][-1]
        arr[row].insert(1, 0)


def spread():
    q = deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(R):
        for j in range(C):
            if arr[i][j] != 0 and arr[i][j] != -1:
                q.append((j, i, arr[i][j]))
    while q:
        x, y, n = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < C and 0 <= ny < R and not (nx == 0 and (ny == cleaner[0] or ny == cleaner[1])):
                arr[y][x] -= (n // 5)
                arr[ny][nx] += (n // 5)


R, C, T = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
cleaner = []
for i in range(R):
    for j in range(C):
        if arr[i][j] == -1:
            cleaner.append(i)
for i in range(T):
    spread()
    move(cleaner[0], 0)
    move(cleaner[1], 1)
result = 2
for i in range(R):
    result += sum(arr[i])
print(result)