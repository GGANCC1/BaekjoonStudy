import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
my_dict = {}
for i in range(1, n+1, 1):
    my_dict[str(i)] = sys.stdin.readline().rstrip()
reverse_dict = dict(map(reversed, my_dict.items()))
question = [sys.stdin.readline().rstrip() for _ in range(m)]
for q in question:
    if q in my_dict.keys():
        print(my_dict[q])
    elif q in reverse_dict.keys():
        print(reverse_dict[q])
