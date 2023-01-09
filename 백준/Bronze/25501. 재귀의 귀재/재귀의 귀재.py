import sys

def recursion(s, l, r):
    global num
    num += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l + 1, r - 1)


def isPalindrome(s):
    return recursion(s, 0, len(s) - 1)

n = int(input())
list = [sys.stdin.readline().rstrip() for _ in range(n)]
for i in list:
    num = 0
    print(isPalindrome(i), num)
