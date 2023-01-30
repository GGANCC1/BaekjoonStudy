import sys

a, b, c = map(int, sys.stdin.readline().rstrip().split())
print((((a+1)*(b+1))//(c+1))-1)
