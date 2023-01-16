import sys


def binary_search(n):
    low = 0
    high = len(my_dict) - 1
    while low <= high:
        mid = (low + high) // 2
        if my_dict[mid][0] == n:
            return my_dict[mid][1]
        elif my_dict[mid][0] < n:
            low = mid + 1
        else:
            high = mid - 1
    return 0


n = map(int, sys.stdin.readline().rstrip())
my_dict = {}
list1 = list(map(int, sys.stdin.readline().rstrip().split()))
for i in list1:
    if i not in my_dict.keys():
        my_dict[i] = 1
    else:
        my_dict[i] += 1
my_dict = list(sorted(my_dict.items()))
m = map(int, sys.stdin.readline().rstrip())
list2 = list(map(int, sys.stdin.readline().rstrip().split()))
for i in list2:
    print(binary_search(i), end=' ')
