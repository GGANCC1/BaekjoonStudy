import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
arr.sort()


def binary_search(start, end):
    low = start
    high = end
    while low <= high:
        mid = int((low + high) / 2)
        current = arr[0]
        cnt = 1
        for i in range(1, len(arr)):
            if arr[i] >= current + mid:
                cnt += 1
                current = arr[i]
        if cnt >= k:
            low = mid + 1
        else:
            high = mid - 1
    return high


print(binary_search(1, arr[-1] - arr[0]))
