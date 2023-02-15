import sys

tc = int(sys.stdin.readline().rstrip())
dp = [0] * 12
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(tc):
    n = int(sys.stdin.readline().rstrip())
    for j in range(4, n + 1):
        dp[j] = dp[j-1] + dp[j-2] + dp[j-3]
    print(dp[n])
