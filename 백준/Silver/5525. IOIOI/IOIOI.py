import sys

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
string = sys.stdin.readline().rstrip()
P = ""
for i in range(2 * N + 1):
    if i % 2 == 0:
        P += "I"
    else:
        P += "O"
ans = 0
for i in range(M - 2 * N):
    if string[i] == "O":
        continue
    if string[i:i + 2 * N + 1] == P:
        ans += 1
print(ans)