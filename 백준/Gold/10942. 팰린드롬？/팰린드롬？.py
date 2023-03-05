import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))
dp = [[False] * N for _ in range(N)]
for i in range(N):
    dp[i][i] = True
for i in range(N - 1):
    if arr[i] == arr[i + 1]:
        dp[i][i + 1] = True
for i in range(2, N):
    for j in range(N - i):
        if arr[j] == arr[j + i] and dp[j + 1][j + i - 1]:
            dp[j][j + i] = True
M = int(sys.stdin.readline().rstrip())
for i in range(M):
    S, E = map(int, sys.stdin.readline().split())
    if dp[S-1][E-1]:
        print(1)
    else:
        print(0)