import sys

board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(9)]
blank = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blank.append([j, i])


def promising(x, y):
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # row 확인
    for i in range(9):
        if board[y][i] in arr:
            arr.remove(board[y][i])
    # column 확인
    for i in range(9):
        if board[i][x] in arr:
            arr.remove(board[i][x])
    # 3 x 3 Square 확인
    x = (x // 3) * 3
    y = (y // 3) * 3
    for i in range(y, y + 3, 1):
        for j in range(x, x + 3, 1):
            if board[i][j] in arr:
                arr.remove(board[i][j])
    return arr


def dfs(num):
    if len(blank) == num:
        for i in board:
            print(" ".join(map(str, i)))
        exit(0)
    x, y = blank[num][0], blank[num][1]
    for i in promising(x, y):
        board[y][x] = i
        dfs(num + 1)
        board[y][x] = 0

dfs(0)
