import sys

N = int(sys.stdin.readline())

list = []
my_dict = {}
sum = 0
for i in range(N):
    list.append(int(sys.stdin.readline()))
    sum += list[i]
    if list[i] in my_dict.keys():
        my_dict[list[i]] += 1
    else:
        my_dict[list[i]] = 1
list.sort()
sorted_dict = sorted(my_dict.items(), key=lambda x:x[1], reverse=True)

print(round(float(sum/N)))

print(list[(N-1)//2])

mode = [k for k, v in my_dict.items() if v==sorted_dict[0][1]]
if len(mode)!=1:
    mode.sort()
    print(mode[1])
else:
    print(mode[0])

print(list[-1] - list[0])
