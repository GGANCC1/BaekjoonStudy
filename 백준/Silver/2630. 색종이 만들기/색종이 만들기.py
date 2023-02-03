import sys

w = 0
b = 0
num = int(sys.stdin.readline().rstrip())
paper = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(num)]


# 하나의 색으로 이루어진 색종이인지 판별, 단일 색으로 이루어졌다면 1을, 섞여있다면 0을 리턴
def check(y, x, n):
    global w, b
    color = paper[y][x]
    for i in range(y, y + n):
        for j in range(x, x + n):
            if color != paper[i][j]:
                return 0
    if color == 0:
        w += 1
    else:
        b += 1
    return 1


def sol(y, x, n):
    global w, b
    if n == 1:
        if paper[y][x] == 1:
            b += 1
        else:
            w += 1
        return
    if not check(y, x, n // 2):
        sol(y, x, n // 2)
    if not check(y, x + n // 2, n // 2):
        sol(y, x + n // 2, n // 2)
    if not check(y + n // 2, x, n // 2):
        sol(y + n // 2, x, n // 2)
    if not check(y + n // 2, x + n // 2, n // 2):
        sol(y + n // 2, x + n // 2, n // 2)


if not check(0, 0, num):
    sol(0, 0, num)
print(w)
print(b)
