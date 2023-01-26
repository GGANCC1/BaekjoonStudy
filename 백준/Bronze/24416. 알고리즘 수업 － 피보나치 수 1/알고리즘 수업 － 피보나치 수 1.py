import sys

x = int(sys.stdin.readline().rstrip())
f = [0] * 41
cnt = [0, 0]


def fib(n):
    if n == 1 or n == 2:
        cnt[0] += 1
        return 1
    else:
        return (fib(n - 1) + fib(n - 2));


def fibonacci(n) :
    f[1] = 1
    f[2] = 1
    for i in range(3, n + 1, 1):
        cnt[1] += 1
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

fib(x)
fibonacci(x)
print(cnt[0], cnt[1])

