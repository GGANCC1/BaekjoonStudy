import sys
def get_gcd(x, y):
    if x < y:
        x, y = y, x
    while True:
        z = x % y
        if z == 0:
            return y
        x = y
        y = z

n = int(sys.stdin.readline().rstrip())
list = []
for i in range(n):
    list.append(int(sys.stdin.readline().rstrip()))
list.sort()
gcd = list[1] - list[0]

for i in range(2, n, 1):
    gcd = get_gcd(gcd, list[i] - list[i - 1])

for i in range(2, gcd + 1, 1):
    if gcd%i==0:
        print(i, end=' ')