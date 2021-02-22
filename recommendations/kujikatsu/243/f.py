MOD = 10 ** 9 + 7
n = int(input())
x = list(map(int, input().split()))

fact, inv = [1, 1], [0, 1]
 
for i in range(2, n + 1):
    fact.append(fact[-1] * i % MOD)
    inv.append(-inv[MOD % i] * (MOD // i) % MOD)

x = [b - a for a, b in zip(x, x[1:])]
ans = 0
count = 0

for i in range(1, n): 
    count += fact[n - 1] * inv[i] % MOD
    ans += count * x[i - 1] % MOD
    ans %= MOD

print(ans)