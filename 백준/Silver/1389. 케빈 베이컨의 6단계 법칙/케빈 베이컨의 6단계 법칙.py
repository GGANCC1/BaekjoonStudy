import sys

def sol():
    dist = [[INF] * N for _ in range(N)]
    for i in range(M):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        dist[a - 1][b - 1] = 1
        dist[b - 1][a - 1] = 1
    # dist[i][j]는 i에서 j까지 가는 최단비용을 뜻함.
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if dist[j][k] > dist[j][i] + dist[i][k]:
                    dist[j][k] = dist[j][i] + dist[i][k]
    return dist


INF = sys.maxsize
N, M = map(int, sys.stdin.readline().rstrip().split())
arr = sol()
min_value = INF
for i in range(N):
    if min_value > sum(arr[i]) - arr[i][i]:
        min_value = sum(arr[i]) - arr[i][i]
        ans = i + 1
print(ans)
