import sys

n = int(input())
num = list(map(int, sys.stdin.readline().split()))
sorted_list = sorted(set(num))
my_dict = {sorted_list[i]: i for i in range(len(sorted_list))}
for i in num:
    print(my_dict[i], end=' ')