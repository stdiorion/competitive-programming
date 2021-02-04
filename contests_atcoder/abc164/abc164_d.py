from collections import Counter

MOD = 2019

s = input()

partial = [0]

for i, l in enumerate(reversed(s)):
    partial.append((partial[-1] + int(l) * pow(10, i, MOD)) % MOD)

c = Counter(partial)

ans = 0

for v in c.values():
    ans += v * (v - 1) // 2

print(ans)