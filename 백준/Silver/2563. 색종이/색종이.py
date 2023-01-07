list = [[int(0) for _ in range(100)] for _ in range(100)]
size = 0
N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    for j in range(89-b, 99-b, 1):
        for k in range(a, a+10, 1):
            if list[j][k]:
                continue
            list[j][k] = 1
            size += 1
print(size)