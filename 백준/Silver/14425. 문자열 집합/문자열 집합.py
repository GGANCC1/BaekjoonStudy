import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
list1 = [sys.stdin.readline().rstrip() for _ in range(n)]
list2 = [sys.stdin.readline().rstrip() for _ in range(m)]
count = 0
for i in list2:
    if i in list1:
        count += 1
print(count)