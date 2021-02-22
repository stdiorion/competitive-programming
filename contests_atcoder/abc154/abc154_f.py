MOD = 10 ** 9 + 7
r1, c1, r2, c2 = map(int, input().split())

def comb(n, r, p=MOD):
    if not 0 <= r <= n: return 0
    r = min(r, n - r)
    if p is None: res = fact[n] * factinv[r] * factinv[n-r]
    else: res = fact[n] * factinv[r] % p * factinv[n-r] % p
    return res

p = MOD
N = r2 + c2 + 2
fact, factinv, inv = [1, 1], [1, 1], [0, 1]
factappend = fact.append
invappend = inv.append
factinvappend = factinv.append

for i in range(2, N + 1):
    factappend(fact[-1] * i % p)
    invappend(-inv[p % i] * (p // i) % p)
    factinvappend(factinv[-1] * inv[-1] % p)

r1 -= 1
c1 -= 1

ans = 0
ans += comb(r2 + c2 + 2, r2 + 1)
ans -= comb(r2 + c1 + 2, r2 + 1)
ans -= comb(r1 + c2 + 2, r1 + 1)
ans += comb(r1 + c1 + 2, r1 + 1)
print(ans % MOD)