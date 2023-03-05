import sys

string1 = sys.stdin.readline().strip()
string2 = sys.stdin.readline().strip()
dp = []
for i in range(len(string2) + 1):
    dp.append([])
    for j in range(len(string1) + 1):
        dp[i].append(0)

for i in range(1, len(string2) + 1):
    for j in range(1, len(string1) + 1):
        if string2[i-1] == string1[j-1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(max(dp[-1]))

