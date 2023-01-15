import sys


def binary_search(n):
    low = 0
    high = len(list1) - 1
    while low <= high:
        mid = (low + high) // 2
        if list1[mid] == n:
            return 1
        elif list1[mid] < n:
            low = mid + 1
        else:
            high = mid - 1
    return 0


int(input())
list1 = list(map(int, sys.stdin.readline().rstrip().split()))
list1.sort()
int(input())
list2 = list(map(int, sys.stdin.readline().rstrip().split()))
for i in list2:
    print(binary_search(i), end=' ')
