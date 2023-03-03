import sys

N, S = map(int, sys.stdin.readline().split())
arr = [0] + list(map(int, sys.stdin.readline().split()))
pre = [0] * (N + 1)
for i in range(1, len(arr)):
    pre[i] = pre[i - 1] + arr[i]
right = 1
left = 0
INF = sys.maxsize
ans = INF
while right <= N:
    if pre[right] - pre[left] >= S:
        ans = min(ans, right - left)
        left += 1
    else:
        right += 1
if ans == INF:
    print(0)
else:
    print(ans)
