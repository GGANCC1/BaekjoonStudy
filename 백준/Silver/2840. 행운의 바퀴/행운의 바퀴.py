n, k = map(int, input().split())
list = []
for _ in range(n):
    list.append('?')
idx = 0
flag = False
for _ in range(k):
    s, ch = input().split()
    s = int(s)
    ch = str(ch)
    idx += s
    idx %= n
    if list[idx]=='?':
        list[idx] = ch
        continue
    elif list[idx] != ch:
        flag = True
for e in list:
    if list.count(e) > 1 and e != '?':
        flag = True
if flag or n == 0:
    print('!')
else:
    for _ in range(n):
        print(list[idx], end='')
        idx-=1
        if idx<0:
            idx = n-1