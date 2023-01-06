def primality(n):
    i = 2
    if n==1:
        return False
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

N = int(input())
for i in range(N):
    n = int(input())
    if n%2==0:
        a = int(n/2)
        b = int(n/2)
    else:
        a = int(((n-1)/2))
        b = a+1
    while not primality(a) or not primality(b):
        a -= 1
        b += 1
    print(str(a) + " " + str(b))