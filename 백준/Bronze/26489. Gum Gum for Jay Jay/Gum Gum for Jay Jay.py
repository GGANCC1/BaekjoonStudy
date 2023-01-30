import sys

ans = 0
while True:
    try:
        line = input()
        ans += 1
    except EOFError:
        break

print(ans)