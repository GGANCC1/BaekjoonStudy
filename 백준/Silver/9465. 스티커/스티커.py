import sys

tc = int(sys.stdin.readline().rstrip())
for i in range(tc):
    n = int(sys.stdin.readline().rstrip())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    if n > 1:
        dp[0][1] = arr[1][0] + arr[0][1]
        dp[1][1] = arr[1][1] + arr[0][0]
        for j in range(2, n):
            dp[0][j] = max(max(dp[0][j - 2], dp[1][j - 2]), dp[1][j - 1]) + arr[0][j]
            dp[1][j] = max(max(dp[0][j - 2], dp[1][j - 2]), dp[0][j - 1]) + arr[1][j]
    print(max(dp[0][n - 1], dp[1][n - 1]))