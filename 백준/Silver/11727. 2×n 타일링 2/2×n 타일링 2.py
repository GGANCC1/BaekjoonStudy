import sys

n = int(sys.stdin.readline().rstrip())
mod = 10007
dp = [0] * 1001
dp[1] = 1
dp[2] = 3
for i in range(3, n + 1):
    dp[i] = (dp[i-1] + 2 * dp[i-2]) % mod
print(dp[n] % mod)