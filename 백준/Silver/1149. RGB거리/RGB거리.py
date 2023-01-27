import sys

N = int(sys.stdin.readline().rstrip())
dp = []
for i in range(N):
    dp.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(1, N):
    dp[i][0] += min(dp[i - 1][1], dp[i - 1][2]) # 빨간집 출발
    dp[i][1] += min(dp[i - 1][0], dp[i - 1][2]) # 초록집 출발
    dp[i][2] += min(dp[i - 1][0], dp[i - 1][1]) # 파란집 출발

print(min(dp[N-1]))