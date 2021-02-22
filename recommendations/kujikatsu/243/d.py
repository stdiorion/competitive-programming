n, prime = map(int, input().split())

svc = []

for _ in range(n):
    start, end, cost = map(int, input().split())
    end += 1
    svc.append((start, cost))
    svc.append((end, -cost))

svc.sort()

pay = 0
prev = 0
total = 0

for day, cost in svc:
    total += min(pay, prime) * (day - prev)
    pay += cost
    prev = day

print(total)