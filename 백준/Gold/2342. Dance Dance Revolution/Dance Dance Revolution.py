import sys


def cost(t, f):
    if f == 0:
        if t == 0:
            return 0
        else:
            return 2
    elif f == t:
        return 1
    elif abs(f - t) == 1 or abs(f - t) == 3:
        return 3
    else:
        return 4


move = list(map(int, sys.stdin.readline().split()))
n = len(move) - 1
if n == 0:
    print(0)
    exit(0)
dp = [[[400001 for _ in range(5)] for _ in range(5)] for _ in range(n + 1)]
dp[-1][0][0] = 0
for i in range(n):
    for j in range(5):
        for k in range(5):
            c = cost(move[i], k)
            dp[i][move[i]][j] = min(dp[i][move[i]][j], dp[i - 1][k][j] + c)
            dp[i][j][move[i]] = min(dp[i][j][move[i]], dp[i - 1][j][k] + c)
min_value = 400001
for l in range(5):
    for r in range(5):
        min_value = min(min_value, dp[n - 1][l][r])
print(min_value)