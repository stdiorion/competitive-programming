from decimal import Decimal, getcontext
from math import floor, ceil
getcontext().prec = 22

x, y, r = map(Decimal, input().split())

ans = 0

for h in range(floor(y - r), floor(y + r + 2)):
    dis2 = r ** 2 - (y - h) ** 2
    if dis2 < 0: continue
    dis = Decimal(dis2).sqrt()
    ans += floor(x + dis) - ceil(x - dis) + 1

print(ans)