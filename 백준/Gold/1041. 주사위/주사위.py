import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
result = 0
s = []
if(n == 1):
    arr.sort()
    for i in range(5):
        result += arr[i]
else:
    s.append(min(arr[0], arr[5]))
    s.append(min(arr[1], arr[4]))
    s.append(min(arr[2], arr[3]))
    s.sort()
    min1 = s[0]
    min2 = s[0] + s[1]
    min3 = s[0] + s[1] + s[2]
    ans1 = (n - 2) * (n - 2) + 4 * (n - 1) * (n - 2)
    ans2 = 4 * (n - 2) + 4 * (n - 1)
    ans3 = 4
    result += ans1 * min1
    result += ans2 * min2
    result += ans3 * min3

print(result)