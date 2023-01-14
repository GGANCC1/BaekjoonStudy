import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
ans = 0
for i in range(0, len(arr), 1):
    for j in range(i+1, len(arr), 1):
        for k in range(j+1, len(arr), 1):
            num = (arr[i] + arr[j] + arr[k])
            if ans < num <= m:
                ans = num
print(ans)