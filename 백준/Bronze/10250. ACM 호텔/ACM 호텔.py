import math

N = int(input())
for i in range(N):
    h, w, n = map(int, input().split())
    x = math.ceil(n / h)
    ans = str(n - (x-1) * h)
    if x < 10:
        ans += "0"
    ans += str(x)
    print(ans)
