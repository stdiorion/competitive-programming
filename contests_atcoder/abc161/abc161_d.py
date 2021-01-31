from collections import defaultdict

k = int(input())

lunlun = []

memo = defaultdict(list)

def dfs(d, now):
    if d == 0: lunlun.append(now)
    else:
        last = now % 10
        if last != 0: dfs(d - 1, now * 10 + (last - 1))
        dfs(d - 1, now * 10 + (last))
        if last != 9: dfs(d - 1, now * 10 + (last + 1))


for d in range(10):
    for j in range(1, 10):
        dfs(d, j)

print(lunlun[k - 1])