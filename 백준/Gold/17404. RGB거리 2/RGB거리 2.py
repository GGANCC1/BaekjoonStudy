import sys

N = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
INF = sys.maxsize
ans = INF
for i in range(3):
    dp = [[INF, INF, INF] for _ in range(N)]
    dp[0][i] = arr[0][i]
    for j in range(1, N):
        dp[j][0] = arr[j][0] + min(dp[j - 1][1], dp[j - 1][2])
        dp[j][1] = arr[j][1] + min(dp[j - 1][0], dp[j - 1][2])
        dp[j][2] = arr[j][2] + min(dp[j - 1][0], dp[j - 1][1])
    for j in range(3):
        if i != j:
            ans = min(ans, dp[-1][j])
print(ans)