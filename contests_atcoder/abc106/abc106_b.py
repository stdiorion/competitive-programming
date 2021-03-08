n = int(input())

div = [[] for _ in range(n + 1)]
for d in range(1, n + 1):
    for i in range(d, n + 1, d):
        div[i].append(d)

print(sum(len(x) == 8 and i % 2 == 1 for i, x in enumerate(div)))