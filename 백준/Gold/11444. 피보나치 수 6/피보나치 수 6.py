import sys

num = int(sys.stdin.readline().rstrip())
memo = {0: 0, 1: 1, 2: 1}
mod = 1000000007


def sol(n):
    if n in memo.keys():
        return memo[n]
    if n % 2 == 0:
        a = sol(n // 2 + 1) % mod
        b = sol(n // 2 - 1) % mod
        c = sol(n // 2)
        memo[n] = (c * (a + b)) % mod
        return memo[n]
    else:
        a = sol(n // 2) % mod
        b = sol(n // 2 + 1) % mod
        memo[n] = (a * a + b * b) % mod
        return memo[n]


print(sol(num))
