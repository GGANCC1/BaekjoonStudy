import sys

n = int(input())
list = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
for i in range(n):
    rating = 1
    for j in list:
        if list[i][0] < j[0] and list[i][1] < j[1]:
            rating += 1
    print(rating, end=' ')