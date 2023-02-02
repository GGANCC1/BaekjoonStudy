import sys
from collections import deque

tc = int(sys.stdin.readline().rstrip())
importance = deque()
for i in range(tc):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    importance.extend(list(map(int, sys.stdin.readline().rstrip().split())))
    target = m
    cnt = 0
    while True:
        maximum = max(importance)
        num = importance.popleft()
        if maximum <= num:
            cnt += 1
            if target == 0:
                print(cnt)
                break
            else:
                target -= 1
        else:
            importance.append(num)
            if target == 0:
                target = len(importance) - 1
            else:
                target -= 1
    importance.clear()
