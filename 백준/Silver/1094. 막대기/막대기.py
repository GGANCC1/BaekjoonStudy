import sys

n = int(sys.stdin.readline().rstrip())
num = 64
minimum = 64
cnt = 1
while num > n:
    minimum //= 2
    cnt += 1
    if num - minimum >= n:
        num -= minimum
        cnt -= 1
print(cnt)