n, p = map(int, input().split())
list = []
count = 0

for i in range(0, 8):
    list.append([])
for i in range(0, n):
    a, b = map(int, input().split())
    while list[a] and list[a][0] > b:
        list[a].pop(0)
        count += 1
    if list[a] and list[a][0] == b:
        list[a].pop(0)
        count -= 1
    list[a].insert(0, b)
    count += 1
print(count)
