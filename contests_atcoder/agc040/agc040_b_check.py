from random import randint
from operator import itemgetter


def stupid(n, problems):
    ans = 0

    for bit in range(1, (1 << n) - 1):
        l1, l2 = 1, 1
        r1, r2 = 1e9, 1e9

        for i, (l, r) in enumerate(problems):
            if (bit >> i) & 1:
                l1 = max(l1, l)
                r1 = min(r1, r)
            else:
                l2 = max(l2, l)
                r2 = min(r2, r)
        score1 = max(0, r1 - l1 + 1)
        score2 = max(0, r2 - l2 + 1)
        ans = max(ans, score1 + score2)

    return ans

def solve(n, problems):
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
    
    return ans

for _ in range(100):
    n = randint(2, 16)
    problems = [(randint(1, 10), randint(1, 10)) for _ in range(n)]
    problems = [(l, r) if l < r else (r, l) for l, r in problems]
    ans1 = stupid(n, problems)
    ans2 = solve(n, problems)
    if ans1 != ans2:
        print(n)
        print(*problems, sep="\n")
        print(ans1, ans2)
        exit()