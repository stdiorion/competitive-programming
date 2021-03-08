from collections import Counter
from itertools import combinations
n = int(input())
a = list(map(int, input().split()))

c = Counter(a)

ans = 0
for ai, aj in combinations(c, 2):
    ans += (ai - aj)** 2 * c[ai] * c[aj]

print(ans)