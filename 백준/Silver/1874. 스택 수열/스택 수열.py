import sys
from collections import deque


n = int(sys.stdin.readline().rstrip())
stack = deque()
ans = deque()
num = 1
for i in range(n):
    x = int(sys.stdin.readline().rstrip())
    while True:
        if x > num:
            stack.append(num)
            ans.append("+")
            num += 1
        elif x == num:
            ans.append("+")
            ans.append("-")
            num += 1
            break
        else:
            if x != stack[-1]:
                print("NO")
                exit(0)
            else:
                stack.pop()
                ans.append("-")
                break
for i in ans:
    print(i)