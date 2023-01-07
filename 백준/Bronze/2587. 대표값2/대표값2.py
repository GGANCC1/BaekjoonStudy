
list = []
for i in range(5):
    list.append(int(input()))
print(int(sum(list)/5))
list.sort()
print(list[2])