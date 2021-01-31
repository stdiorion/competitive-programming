from decimal import Decimal
n, x = map(int, input().split())
drinks = [list(map(int, input().split())) for _ in range(n)]

alch = Decimal(0)

for i, d in enumerate(drinks):
    alch += Decimal(d[0]) * Decimal(d[1]) / Decimal(100)
    if alch > x:
        print(i + 1)
        exit()
else:
    print(-1)