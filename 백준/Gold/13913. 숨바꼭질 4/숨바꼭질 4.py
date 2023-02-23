import sys
from collections import deque


n, k = map(int, sys.stdin.readline().rstrip().split())
time = [100001] * 100001
time[n] = 0


def bfs():
    q = deque()
    q.append((n, str(n)))
    ans = sys.maxsize
    while q:
        current_pos, path = q.popleft()
        if current_pos == k:
            ans_time = min(ans, time[current_pos])
            ans_path = " ".join(map(str, path.split()))
            break
        next_pos = [current_pos - 1, current_pos + 1, current_pos * 2]
        for pos in next_pos:
            if 0 <= pos <= 100000 and time[pos] >= time[current_pos] + 1:
                time[pos] = time[current_pos] + 1
                q.append((pos, path + " " + str(pos)))
    return [ans_time, ans_path]


result = bfs()
print(result[0])
print(result[1])


