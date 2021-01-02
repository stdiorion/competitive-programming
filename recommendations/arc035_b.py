MOD = 10 ** 9 + 7

n = int(input())
times = [int(input()) for _ in range(n)]

fct = [1] * (n + 1)
for i in range(1, n + 1):
    fct[i] = fct[i - 1] * i % MOD

times.sort()

ans = 0
count = [1]

for i, t in enumerate(times):
    ans += t * (n - i)
    if i > 0:  
        if t == t_prev:
            count[-1] += 1
        else:
            count.append(1)
    t_prev = t

print(ans)

ans2 = 1

for c in count:
    ans2 *= fct[c]
    ans2 %= MOD

print(ans2)