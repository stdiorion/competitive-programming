from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

# 長さの配列
l = []

prev = 1

for num in a:
    if num - prev > 0: l.append(num - prev)
    prev = num + 1

if N + 1 - prev > 0: l.append(N + 1 - prev)

k = min(l) if len(l) else 1

print(sum([-(-x // k) for x in l]))