import sys

w = 0
b = 0
num = int(sys.stdin.readline().rstrip())
board = []
for i in range(num):
    s = sys.stdin.readline().rstrip()
    board.append([])
    for j in s:
        board[i].append(int(j))

# 하나의 색으로 이루어진 색종이인지 판별, 단일 색으로 이루어졌다면 1을, 섞여있다면 0을 리턴
def check(y, x, n):
    global w, b
    color = board[y][x]
    for i in range(y, y + n):
        for j in range(x, x + n):
            if color != board[i][j]:
                return 0
    if color == 0:
        print('0', end='')
        w += 1
    else:
        print('1', end='')
        b += 1
    return 1


def sol(y, x, n):
    global w, b
    if n == 1:
        return
    print('(', end='')
    if not check(y, x, n // 2):
        sol(y, x, n // 2)
        print(')', end='')
    if not check(y, x + n // 2, n // 2):
        sol(y, x + n // 2, n // 2)
        print(')', end='')
    if not check(y + n // 2, x, n // 2):
        sol(y + n // 2, x, n // 2)
        print(')', end='')
    if not check(y + n // 2, x + n // 2, n // 2):
        sol(y + n // 2, x + n // 2, n // 2)
        print(')', end='')

if not check(0, 0, num):
    sol(0, 0, num)
    print(')')
