from itertools import accumulate
from fractions import Fraction

n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]

snuke = sum(x[0] for x in times)
rng = [x[1] for x in times]
rng.sort(reverse=True)

srng = [0] + list(accumulate(rng))

def snuke_win(m):
    inte = int(m)
    frac = m - inte
    return srng[inte] + rng[inte] * frac >= snuke

def meguru_bisect(lose, win):
    while abs(win - lose) > 1:
        m = (lose + win) // 2
        if snuke_win(m):
            win = m
        else:
            lose = m
    return win

draw_point = meguru_bisect(Fraction(0), Fraction(n))

print()