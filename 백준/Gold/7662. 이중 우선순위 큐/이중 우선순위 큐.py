import sys
import heapq

tc = int(sys.stdin.readline().rstrip())
check = [False] * 1000001
for i in range(tc):
    n = int(sys.stdin.readline().rstrip())
    maxQueue = []
    minQueue = []
    for j in range(n):
        cmd, element = map(str, sys.stdin.readline().rstrip().split())
        element = int(element)
        if cmd == 'I':
            heapq.heappush(maxQueue, (-element, j))
            heapq.heappush(minQueue, (element, j))
            check[j] = True
        elif cmd == 'D' and minQueue and maxQueue:
            if element == -1:
                while minQueue and not check[minQueue[0][1]]:
                    heapq.heappop(minQueue)
                if minQueue:
                    temp = heapq.heappop(minQueue)
                    check[temp[1]] = False
            else:
                while maxQueue and not check[maxQueue[0][1]]:
                    heapq.heappop(maxQueue)
                if maxQueue:
                    temp = heapq.heappop(maxQueue)
                    check[temp[1]] = False
        else:
            pass
    while maxQueue and not check[maxQueue[0][1]]:
        heapq.heappop(maxQueue)
    while minQueue and not check[minQueue[0][1]]:
        heapq.heappop(minQueue)
    if maxQueue and minQueue:
        print(-maxQueue[0][0], minQueue[0][0])
    else:
        print("EMPTY")
