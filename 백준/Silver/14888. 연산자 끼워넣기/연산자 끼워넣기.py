import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
operator = list(map(int, sys.stdin.readline().rstrip().split()))
max_value = pow(10,9) * (-1)
min_value = pow(10,9)
temp = [0] * 11
temp[0] = arr[0]

def calc(c, a, b):
    if c == 0:
        return a + b
    elif c == 1:
        return a - b
    elif c == 2:
        return a * b
    else:
        if a < 0:
            return (abs(a) // b) * (-1)
        return a // b

def is_promising():
    promising = []
    for i in range(len(operator)):
        if operator[i] != 0:
            promising.append(i)
    return promising

def dfs(num):
    global temp, max_value, min_value
    if not sum(operator):
        if max_value < temp[num - 1]:
            max_value = temp[num - 1]
        if min_value > temp[num - 1]:
            min_value = temp[num - 1]
        return
    for i in is_promising():
        operator[i] -= 1
        temp[num] = calc(i, temp[num - 1], arr[num])
        dfs(num + 1)
        operator[i] += 1

dfs(1)
print(max_value)
print(min_value)
