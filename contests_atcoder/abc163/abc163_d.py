MOD = 10 ** 9 + 7
n, k = map(int, input().split())

ans = 0

for i in range(k, n + 2):
    ans += (n - i + 1 + n) * i // 2
    ans -= (0 + i - 1) * i // 2
    ans += 1
    ans %= MOD

print(ans)