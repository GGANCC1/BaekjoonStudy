import sys

list = list(map(int, sys.stdin.readline().split()))
print(min(list[0], list[1], list[2]-list[0], list[3]-list[1]))