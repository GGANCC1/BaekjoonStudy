import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
prefix_sum = [0]
s = 0
for i in arr:
    s += i
    prefix_sum.append(s)
for i in range(k):
    a, b = map(int, sys.stdin.readline().split())
    print(prefix_sum[b]-prefix_sum[a-1])
