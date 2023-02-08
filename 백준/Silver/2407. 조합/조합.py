import sys

N, K = map(int, sys.stdin.readline().rstrip().split())


def factorial(n):
    num = 1
    for i in range(2, n + 1):
        num = (num * i)
    return num


result = factorial(N) // (factorial(K) * factorial(N - K))
print(result)
