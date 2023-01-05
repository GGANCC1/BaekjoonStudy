import math
a, b, v = map(float, input().split())
v -= a
print(math.ceil(v/(a-b)) + 1)