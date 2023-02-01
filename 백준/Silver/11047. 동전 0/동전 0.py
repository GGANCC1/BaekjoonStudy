import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
arr.sort(reverse=True)
cnt = 0
for i in arr:
    if k >= i:
        cnt += (k // i)
        k -= (k // i) * i
print(cnt)