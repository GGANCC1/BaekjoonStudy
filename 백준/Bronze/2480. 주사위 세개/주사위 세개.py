dice = list(map(int, input().split()))
for i in range(3):
    if dice.count(dice[i])==3:
        print(10000+(dice[i]*1000))
        break
    elif dice.count(dice[i])==2:
        print(1000+(dice[i]*100))
        break
    elif i==2:
        print(max(dice)*100)