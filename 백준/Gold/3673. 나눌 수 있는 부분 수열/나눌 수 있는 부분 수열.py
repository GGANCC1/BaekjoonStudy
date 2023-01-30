import sys

tc = int(sys.stdin.readline().rstrip())
for i in range(tc):
    m, n = map(int, sys.stdin.readline().rstrip().split())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    prefix_sum = [0] * (n + 1)
    numbers = [0] * m
    numbers[0] = 1
    for j in range(1, len(arr) + 1):
        prefix_sum[j] = (prefix_sum[j - 1] + arr[j - 1]) % m
        numbers[prefix_sum[j]] += 1
    ans = 0
    for i in numbers:
        if i >= 2:
            ans += (i * (i - 1)) // 2
    print(ans)
