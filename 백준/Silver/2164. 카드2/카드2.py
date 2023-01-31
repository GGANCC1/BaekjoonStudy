import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
dq = deque()
dq.extend([x for x in range(1, n + 1)])
while len(dq) != 1:
    dq.popleft()
    dq.append(dq.popleft())
print(dq[0])
