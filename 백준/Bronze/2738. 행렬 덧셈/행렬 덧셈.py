import sys

N, M = map(int, input().split())
matrix1 = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
matrix2 = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
result = []
for i in range(N):
    result.append([])
    for j in range(M):
        result[i].append(matrix1[i][j]+matrix2[i][j])
for i in result:
    for j in i:
        print(j, end=' ')
    print('')