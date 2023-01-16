import sys

s = sys.stdin.readline().rstrip()
my_dict = {}
for i in range(len(s)):
    for j in range(i+1, len(s)+1, 1):
        if s[i:j] not in my_dict.keys():
            my_dict[s[i:j]] = 1
print(len(my_dict))

