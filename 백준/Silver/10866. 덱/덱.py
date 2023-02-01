import sys
from collections import deque


def isEmpty():
    if len(dq) == 0:
        return 1
    else:
        return 0


n = int(sys.stdin.readline().rstrip())
dq = deque()

for i in range(n):
    try:
        string = sys.stdin.readline().rstrip()
        cmd, num = string.split()
    except:
        cmd = string
    if cmd == "push_back":
        dq.append(num)
    elif cmd == "push_front":
        dq.appendleft(num)
    elif cmd == "front":
        if isEmpty():
            print(-1)
        else:
            print(dq[0])
    elif cmd == "back":
        if isEmpty():
            print(-1)
        else:
            print(dq[-1])
    elif cmd == "pop_front":
        if isEmpty():
            print(-1)
        else:
            print(dq.popleft())
    elif cmd == "pop_back":
        if isEmpty():
            print(-1)
        else:
            print(dq.pop())
    elif cmd == "size":
        print(len(dq))
    elif cmd == "empty":
        print(isEmpty())