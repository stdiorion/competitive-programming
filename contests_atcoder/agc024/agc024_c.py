import sys
input = sys.stdin.readline
n = int(input())
a = [int(input()) for _ in range(n)]
x = [0] * n

i = 0
for c in a:
    if c == 0:
        i = 0
    if i < c:
        print(-1)
        exit()
    i += 1

for c, d in zip(a, a[1:]):
    if d - c > 1:
        print(-1)
        exit()

ans = 0
now = 0

for c in reversed(a):
    now -= 1
    if now == c:
        continue
    ans += c
    now = c

print(ans)