import sys
from operator import itemgetter
input = sys.stdin.readline

n = int(input())
problems = [tuple(map(int, input().split())) for _ in range(n)]

problems_l = sorted(problems, key=itemgetter(0))
problems_r = sorted(problems, key=itemgetter(1))

ans = 0

for l, r in problems:
    if l == problems_l[-1][0]:
        max_l = problems_l[-2][0]
    else:
        max_l = problems_l[-1][0]
    if r == problems_r[0][1]:
        min_r = problems_r[1][1]
    else:
        min_r = problems_r[0][1]
    ans = max(ans, r - l + 1 + max(0, min_r - max_l + 1))

range_1 = []
lb, rb = 1, 1e9
for l, r in problems_l[:-1]:
    if lb < l:
        lb = l
    if r < rb:
        rb = r
    range_1.append(rb - lb + 1)

range_2 = []
lb, rb = 1, 1e9
for l, r in problems_l[:0:-1]:
    if lb < l:
        lb = l
    if r < rb:
        rb = r
    range_2.append(rb - lb + 1)

for x, y in zip(range_1, range_2[::-1]):
    ans = max(ans, x + y)

print(ans)