import sys

k = int(sys.stdin.readline().rstrip())
list = [list(map(int, sys.stdin.readline().split())) for _ in range(6)]
w, w_idx = 0, 0
h, h_idx = 0, 0
for i in range(len(list)):
    if list[i][0]==1 or list[i][0]==2:
        if w < list[i][1]:
            w = list[i][1]
            w_idx = i
    elif list[i][0]==3 or list[i][0]==4:
        if h < list[i][1]:
            h = list[i][1]
            h_idx = i
subW = abs(list[(w_idx - 1) % 6][1] - list[(w_idx + 1) % 6][1])
subH = abs(list[(h_idx - 1) % 6][1] - list[(h_idx + 1) % 6][1])
print(k * ((w * h) - (subW * subH)))


