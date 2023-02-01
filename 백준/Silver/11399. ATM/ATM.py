import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
s = [0] * n
s[0] = arr[0]
for i in range(1, len(arr)):
    s[i] = s[i-1] + arr[i]
print(sum(s))