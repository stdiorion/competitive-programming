MOD = 10 ** 9 + 7

n = int(input())

def cmb(n, r, p):
    if r < 0 or n < r:
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

p = MOD
N = n  # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用
fact_append = fact.append
inv_append = inv.append
factinv_append = factinv.append
 
for i in range(2, N + 1):
    fact_append((fact[-1] * i) % p)
    inv_append((-inv[p % i] * (p // i)) % p)
    factinv_append((factinv[-1] * inv[-1]) % p)

ans = 0

for i in range(2, n + 1):
    ans += (pow(2, i, MOD) - 2) * pow(8, n - i, MOD) * cmb(n, i, MOD)
    ans %= MOD

print(ans)