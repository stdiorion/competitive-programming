from math import gcd
from itertools import combinations

n = int(input())
a = list(map(int, input().split()))

ans = set()
m = min(a)
ans.add(m)

for x, y in combinations(a, 2):
    g = gcd(x, y)
    if g < m and g not in ans:
        ans.add(g)

print(len(ans))