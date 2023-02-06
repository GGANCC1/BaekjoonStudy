import sys
from collections import deque

tc = int(sys.stdin.readline().rstrip())
arr = [0] * 21
for i in range(tc):
    string = sys.stdin.readline().rstrip()
    try:
        cmd, num = string.split()
        num = int(num)
    except:
        cmd = string
    if cmd == "add":
        if not arr[num]:
            arr[num] = 1
    elif cmd == "remove":
        if arr[num]:
            arr[num] = 0
    elif cmd == "check":
        if arr[num]:
            print(1)
        else:
            print(0)
    elif cmd == "toggle":
        if arr[num]:
            arr[num] = 0
        else:
            arr[num] = 1
    elif cmd == "all":
        arr = [1] * 21
    elif cmd == "empty":
        arr = [0] * 21
