from fractions import Fraction
a, b, c, d, e, f = map(int, input().split())

water = [x + y for x in range(0, f + 1, 100 * a) for y in range(0, f + 1, 100 * b) if 0 < x + y <= f]
water = list(set(water))

sugar = [x + y for x in range(0, f + 1, c) for y in range(0, f + 1, d) if x + y <= f]
sugar = list(set(sugar))

cur = 0

ans = (100 * a, 0)
maxd = Fraction(0)

for w in water:
    for s in sugar:
        if w + s > f:
            continue
        dns = Fraction(s, (w + s))
        if dns > maxd and e * w >= 100 * s:
            maxd = dns
            ans = (w + s, s)

print(*ans)