import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
# 벽면에서의 이동 방향 결정을 위해 10001로 감싸줌
data = [[10001] * (m + 1)] + [[10001] + list(map(int, sys.stdin.readline().rstrip().split())) + [10001] for _ in range(n)]  + [[10001] * (m + 1)]
dp = [[0] * (m + 1)] + [[0] + [-1] * m + [0] for _ in range(n)] + [[0] * (m + 1)]


def dfs(low, col):
    if dp[low][col] != -1:
        return dp[low][col]
    if low == n and col == m:
        return 1
    route = 0
    height = data[low][col]
    up = data[low - 1][col]
    down = data[low + 1][col]
    left = data[low][col - 1]
    right = data[low][col + 1]
    # up
    if up < height:
        route += dfs(low - 1, col)
    # down
    if down < height:
        route += dfs(low + 1, col)
    # left
    if left < height:
        route += dfs(low, col - 1)
    # right
    if right < height:
        route += dfs(low, col + 1)
    dp[low][col] = route
    return dp[low][col]


print(dfs(1, 1))
