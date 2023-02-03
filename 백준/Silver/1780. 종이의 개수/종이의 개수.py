import sys

ans = [0, 0, 0]
num = int(sys.stdin.readline().rstrip())
board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(num)]


# 하나의 색으로 이루어진 색종이인지 판별, 단일 색으로 이루어졌다면 1을, 섞여있다면 0을 리턴
def check(y, x, n):
    color = board[y][x]
    for i in range(y, y + n):
        for j in range(x, x + n):
            if color != board[i][j]:
                return 0
    ans[color] += 1
    return 1


def sol(y, x, n):
    if n == 1:
        ans[board[y][x]] += 1
        return
    for i in range(3):
        for j in range(3):
            if not check(y + i * (n // 3), x + j * (n // 3), n // 3):
                sol(y + i * (n // 3), x + j * (n // 3), n // 3)


if not check(0, 0, num):
    sol(0, 0, num)
print(ans[-1])
print(ans[0])
print(ans[1])