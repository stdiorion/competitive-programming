n = int(input())
works = [tuple(map(int, input().split())) for _ in range(n)]
ans = 10 ** 12
for a in range(n):
    for b in range(n):
        if a != b:
            ans = min(ans, max(works[a][0], works[b][1]))
        else:
            ans = min(ans, works[a][0] + works[b][1])
print(ans)