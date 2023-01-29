import sys

N = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().strip().split()))


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


ans = [0] * N
for i in range(1, N+1, 1):
    ans[i-1] += get_lis(data[:i])
data.reverse()
for i in range(1, N+1, 1):
    ans[N-i] += get_lis(data[:i])
print(max(ans) - 1)
