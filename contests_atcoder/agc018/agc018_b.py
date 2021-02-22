from collections import Counter
n, m = map(int, input().split())
favs = [list(map(int, input().split())) for _ in range(n)]

indices = [0] * n
held = set(range(1, m + 1))

ans = n

for _ in range(m):
    for i in range(n):
        while favs[i][indices[i]] not in held:
            indices[i] += 1
    events = [favs[i][j] for i, j in enumerate(indices)]
    c = Counter(events).most_common(1)[0]
    held.discard(c[0])
    ans = min(ans, c[1])

print(ans)