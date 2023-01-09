import sys
n = int(input())
list= [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
list.sort(key=lambda x: (x[1], x[0]))
for i in list:
    print(i[0], i[1])