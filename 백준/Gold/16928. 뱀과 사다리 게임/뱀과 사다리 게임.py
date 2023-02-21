import sys
from collections import deque


def bfs(pos):
    global start, end
    q = deque()
    q.append(pos)
    visited = [110] * 110
    visited[1] = 0
    dx = [1, 2, 3, 4, 5, 6]
    ans = sys.maxsize
    while q:
        x, cnt = q.popleft()
        for i in range(6):
            flag = True
            nx = x + dx[i]
            if nx == 100:
                ans = min(ans, cnt + 1)
            elif nx < 101 and visited[nx] > cnt + 1:
                for j in range(N + M):
                    if nx == start[j]:
                        flag = False
                        if visited[end[j]] > cnt + 1:
                            visited[start[j]] = cnt + 1
                            visited[end[j]] = cnt + 1
                            q.append((end[j], cnt + 1))
                if flag:
                    visited[nx] = cnt + 1
                    q.append((nx, cnt + 1))
    return ans


N, M = map(int, sys.stdin.readline().split())
start = []
end = []
for i in range(N + M):
    f, t = map(int, sys.stdin.readline().split())
    start.append(f)
    end.append(t)
print(bfs((1, 0)))
