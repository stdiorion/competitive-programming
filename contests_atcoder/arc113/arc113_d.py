MOD = 998244353
n, m, k = map(int, input().split())

def solve(n, m, k):
    if n == m == 1:
        return k
    if n == 1:
        return pow(k, m, MOD)
    if m == 1:
        return pow(k, n, MOD)
    
    res = 0
    acc = 0

    for i in range(1, k + 1):
        acc = pow(i, n, MOD) - pow(i - 1, n, MOD)
        res += acc * pow(k - i + 1, m, MOD)
        res %= MOD
    
    return res

print(solve(n, m, k))