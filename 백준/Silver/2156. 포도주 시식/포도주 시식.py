import sys

N = int(sys.stdin.readline().rstrip())
data = [0]
for i in range(N):
    data.append(int(sys.stdin.readline().strip()))
dp = [0] * 10001
dp[1] = data[1]
if N > 1:
    dp[2] = data[1] + data[2]

for i in range(3, N + 1):
    dp[i] = max(dp[i-3] + data[i-1] + data[i], dp[i-2] + data[i], dp[i-1])

print(max(dp))
