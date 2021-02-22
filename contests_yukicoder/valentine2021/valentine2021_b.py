MOD = 998244353
n = int(input())

numbers = list(range(2, n + 1))
primes = []

while numbers[0] * numbers[0] <= n:
    now = numbers[0]
    primes.append(now)
    numbers = [x for x in numbers if x % now]

primes += numbers

ans = 1

for p in primes[:-1]:
    for i in range(1, 30):
        if p ** i > n:
            ans = ans * p ** (i - 1) % MOD
            break

print(ans)