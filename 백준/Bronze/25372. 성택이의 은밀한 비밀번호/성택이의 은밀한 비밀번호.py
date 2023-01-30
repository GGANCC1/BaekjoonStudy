import sys

n = int(sys.stdin.readline().rstrip())
for i in range(n):
    password = sys.stdin.readline().rstrip()
    if 6 <= len(password) <= 9:
       print("yes")
    else:
        print("no")