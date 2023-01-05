N = int(input())
for i in range(N):
    k = int(input())
    n = int(input())
    under_floor = list(int(i) for i in range(1, n+1))
    for j in range(k):
        current_floor = []
        for l in range(n):
            current_floor.append(sum(under_floor[0:l+1]))
        under_floor = current_floor
    print(current_floor[-1])