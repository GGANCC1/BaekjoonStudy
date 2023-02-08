import sys

n = int(sys.stdin.readline().rstrip())
files = [sys.stdin.readline().rstrip() for x in range(n)]
check = [1] * 51
length = len(files[0])
for i in range(length):
    for j in range(1, n):
        if files[j][i] != files[0][i]:
            check[i] = 0
            break
for i in range(length):
    if check[i]:
        print(files[0][i], end='')
    else:
        print('?', end='')
