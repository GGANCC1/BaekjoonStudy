import sys


def sol(d):
    global m
    if d == m:
        print(" ".join(map(str, arr)))
        return
    for i in range(len(nums)):
        if d == 0 or arr[-1] <= nums[i]:
            arr.append(nums[i])
            sol(d + 1)
            arr.pop()


n, m = map(int, sys.stdin.readline().split())
nums = list(set(map(int, sys.stdin.readline().split())))
nums.sort()
arr = []
sol(0)