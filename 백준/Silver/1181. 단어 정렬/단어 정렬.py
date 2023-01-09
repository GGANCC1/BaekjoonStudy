import sys

n = int(input())
ans = [sys.stdin.readline().rstrip() for _ in range(n)]
ans = list(set(ans))
my_dict = {}
for i in ans:
    l = len(i)
    if l not in my_dict.keys():
        my_dict[l] = []
    my_dict[l].append(i)
sorted_dict = sorted(my_dict.items())
for i in sorted_dict:
    i[1].sort()
    for j in i[1]:
        print(j)