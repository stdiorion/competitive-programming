MOD = 998244353
N, M, K = map(int, input().split())

def comb(n, r, p=None):
    if not 0 <= r <= n: return 0
    r = min(r, n - r)
    if p is None: res = fact[n] * factinv[r] * factinv[n-r]
    else: res = fact[n] * factinv[r] * factinv[n-r] % p
    return res

p = MOD
fact, factinv, inv = [1, 1], [1, 1], [0, 1]
 
for i in range(2, N + 1):
    fact.append(fact[-1] * i % p)
    inv.append(-inv[p % i] * (p // i) % p)
    factinv.append(factinv[-1] * inv[-1] % p)

def solve(n, k):
    if n == 1:
        return M
    else:
        if k:
            return solve(n - k, 0) * comb(n - 1, k, MOD) % MOD
        else:
            return M * pow(M - 1, n - 1, MOD) % MOD
ans = 0
for i in range(K + 1):
    ans += solve(N, i)
    ans %= MOD
print(ans)