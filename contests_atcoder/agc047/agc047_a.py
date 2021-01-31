from decimal import Decimal
from collections import defaultdict
from itertools import combinations
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = [int(Decimal(input()) * 10 ** 9) for _ in range(n)]

twofive = defaultdict(int)

for x in a:
    p = 0
    while x % 2 == 0 and p < 18:
        x //= 2
        p += 1
    
    q = 0
    while x % 5 == 0 and q < 18:
        x //= 5
        q += 1
    
    twofive[(p, q)] += 1

ans = 0

done = set()

for p1 in range(19):
    for q1 in range(19):
        for p2 in range(19):
            for q2 in range(19):
                if (p1, q1, p2, q2) in done: continue
                if p1 + p2 >= 18 and q1 + q2 >= 18:
                    if (p1, q1) == (p2, q2) and twofive[(p1, q1)]:
                        ans += twofive[(p1, q1)] * (twofive[(p1, q1)] - 1) // 2
                    elif twofive[(p1, q1)] and twofive[(p2, q2)]:
                        ans += twofive[(p1, q1)] * twofive[(p2, q2)]
                done.add((p2, q2, p1, q1))

print(ans)