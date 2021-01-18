n, c = map(int, input().split())
services = [tuple(map(int, input().split())) for _ in range(n)]

tl = []

for sv in services:
    begin, end, cost = sv
    tl.append((begin, cost))
    tl.append((end+1, -cost))

tl.sort()

prev = 0
daily = 0
total = 0

for x in tl:
    now, dcost = x
    total += (now - prev) * min(daily, c)
    prev = now
    daily += dcost

print(total)