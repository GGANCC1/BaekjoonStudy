import sys

R, C, H, W = map(int, sys.stdin.readline().rstrip().split())
data = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(R)]
pre1 = [[0] * (C + 1) for _ in range(R + 1)]
pre2 = [[0] * (C + 1) for _ in range(R + 1)]


def binary_search(start, end):
    low = start
    high = end
    while low <= high:
        flag = False
        mid = (low + high) // 2
        # mid 값을 기준으로 크고 작음을 판별해 미리 저장
        for i in range(1, R + 1):
            for j in range(1, C + 1):
                if data[i - 1][j - 1] > mid:
                    pre1[i][j] = 1
                else:
                    pre1[i][j] = -1
        # 그렇게 저장한 값의 누적합을 미리 계산하여 H * W의 구간을 빠르게 판별할 수 있도록 함
        for i in range(1, R + 1):
            for j in range(1, C + 1):
                pre2[i][j] = pre2[i - 1][j] + pre2[i][j - 1] - pre2[i - 1][j - 1] + pre1[i][j]
        # data 배열 내에서 각 H * W 구간을 순회하며, mid값이 중간값으로 존재가능한 값인지를 판별
        # 만약 가능하다면 mid값을 감소시키고 아니라면 증가시킴
        for i in range(H, R + 1):
            for j in range(W, C + 1):
                if pre2[i][j] - pre2[i - H][j] - pre2[i][j - W] + pre2[i - H][j - W] <= 0:
                    flag = True
                    break
            if flag:
                break
        if flag:
            high = mid - 1
        else:
            low = mid + 1
    return low


print(binary_search(0, R * C))
