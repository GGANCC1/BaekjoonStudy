import sys

N = int(input())

list = [0]*10001

for i in range(N):
    n = int(sys.stdin.readline())
    list[n] += 1
for i in range(len(list)):
    if list[i] != 0:
        for j in range(list[i]):
            print(i)