from itertools import accumulate

MOD = 10 ** 9 + 7
n, k = map(int, input().split())

def comb(n, r):
    if not 0 <= r <= n: return 0
    return fact[n] * factinv[r] % MOD * factinv[n - r] % MOD

N = 2 * n
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

k = min(k, n - 1)

ans = 0
for i in range(k + 1):
    ans += comb(n, i) * comb(n - 1, i) % MOD

print(ans % MOD)