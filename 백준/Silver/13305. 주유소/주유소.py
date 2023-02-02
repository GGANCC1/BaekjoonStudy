import sys

n = int(sys.stdin.readline().rstrip())
distance = list(map(int, sys.stdin.readline().rstrip().split()))
cost = list(map(int, sys.stdin.readline().rstrip().split()))
current_cost = cost[0]
ans = 0
i = 0
while i < len(distance):
    num = distance[i]
    for j in range(i + 1, len(cost)):
        if cost[i] >= cost[j]:
            ans += num * cost[i]
            i = j
            break
        else:
            num += distance[j]
print(ans)