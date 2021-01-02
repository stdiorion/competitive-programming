from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
a = list(map(int, input().split()))

# 分割の情報を(開始地点, 長さ)のタプルのリストで保持
spl = [(1, N)]

for num in a:
    for s in spl:
        if s[0] <= num and num < s[0] + s[1]:
            spl.remove(s)
            if num - s[0] != 0: spl.append((s[0], num - s[0]))
            if s[0] + s[1] - num - 1 != 0: spl.append((num + 1, s[0] + s[1] - num - 1))
            break

l = [s[1] for s in spl]

k = min(l) if len(l) else 1

print(sum([-(-x // k) for x in l]))