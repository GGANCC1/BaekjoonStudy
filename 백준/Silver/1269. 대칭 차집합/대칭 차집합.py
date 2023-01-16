import sys
from collections import Counter

n, m = map(int, sys.stdin.readline().rstrip().split())
list1 = list(map(int, sys.stdin.readline().rstrip().split()))
list2 = list(map(int, sys.stdin.readline().rstrip().split()))
intersection = len(set(list1) & set(list2))
print(n+m-2*intersection)
