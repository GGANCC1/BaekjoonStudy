import sys


def binary_search(low, high, target, lis):
    while low < high:
        mid = (low + high) // 2
        if lis[mid] < target:
            low = mid + 1
        else:
            high = mid
    return high


def get_lis(arr):
    lis = [0] * 1000001
    lis[0] = arr[0]
    j = 0
    # 정순
    for i in range(len(arr)):
        if lis[j] < arr[i]:
            lis[j + 1] = arr[i]
            j += 1
        else:
            lis[binary_search(0, j, arr[i], lis)] = arr[i]
    return j + 1


n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
print(get_lis(arr))
