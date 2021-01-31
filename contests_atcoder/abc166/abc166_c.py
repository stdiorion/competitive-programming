n, m = map(int, input().split())

good = set(range(1, n + 1))

h = [0] + list(map(int, input().split()))

for _ in range(m):
    a, b = map(int, input().split())
    if h[a] <= h[b]:
        good.discard(a)
    if h[a] >= h[b]:
        good.discard(b)

print(len(good))