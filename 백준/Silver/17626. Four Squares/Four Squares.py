import sys

n = int(sys.stdin.readline().rstrip())
dp = [0] * 50001
dp[0] = 0
dp[1] = 1

for i in range(2, n + 1):
    minimum = sys.maxsize
    j = 1
    while i >= j**2:
        minimum = min(minimum, dp[i - j**2])
        j += 1
    dp[i] = minimum + 1
print(dp[n])