def primality(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


N = int(input())
list = list(map(int, input().split()))
ans = 0
for i in list:
    if primality(i) and i != 1:
        ans += 1
print(ans)