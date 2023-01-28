import copy
import sys

N = int(sys.stdin.readline().rstrip())
dp = [0]

for i in range(1, N + 1):
    dp.append(int(sys.stdin.readline().rstrip()))
arr = copy.deepcopy(dp)

if N > 1:
    dp[2] += dp[1]
for i in range(3, N + 1):
    dp[i] = max(dp[i - 3] + arr[i - 1] + arr[i], dp[i - 2] + arr[i])

print(dp[N])
