x, y, a, b, c = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

p.sort(reverse=True)
q.sort(reverse=True)
r.sort(reverse=True)

rng = p[:x] + q[:y]
rng.sort()

for i, (col, non) in enumerate(zip(rng, r)):
    if col < non:
        rng[i] = non

print(sum(rng))