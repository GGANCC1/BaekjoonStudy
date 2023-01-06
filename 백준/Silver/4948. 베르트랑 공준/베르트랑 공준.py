def primality(n):
    i = 2
    if n==1:
        return False
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

list = []
while True:
    N = int(input())
    if N==0:
        break
    list.append(N)
for i in list:
    ans = 0
    for j in range(i+1, 2*i+1, 1):
        if primality(j):
            ans +=1
    print(ans)