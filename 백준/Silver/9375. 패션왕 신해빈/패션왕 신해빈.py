import sys

n = int(sys.stdin.readline().rstrip())
for i in range(n):
    my_dict = {}
    m = int(sys.stdin.readline().rstrip())
    for j in range(m):
        x, y = map(str, sys.stdin.readline().rstrip().split())
        if y not in my_dict.keys():
            my_dict[y] = [x]
        else:
            my_dict[y].append(x)
    result = 1
    for key in my_dict:
        result *= (len(my_dict[key]) + 1)
    result -= 1
    print(result)
