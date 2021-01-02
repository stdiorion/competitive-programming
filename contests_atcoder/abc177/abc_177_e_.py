import math
from functools import reduce

def gcd_list(numbers):
    return reduce(math.gcd, numbers)

n = int(input())
a = list(map(int, input().split()))

def set_check():
    if gcd_list(a) == 1:
        print("setwise coprime")
    else:
        print("not coprime")

indexed = [False] * (10 ** 6 + 1)

for x in a:
    if x == 1:
        continue
    if not indexed[x]:
        indexed[x] = True
    else:
        set_check()
        exit()
else:
    limit = 10 ** 6

    for k in range(2, limit):
        exists = False
        for i in range(k, limit + 1, k):
            if indexed[i]:
                if exists:
                    set_check()
                    exit()
                else:
                    exists = True

print("pairwise coprime")