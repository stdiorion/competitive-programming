import math
from functools import reduce

def gcd_list(numbers):
    return reduce(math.gcd, numbers)

n = int(input())
a = list(map(int, input().split()))

prod_a = a[0]

for i in range(1, len(a)):
    if math.gcd(prod_a, a[i]) != 1:
        break
    prod_a *= a[i]
else:
    print("pairwise coprime")
    exit()

if gcd_list(a) == 1:
    print("setwise coprime")
else:
    print("not coprime")