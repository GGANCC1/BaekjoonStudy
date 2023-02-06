import sys

tc = int(sys.stdin.readline().rstrip())
dp = [[1, 0], [0, 1], [1, 1], [1, 2]]
for i in range(37):
    dp.append([-1, -1])


def sol(n):
    if n == 0 or n == 1 or n == 2 or n == 3:
        return dp[n]
    if dp[n][0] != -1:
        return dp[n]
    x = sol(n - 1)
    y = sol(n - 2)
    dp[n][0] = x[0] + y[0]
    dp[n][1] = x[1] + y[1]
    return dp[n]


for i in range(tc):
    num = int(sys.stdin.readline().rstrip())
    ans = sol(num)
    print(ans[0], ans[1])