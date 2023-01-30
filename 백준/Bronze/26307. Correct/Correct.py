import sys

h, m = map(int, sys.stdin.readline().rstrip().split())
print((h - 9) * 60 + m)
