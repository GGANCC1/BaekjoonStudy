n = int(input())
cnt = 0
temp = int(n/5)
for _ in range(int(n/5) + 1):
    if (n - (temp*5))%3 == 0:
        cnt = temp + (n - (temp*5))/3
        break
    else:
        temp -=1
if cnt == 0:
    cnt = -1
print(int(cnt))