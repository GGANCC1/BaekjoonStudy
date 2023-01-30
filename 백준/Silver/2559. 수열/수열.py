import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
prefix_sum = [0] * (n - k + 1)
left = 0
right = k - 1
prefix_sum[0] = sum(arr[:k])
idx = 1
while True:
    if right == n - 1:
        break
    right += 1
    prefix_sum[idx] += prefix_sum[idx-1] - arr[left] + arr[right]
    left += 1
    idx += 1
print(max(prefix_sum))

