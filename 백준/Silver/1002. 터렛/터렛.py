import math
import sys

t = int(sys.stdin.readline().rstrip())
pt = {}
for i in range(t):
    pt['x1'], pt['y1'], pt['r1'], pt['x2'], pt['y2'], pt['r2'] = map(int, sys.stdin.readline().rstrip().split())
    distance = math.sqrt((pt['x1'] - pt['x2'])**2 + (pt['y1'] - pt['y2'])**2)
    if distance == 0:
        if pt['r1'] == pt['r2']:
            print(-1)
        else:
            print(0)
    elif distance == pt['r1'] + pt['r2'] or distance + pt['r1'] == pt['r2'] or distance + pt['r2'] == pt['r1']:
        print(1)
    elif distance + pt['r1'] < pt['r2'] or distance + pt['r2'] < pt['r1']:
        print(0)
    elif distance < pt['r1'] + pt['r2']:
        print(2)
    else:
        print(0)