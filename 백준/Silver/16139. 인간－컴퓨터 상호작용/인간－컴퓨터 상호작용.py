import sys

string = str(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())
prefix_sum = [[0] * 26 for _ in range(len(string))]
for i in range(len(string)):
    prefix_sum[i][ord(string[i]) - 97] += 1
    for j in range(26):
        prefix_sum[i][j] += prefix_sum[i-1][j]
for i in range(n):
    s, a, b = map(str, sys.stdin.readline().rstrip().split())
    a, b = int(a), int(b)
    if a == 0:
        print(prefix_sum[b][ord(s) - 97])
    else:
        print(prefix_sum[b][ord(s) - 97] - prefix_sum[a - 1][ord(s) - 97])



