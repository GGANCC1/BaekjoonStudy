import sys
from collections import Counter

n, m = map(int, sys.stdin.readline().rstrip().split())
list1 = Counter(sys.stdin.readline().rstrip() for _ in range(n))
list2 = [sys.stdin.readline().rstrip() for _ in range(m)]
ans = []
for i in list2:
    if list1[i]:
        ans.append(i)
ans.sort()
print(len(ans))
if len(ans):
    print("\n".join(ans))
