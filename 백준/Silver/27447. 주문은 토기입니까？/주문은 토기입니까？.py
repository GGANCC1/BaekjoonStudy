import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
guest = list(map(int, sys.stdin.readline().rstrip().split()))
time = [True] * (guest[-1] + 1)
time[0] = False
time[max(1, guest[0] - M)] = False
for i in guest:
    time[i] = False


def get_front(n):
    for i in range(n + 1, guest[-1]):
        if time[i]:
            return i


front = 0
if guest[-1] < 2 * N - 1 or guest[0] < 2:
    print("fail")
else:
    flag = 1
    for i in range(1, len(guest)):
        step = 1
        front = get_front(front)
        if front == None:
            print("fail")
            flag = 0
            break
        else:
            time[front] = False
            step += 1
        for j in range(max(front, guest[i] - M), guest[i]):
            if time[j]:
                time[j] = False
                step += 1
                break
        if step != 3:
            print("fail")
            flag = 0
            break
    if flag:
        print("success")
