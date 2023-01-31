import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
arr = []
prefix_num = [[0]*n for i in range(n)]
for i in range(n):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    num = 0
    arr.append([])
    for j in range(len(row)):
        num += row[j]
        arr[i].append(row[j])
        prefix_num[i][j] = num
for i in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
    result = 0
    for j in range(x1-1, x2, 1):
        if y1 == 1:
            result += prefix_num[j][y2 - 1]
        else:
            result += prefix_num[j][y2 - 1] - prefix_num[j][y1 - 2]
    print(result)