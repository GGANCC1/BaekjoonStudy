import sys
from collections import deque

n, k = map(int, sys.stdin.readline().rstrip().split())
q = deque()
q.extend([x for x in range(1, n + 1)])
ans = deque()
while len(q) > 0:
    for i in range(1, k):
        q.append(q[0])
        q.popleft()
    ans.append(q[0])
    q.popleft()
print("<", end='')
print(", ".join(map(str, ans)), end='')
print(">")