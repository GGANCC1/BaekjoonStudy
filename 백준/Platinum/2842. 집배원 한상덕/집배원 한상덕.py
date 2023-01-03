# bfs 알고리즘, 투 포인터 알고리즘
import sys
from collections import deque

def bfs(start_x, start_y, left, right):
    visit = [[False]*N for _ in range(N)]
    queue = deque([(start_x, start_y)])
    visit[start_x][start_y] = True
    K = 0   # 방문한 곳의 개수

    # stack이 empty stack이 될 때까지 반복
    while queue:
        # 현재 방문 지점
        x, y = queue.popleft()
        # 인접 노드 탐색, 현재 node가 방문한 적 없는 경우 visit = True로 변경
        for i in range(8):
            nx, ny = x+dr[i], y+dc[i]
            # 행렬 범위를 벗어나는 경우 재탐색
            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue
            # 범위는 벗어나지 않았으나 이미 방문한 노드인 경우 재탐색
            if visit[nx][ny]:
                continue
            # left, right의 범위 안에 들어가는 고도가 아닌 경우에만 탐색
            if all_altitude[left] <= altitude[nx][ny] <= all_altitude[right]:
                visit[nx][ny] = True
                queue.append((nx, ny))
                if board[nx][ny] == 'K':
                    K += 1
    return K

# 위, 아래, 좌, 우, 좌상, 우상, 우하, 좌하
dr = [-1, 1, 0, 0, -1, 1, 1, -1]
dc = [0, 0, -1, 1, -1, -1, 1, 1]

N = int(input())
board = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(N)]
altitude = [[int(x) for x in sys.stdin.readline().split()] for _ in range(N)]

houses = 0
all_altitude = []

# 출발점의 위치와 목적지의 개수를 파악
for i in range(N):
    for j in range(N):
        if board[i][j] == 'P':
            px, py = i, j
        elif board[i][j] == 'K':
            houses += 1
        all_altitude.append(altitude[i][j])

# 입력받은 지점들의 모든 고도값을 all_altitude에 저장하여 중복제거 및 정렬
all_altitude = sorted(set(all_altitude))

# 투 포인터 알고리즘을 위한 포인터
left, right = 0, 0
answer = sys.maxsize    # int의 최댓값

# left가 끝에 도달할 때까지만 반복
while left < len(all_altitude):
    K = 0
    # 시작점이 투 포인터의 범위 안에 들어가는 경우에만 시행
    if all_altitude[left] <= altitude[px][py] <= all_altitude[right]:
        K = bfs(px, py, left, right)

    # 모든 집을 방문한 경우
    if K == houses:
        # 최소 피로도 계산
        answer = min(answer, all_altitude[right]-all_altitude[left])
        left += 1
    # right가 아직 우측으로 이동 가능하다면
    elif (right + 1) < len(all_altitude):
        right += 1
    else:
        break
print(answer)