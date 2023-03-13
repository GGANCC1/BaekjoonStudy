import sys

N = int(sys.stdin.readline().rstrip())
if N == 3:
    print(-1)
elif N == 4:
    for x in [3, 1, 4, 2]:
        print(x)
elif N % 2 == 0:
    print(N // 2 + 1)
    for i in range(2, N - 2):
        if i == N // 2:
            print(2)
        else:
            print(i + 1)
    print(1)
    print(N)
    print(N - 1)
else:
    for i in range(1, N - 2):
        print(i + 1)
    print(1)
    print(N)
    print(N - 1)