import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
board = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(n)]
minimum = []

start_y = 0
while start_y < n-7:
    start_x = 0
    while start_x < m-7:
        pattern = [['W', 'B'], ['B', 'W']]
        count = 0
        for i in range(start_y, start_y+8, 1):
            for j in range(start_x, start_x+8, 1):
                if not pattern[i%2][j%2] == board[i][j]:
                    count += 1
        minimum.append(count)

        count = 0
        pattern = [['B', 'W'], ['W', 'B']]
        for i in range(start_y, start_y+8, 1):
            for j in range(start_x, start_x+8, 1):
                if not pattern[i%2][j%2] == board[i][j]:
                    count += 1
        minimum.append(count)
        start_x += 1
    start_y += 1
print(min(minimum))
