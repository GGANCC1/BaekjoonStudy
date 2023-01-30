import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
prefix_sum = [0] * (n + 1)
numbers = [0] * m
numbers[0] = 1

for i in range(1, len(arr) + 1):
    prefix_sum[i] = (prefix_sum[i - 1] + arr[i - 1]) % m
    numbers[prefix_sum[i]] += 1
ans = 0
for i in numbers:
    if i >= 2:
        ans += (i * (i - 1)) // 2
print(ans)
