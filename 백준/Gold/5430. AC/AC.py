import sys
from collections import deque

tc = int(sys.stdin.readline().rstrip())

for i in range(tc):
    cmd = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    arr = sys.stdin.readline().rstrip()[1:-1].split(',')
    if n != 0:
        dq = deque(int(x) for x in arr)
    else:
        dq = deque()
    flag = 1
    # 0은 큐의 앞쪽, 1은 큐의 뒤쪽
    direction = 0
    for p in cmd:
        if p == 'R':
            if direction:
                direction = 0
            else:
                direction = 1
        else:
            if n == 0 or len(dq) == 0:
                print("error")
                flag = 0
                break
            else:
                if direction:
                    dq.pop()
                else:
                    dq.popleft()
    if flag:
        print('[', end='')
        if direction and len(dq) != 0:
            for j in range(len(dq)-1, 0, -1):
                print(dq[j], end=',')
            print(dq[0], end='')
        elif len(dq) != 0:
            for j in range(len(dq)-1):
                print(dq[j], end=',')
            print(dq[len(dq)-1], end='')
        print(']')
