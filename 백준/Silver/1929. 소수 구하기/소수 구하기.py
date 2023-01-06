import sys

def primality(n):
    i = 2
    if n==1:
        return False
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

M, N = map(int, input().split())
for i in range(M, N+1, 1):
    if primality(i):
        print(i)

