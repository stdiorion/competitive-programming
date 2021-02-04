from itertools import combinations_with_replacement

n, m, q = map(int, input().split())
pairs = [tuple(map(int, input().split())) for _ in range(q)]

ans = 0

for a in combinations_with_replacement(range(1, m + 1), n):
    points = 0
    for i1, i2, c, point in pairs:
        i1 -= 1
        i2 -= 1
        points += point if a[i2] - a[i1] == c else 0
    ans = max(ans, points)

print(ans)