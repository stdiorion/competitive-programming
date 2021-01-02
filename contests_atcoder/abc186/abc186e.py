import math

t = int(input())

def xgcd(a, b):
    x, y = 0, 1
    u, v = 1, 0

    while a != 0:
        q,r = b // a, b % a
        m,n = x - u * q, y - v * q
        b,a, x,y, u,v = a,r, u,v, m,n
    
    return b, x, y

def modinv(a, m):
    gcd, x, y = xgcd(a, m)
    return x % m if gcd == 1 else -1

for i in range(t):
    n, s, k = map(int, input().split())
    if (g := math.gcd(math.gcd(n, s), k)) != 1:
        n //= g
        s //= g
        k //= g

    if (ans := modinv(k, n)) != -1:
        print((ans * (n - s)) % n)
    else:
        print(-1)