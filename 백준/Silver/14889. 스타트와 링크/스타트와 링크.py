import sys

n = int(sys.stdin.readline().rstrip())
score = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
member = [True] * n
min_value = sys.maxsize


def calc_score():
    global n
    team1 = []
    team2 = []
    result = 0
    for i in range(len(member)):
        if member[i]:
            team1.append(i)
        else:
            team2.append(i)
    for i in range((n // 2) - 1):
        for j in range(i + 1, n // 2, 1):
            result += (score[team1[i]][team1[j]] + score[team1[j]][team1[i]])
            result -= (score[team2[i]][team2[j]] + score[team2[j]][team2[i]])
    return abs(result)


def is_promising():
    promising = []
    idx = 0
    for i in range(len(member)):
        if not member[i]:
            idx = i
    for i in range(idx + 1, len(member), 1):
        if member[i]:
            promising.append(i)
    return promising


def dfs(num):
    global min_value
    if num == n // 2:
        min_value = min(min_value, calc_score())
        return
    for i in is_promising():
        member[i] = False
        dfs(num + 1)
        member[i] = True

dfs(0)
print(min_value)
