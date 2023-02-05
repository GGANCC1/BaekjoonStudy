import sys

n = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())


def binary_search(start, end):
    low = start
    high = end
    while low <= high:
        mid = (low + high) // 2
        cnt = 0
        for i in range(1, n + 1):
            cnt += min(n, mid // i)
        if cnt < k:
            low = mid + 1
        else:
            high = mid - 1
    return low


print(binary_search(1, k))
