import sys
string1 = sys.stdin.readline().rstrip()
string2 = sys.stdin.readline().rstrip()
if len(string1) >= len(string2):
    print("go")
else:
    print("no")