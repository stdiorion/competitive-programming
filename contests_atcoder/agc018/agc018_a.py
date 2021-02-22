import math
from functools import reduce
def gcd(*n): return reduce(math.gcd, n)

n, k = map(int, input().split())
a = list(map(int, input().split()))
if max(a) < k or k % gcd(*a):
    print("IMPOSSIBLE")
else:
    print("POSSIBLE")