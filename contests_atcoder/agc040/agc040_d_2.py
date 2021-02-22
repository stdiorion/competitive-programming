from itertools import accumulate
from fractions import Fraction

n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]

snuke = sum(x[0] for x in times)
rng = [x[1] for x in times]
rng.sort(reverse=True)

srng = [0] + list(accumulate(rng))

print(srng)
print(snuke)