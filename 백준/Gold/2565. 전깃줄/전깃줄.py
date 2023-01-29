import sys

N = int(sys.stdin.readline().rstrip())
data = [0] * 500
for i in range(N):
    a, b = map(int, sys.stdin.readline().strip().split())
    data[a-1] = b


def binary_search(low, high, target, lis):
    while low < high:
        mid = (low + high) // 2
        if lis[mid] < target:
            low = mid + 1
        else:
            high = mid
    return high


def get_lis(arr):
    lis = [0] * 501
    for i in arr:
        if i != 0:
            lis[0] = i
            break
    j = 0
    # 정순
    for i in range(len(arr)):
        # 0은 연결된 전깃줄이 없다는 뜻이므로 패스
        if arr[i] == 0:
            continue
        if lis[j] < arr[i]:
            lis[j + 1] = arr[i]
            j += 1
        else:
            lis[binary_search(0, j, arr[i], lis)] = arr[i]
    return j + 1

print(N - get_lis(data))
