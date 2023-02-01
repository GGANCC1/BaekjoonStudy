import sys


def sol(s):
    for i in range(len(s) // 2):
        if s[i] != s[-(i + 1)]:
            print("no")
            return 0
    print("yes")
    return 0


while True:
    string = sys.stdin.readline().rstrip()
    if string == '0':
        break
    sol(string)
