import sys

n, m, k = map(int, sys.stdin.readline().rstrip().split())
dpB = [[0] * (m + 1) for _ in range(n + 1)]
dpW = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    line = sys.stdin.readline().rstrip()
    for j in range(1, m + 1):
        if (i + j) % 2 == 0:
            if line[j - 1] == 'W':
                dpB[i][j] = dpB[i][j - 1] + dpB[i - 1][j] - dpB[i - 1][j - 1] + 1
                dpW[i][j] = dpW[i][j - 1] + dpW[i - 1][j] - dpW[i - 1][j - 1]
            else:
                dpB[i][j] = dpB[i][j - 1] + dpB[i - 1][j] - dpB[i - 1][j - 1]
                dpW[i][j] = dpW[i][j - 1] + dpW[i - 1][j] - dpW[i - 1][j - 1] + 1
        else:
            if line[j - 1] == 'B':
                dpB[i][j] = dpB[i][j - 1] + dpB[i - 1][j] - dpB[i - 1][j - 1] + 1
                dpW[i][j] = dpW[i][j - 1] + dpW[i - 1][j] - dpW[i - 1][j - 1]
            else:
                dpB[i][j] = dpB[i][j - 1] + dpB[i - 1][j] - dpB[i - 1][j - 1]
                dpW[i][j] = dpW[i][j - 1] + dpW[i - 1][j] - dpW[i - 1][j - 1] + 1
result = sys.maxsize
for i in range(k, n + 1):
    for j in range(k, m + 1):
        wrong = min(dpB[i][j] - dpB[i - k][j] - dpB[i][j - k] + dpB[i - k][j - k],
                    dpW[i][j] - dpW[i - k][j] - dpW[i][j - k] + dpW[i - k][j - k])
        if result > wrong:
            result = wrong
print(result)