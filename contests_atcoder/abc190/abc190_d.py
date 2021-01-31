n = int(input())

def factorize(n):
    fct = []
    b, e = 2, 0
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if b != 2 and e > 0:
            fct.append(e)
        b, e = b + 1, 0
    if n > 2:
        fct.append(1)
    return fct

d = factorize(n)

ans = 2

for x in d:
    ans *= x + 1

print(ans)