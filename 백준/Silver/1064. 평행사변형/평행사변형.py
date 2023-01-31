import sys
import math

x1, y1, x2, y2, x3, y3 = map(int, sys.stdin.readline().rstrip().split())
distance = [math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2)), math.sqrt(pow(x1 - x3, 2) + pow(y1 - y3, 2)),
            math.sqrt(pow(x2 - x3, 2) + pow(y2 - y3, 2))]
distance.sort()
if (x1-x2)*(y1-y3) == (y1-y2)*(x1-x3):
    print(-1.0)
else:
    print(2*(distance[-1] - distance[0]))
