import sys

n = int(sys.stdin.readline().rstrip())
dt = {}
for i in range(n):
    k, v = map(int, sys.stdin.readline().rstrip().split())
    if k in dt.keys():
        dt[k].append(v)
    else:
        dt[k] = [v]
keys = list(dt.keys())
keys.sort()
cnt = 1
end_clock = sys.maxsize
for key in keys:
    dt[key].sort()
    for t in dt[key]:
        if t < end_clock:
            end_clock = t
        elif key >= end_clock:
            cnt += 1
            end_clock = t
print(cnt)
