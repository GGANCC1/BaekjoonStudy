a, b = map(float, input().split())
time = float(input())
b += time
a += int(b/60)
a = int(a%24)
b = int(b%60)
print(a, b)