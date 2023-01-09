def sol(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    return sol(num-1)+sol(num-2)


n = int(input())
print(sol(n))

