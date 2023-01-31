import sys


def isEmpty():
    if len(stack) == 0:
        return 1
    else:
        return 0


n = int(sys.stdin.readline().rstrip())
stack = []
for i in range(n):
    try:
        string = sys.stdin.readline().rstrip()
        cmd, num = string.split()
    except:
        cmd = string
    if cmd == "push":
        stack.append(num)
    elif cmd == "top":
        if isEmpty():
            print(-1)
        else:
            print(stack[-1])
    elif cmd == "pop":
        if isEmpty():
            print(-1)
        else:
            print(stack.pop(-1))
    elif cmd == "size":
        print(len(stack))
    elif cmd == "empty":
        print(isEmpty())
