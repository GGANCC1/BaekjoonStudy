import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
print(n // k, n % k)