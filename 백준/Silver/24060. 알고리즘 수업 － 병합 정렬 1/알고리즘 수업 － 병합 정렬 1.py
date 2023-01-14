import sys

def merge_sort(arr, p, r):  # arr[p..r]을 오름차순 정렬한다.
    if p < r :
        q = (p + r) // 2       # q는 p, r의 중간 지점
        merge_sort(arr, p, q)      # 전반부 정렬
        merge_sort(arr, q + 1, r)  # 후반부 정렬
        merge(arr, p, q, r)        # 병합

# arr[p..q]와 arr[q+1..r]을 병합하여 arr[p..r]을 오름차순 정렬된 상태로 만든다.
# arr[p..q]와 arr[q+1..r]은 이미 오름차순으로 정렬되어 있다.
def merge(arr, p, q, r):
    i = p
    j = q + 1
    global count, k, ans
    tmp = []
    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            tmp.append(arr[i]) # tmp[t] <- A[i]; t++; i++;
            i += 1
        else:
            tmp.append(arr[j]) # tmp[t] <- A[j]; t++; j++;
            j += 1
    while i <= q:  # 왼쪽 배열 부분이 남은 경우
        tmp.append(arr[i]);
        i += 1
    while j <= r:  # 오른쪽 배열 부분이 남은 경우
        tmp.append(arr[j])
        j += 1
    i = p
    while i <= r:  # 결과를 arr[p..r]에 저장
        for x in tmp:
            arr[i] = x
            i += 1
            count += 1
            if count == k:
                ans = x

count = 0
ans = -1
n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
merge_sort(arr, 0, n-1)
print(ans)