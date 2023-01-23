import sys

n = int(sys.stdin.readline().rstrip())
dp = []
for i in range(1001):
    dp.append([])
    for j in range(1001):
        dp[i].append([])
dp[0][0]=1
dp[1][0]=1
dp[1][1]=1
for i in range(2, 31, 1):
    for j in range(i + 1):
        if j == 0:
            dp[i][0] = 1
        elif j == i:
            dp[i][j] = 1
        else:
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j])
for i in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(dp[b][a])
