import sys


def factorial(num):
    result = 1
    while num > 1:
        result *= num
        num -= 1
    return result


n, k = map(int, sys.stdin.readline().rstrip().split())
ans = (factorial(n) // factorial(n - k)) // factorial(k)
print(ans%10007)
