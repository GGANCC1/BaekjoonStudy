import sys

N, k = map(int, input().split())
list = list(map(int, sys.stdin.readline().rstrip().split()))
list.sort()
print(list[len(list)-k])