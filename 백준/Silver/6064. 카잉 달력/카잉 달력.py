import sys


def sol(m, n, x, y):
    while x <= m * n:
        if (x - y) % n == 0:
            return x
        x += m
    return -1


tc = int(sys.stdin.readline().rstrip())
for i in range(tc):
    m, n, x, y = map(int, input().split())
    print(sol(m, n, x, y))