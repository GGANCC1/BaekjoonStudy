import sys
import bisect

T = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().rstrip())
B = list(map(int, sys.stdin.readline().split()))
preA, preB = [], []
for i in range(n):
    num = A[i]
    preA.append(num)
    for j in range(i + 1, n):
        num += A[j]
        preA.append(num)
for i in range(m):
    num = B[i]
    preB.append(num)
    for j in range(i + 1, m):
        num += B[j]
        preB.append(num)
preB.sort()
preA.sort()
ans = 0
for i in range(len(preA)):
    l = bisect.bisect_left(preB, T - preA[i])
    r = bisect.bisect_right(preB, T - preA[i])
    ans += (r - l)
print(ans)
