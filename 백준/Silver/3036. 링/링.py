import sys
import math
from fractions import Fraction

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
for i in range(1, len(arr), 1):
    ans = Fraction(arr[0], arr[i])
    if ans%1==0 and ans!=0:
        print(ans, end='')
        print('/1')
    else:
        print(ans)