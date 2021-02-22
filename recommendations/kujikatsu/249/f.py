from decimal import Decimal
floor = Decimal.__floor__
ceil = Decimal.__ceil__
x, y, r = map(Decimal, input().split())

ans = 0

for k in range(ceil(y - r), floor(y + r) + 1):
    root = Decimal(r * r - (y - k)** 2).sqrt()
    right = x + root
    left = x - root
    right = floor(right)
    left = ceil(left)
    ans += right - left + 1

print(ans)