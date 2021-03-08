MOD = 998244353
d = int(input())

def comb(n, r):
    if not 0 <= r <= n: return 0
    return fact[n] * factinv[r] % MOD * factinv[n-r] % MOD

N = 2 * d
fact = [0] * (N + 1)
factinv = [0] * (N + 1)
inv = [0] * (N + 1)
fact[0] = fact[1] = factinv[0] = factinv[1] = inv[1] = 1
 
for i in range(2, N + 1):
    fact[i] = fact[i - 1] * i % MOD

factinv[N] = pow(fact[N], MOD - 2, MOD)

for i in range(N, 1, -1):
    inv[i] = fact[i - 1] * factinv[i] % MOD
    factinv[i - 1] = factinv[i] * i % MOD

print(comb(2 * d, d) * inv[2] % MOD)