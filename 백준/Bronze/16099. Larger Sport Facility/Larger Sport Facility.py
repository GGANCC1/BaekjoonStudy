import sys

n = int(sys.stdin.readline().rstrip())
for i in range(n):
    ax, ay, bx, by = map(int, sys.stdin.readline().rstrip().split())
    if ax*ay > bx*by:
        print("TelecomParisTech")
    elif ax*ay == bx*by:
        print("Tie")
    else:
        print("Eurecom")