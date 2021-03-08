n, Q = map(int, input().split())
a = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(Q)]

sa = sum(a)

for t, q in queries:
    if t == 1:
        if a[q - 1]:
            sa -= 1
        else:
            sa += 1
        a[q - 1] ^= 1
    if t == 2:
        print(int(sa >= q))