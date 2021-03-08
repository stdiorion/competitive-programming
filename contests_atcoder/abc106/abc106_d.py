"""
include or included な区間の個数を数えるプログラムになっている
"""

import sys
input = sys.stdin.readline
from itertools import accumulate

n, m, Q = map(int, input().split())
trains = [tuple(map(int, input().split())) for _ in range(m)]
queries = [tuple(map(int, input().split())) for _ in range(Q)]

# i以上の区間に完全に含まれる列車の本数
whole = [0] * (n + 1)
# i以上の区間に一部でも含まれる列車の本数
partial = [0] * (n + 1)

for l, r in trains:
    whole[0] += 1
    whole[l] -= 1
    partial[0] += 1
    partial[r] -= 1

whole = list(accumulate(whole))
partial = list(accumulate(partial))

for p, q in queries:
    print(whole[p - 1] - partial[q])