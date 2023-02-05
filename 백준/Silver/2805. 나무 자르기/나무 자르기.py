import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()


def binary_search(start, end):
    low = start
    high = end
    while low <= high:
        num = 0
        mid = int((low + high) / 2)
        for i in arr:
            if i > mid:
                num += (i - mid)
        if num < k:
            high = mid - 1
        else:
            low = mid + 1
    return high


print(binary_search(0, arr[-1]))