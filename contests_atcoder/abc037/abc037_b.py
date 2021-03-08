n, q = map(int, input().split())
queries = [tuple(map(int, input().split())) for _ in range(q)]

a = [0] * n

for l, r, t in queries:
    for i in range(l - 1, r):
        a[i] = t

print(*a, sep="\n")