import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
weight = [0]
value = [0]
dp = [[0]*(k+1) for _ in range(n+1)]
for i in range(n):
    w, v = map(int, sys.stdin.readline().rstrip().split())
    weight.append(w)
    value.append(v)

for i in range(1, n+1):
    for j in range(1, k+1):
        w = weight[i]
        v = value[i]
        if j < w:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

print(max(dp[n]))
