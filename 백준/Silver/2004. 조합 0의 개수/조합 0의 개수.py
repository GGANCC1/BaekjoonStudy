import math
import sys

def fv(num):
    count = 0
    while num >= 5:
        count += (num // 5)
        num //= 5
    return count

def tw(num):
    count = 0
    while num >= 2:
        count += (num // 2)
        num //= 2
    return count

n, k = map(int, sys.stdin.readline().rstrip().split())
five = fv(n) - fv(n-k) - fv(k)
two = tw(n) - tw(n-k) - tw(k)
print(int(min(five, two)))

