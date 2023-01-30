import sys

string = str(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())
prefix_sum = [[0] * 26 for _ in range(len(string))]
for i in range(len(string)):
    prefix_sum[i][ord(string[i]) - 97] = 1
    for j in range(26):
        prefix_sum[i][j] += prefix_sum[i-1][j]
for i in range(n):
    s, a, b = list(sys.stdin.readline().split())
    a, b = int(a), int(b)
    idx = ord(s) - 97
    if a == 0:
        print(prefix_sum[b][idx])
    else:
        print(prefix_sum[b][idx] - prefix_sum[a - 1][idx])



