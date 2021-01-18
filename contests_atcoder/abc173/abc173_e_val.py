MOD = 10 ** 9 + 7
from itertools import combinations
from random import randint
import math

def modprod(l):
    ret = 1
    for x in l:
        ret *= x
        ret %= MOD
    return ret

for t in range(1000):
    n = randint(1, 20)
    k = randint(1, n)
    a = [randint(-10, 10) for _ in range(n)]

    ans_ = -float("inf")
    for comb in combinations(a, k):
        ans_ = max(ans_, math.prod(comb))

    plus = [x for x in a if x > 0]
    minus = [x for x in a if x < 0]
    zero = a.count(0)

    plus.sort()
    minus.sort()

    ans = 1


    if len(a) == k:
        ans = math.prod(a)
    elif len(plus) + len(minus) < k:
        ans = 0
    elif len(plus) + len(minus) == k:
        ans = 0 if len(minus) % 2 else math.prod(plus + minus)
    else: # len(plus) + len(minus) > k
        if len(plus) == 0:
            if k % 2:
                if zero:
                    ans = 0
                else:
                    ans = math.prod(minus[-k:])
            else:
                ans = math.prod(minus[:k])
        else: # len(plus) > 0
            if k % 2:
                ans = plus.pop()
            pairprod = [plus[-1-2*i] * plus[-2-2*i] for i in range(len(plus) // 2)]
            pairprod += [minus[2*i] * minus[2*i+1] for i in range(len(minus) // 2)]
            pairprod.sort(reverse=True)
            ans *= math.prod(pairprod[:k // 2])
            # ans %= MOD

    if ans != ans_:
        print(n, k)
        a.sort()
        print(*a)
        print(f"true: {ans_} out: {ans}")