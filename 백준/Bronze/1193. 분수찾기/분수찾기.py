X = int(input())
a = 1
b = 1
i = 2
cmp = 1
while X!=1:
    cmp += i
    if X <= cmp:
        if i%2 == 0:
            b = i
            for i in range(X-(cmp-i+1)):
                a += 1
                b -= 1
        else:
            a = i
            for i in range(X-(cmp-i+1)):
                a -= 1
                b += 1
        break
    i += 1
print(str(a) + '/' + str(b))