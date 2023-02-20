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
    lis = [0] * 1001
    arr_idx = [0] * 1001
    lis[0] = arr[0]
    j = 0
    for i in range(len(arr)):
        if lis[j] < arr[i]:
            lis[j + 1] = arr[i]
            j += 1
            arr_idx[i] = j + 1
        else:
            idx = binary_search(0, j, arr[i], lis)
            lis[idx] = arr[i]
            arr_idx[i] = idx + 1
    return arr_idx, j + 1


n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
temp, length = get_lis(arr)
result = []
print(length)
for i in range(len(arr), -1, -1):
    if temp[i] == length:
        result.append(arr[i])
        length -= 1
result.sort()
print(" ".join(map(str, result)))
