import sys

N, r, c = map(int, sys.stdin.readline().rstrip().split())
N = pow(2, N)
cnt = 0

def sol(row, col, n):
    global r, c, cnt
    if row == r and col == c:
        print(cnt)
        exit(0)
    if n == 1:
        cnt += 1
        return
    if row <= r < row + n // 2 and col <= c < col + n // 2:
        sol(row, col, n // 2)
    else:
        cnt += (n // 2) * (n // 2)
    if row <= r < row + n // 2 and col + n // 2 <= c < col + n:
        sol(row, col + n // 2, n // 2)
    else:
        cnt += (n // 2) * (n // 2)
    if row + n // 2 <= r < row + n and col <= c < col + n // 2:
        sol(row + n // 2, col, n // 2)
    else:
        cnt += (n // 2) * (n // 2)
    if row + n // 2 <= r < row + n and col + n // 2 <= c < col + n:
        sol(row + n // 2, col + n // 2, n // 2)
    else:
        cnt += (n // 2) * (n // 2)


sol(0, 0, N)

