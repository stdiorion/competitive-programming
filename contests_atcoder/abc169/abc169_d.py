from decimal import Decimal

n = int(input())

def factorize2(n):
    factor = []

    b, e = 2, 0
    while b * b <= n:
        while n % b == 0:
            n //= b
            e += 1
        if e:
            factor.append((b, e))
        b, e = b + 1, 0

    if n > 1:
        factor.append((n, 1))

    return factor

ans = 0

for p, e in factorize2(n):
    ans += int((-1 + Decimal(1 + 8 * e).sqrt()) / 2)

print(ans)