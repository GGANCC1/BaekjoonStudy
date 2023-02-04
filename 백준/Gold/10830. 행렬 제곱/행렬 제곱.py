import sys

n, b = map(int, sys.stdin.readline().rstrip().split())
matrix = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
mod = 1000

def multiple_matrix(m1, m2):
    global n
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += (m1[i][k] * m2[k][j]) % mod
            result[i][j] %= mod
    return result


def sol(m, n):
    if n == 1:
        return m
    mat = sol(m, n // 2)
    if n % 2 == 0:
        return multiple_matrix(mat, mat)
    else:
        return multiple_matrix(multiple_matrix(mat, mat), m)


ans = sol(matrix, b)
for i in ans:
    for j in i:
        print(j % mod, end=' ')
    print('')
