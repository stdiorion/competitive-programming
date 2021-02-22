from itertools import accumulate
n, k = map(int, input().split())
p = [int(x) - 1 for x in input().split()]
c = list(map(int, input().split()))

visited = [False] * n
loops = []
loopcost = []

for start in range(n):
    if visited[start]: continue
    now = start

    loop = []

    while not visited[now]:
        visited[now] = True
        loop.append(c[now])

        now = p[now]
    
    cost = sum(loop)
    loopcost.append(cost)
    loop = list(accumulate(loop))
    loop += [x + cost for x in loop]
    loops.append(loop)

ans = -float("inf")

for l, lc in zip(loops, loopcost):
    for i in range(len(l) - 1):
        for j in range(i + 1, len(l)):
            if j - i > k:
                continue
            score = l[j] - l[i]
            if lc > 0:
                score += lc * ((k - (j - i)) // (len(l) // 2))
            ans = max(ans, score)

print(ans)