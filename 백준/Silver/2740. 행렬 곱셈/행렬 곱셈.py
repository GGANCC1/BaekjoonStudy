import sys

an, am = map(int, sys.stdin.readline().rstrip().split())
arr1 = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(an)]
bn, bm = map(int, sys.stdin.readline().rstrip().split())
arr2 = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(bn)]
result = [[0] * bm for _ in range(an)]

for i in range(an):
    for j in range(bm):
        for k in range(bn):
            result[i][j] += arr1[i][k] * arr2[k][j]
for i in result:
    for j in i:
        print(j, end=' ')
    print('')
