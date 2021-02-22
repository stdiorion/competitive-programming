import sys
input = sys.stdin.readline
n = int(input())
a = [int(input()) for _ in range(n)]

want = {}

for x in a:
    if x in want:
        want[x + 1] = want.pop(x) + 1
    else:
        want[x + 1] = 1

print(n - max(want.values()))