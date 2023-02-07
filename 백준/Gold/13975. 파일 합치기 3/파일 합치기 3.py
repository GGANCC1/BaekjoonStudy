import sys
import heapq

tc = int(sys.stdin.readline().rstrip())
for _ in range(tc):
    k = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    heapq.heapify(data)
    ans = 0
    while len(data) > 1:
        a = heapq.heappop(data)
        b = heapq.heappop(data)
        ans += (a + b)
        heapq.heappush(data, a+ b)
    print(ans)