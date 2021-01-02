h, w, m = map(int, input().split())

blocks = [(h, i) for i in range(w)] + [(i, w) for i in range(h)]

for _ in range(m):
    a, b = tuple(map(int, input().split()))
    blocks.append((a - 1, b - 1))

blocks.sort()

print(blocks)