import sys

r = 31
m = 1234567891
n = int(sys.stdin.readline().rstrip())
string = sys.stdin.readline().rstrip()
ans = 0

for i in range(n):
    ans += ((ord(string[i]) - 96) * pow(31, i)) % m
print(ans % m)