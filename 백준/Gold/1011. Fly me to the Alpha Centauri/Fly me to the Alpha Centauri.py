import sys

n = int(sys.stdin.readline().rstrip())
for i in range(n):
    start, end = map(int, sys.stdin.readline().split())
    distance = end - start
    move = 1
    cnt = 0
    while distance >= move:
        distance -= 2 * move
        cnt += 2
        move += 1
    if distance <= -(move - 1):
        cnt -= 1
    elif distance > 0:
        cnt += 1
    else:
        pass
    print(cnt)
