import sys
import time

n = int(sys.stdin.readline().rstrip())
column = [True]*n
slash = [True]*(2*n-1)
backSlash = [True]*(2*n-1)

def dfs(y):
    if y == n:
        return 1
    count = 0
    for x in range(n):
        if column[x] and slash[y+x] and backSlash[y-x]:
            column[x] = slash[y+x] = backSlash[y-x] = False
            count += dfs(y+1)
            column[x] = slash[y + x] = backSlash[y - x] = True
    return count

print(dfs(0))