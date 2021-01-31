from collections import defaultdict
import heapq
from bisect import insort_left, bisect_left

n, Q = map(int, input().split())
infants = [list(map(int, input().split())) for _ in range(n)]
queries = [list(map(int, input().split())) for _ in range(Q)]

gd = defaultdict(list)

for i, ift in enumerate(infants):
    insort_left(gd[ift[1]], (ift[0], i + 1))

highest = []

for key in gd:
    insort_left(highest, (gd[key][-1][0], key))

rating = [-1] + [x[0] for x in infants]
belongs = [-1] + [x[1] for x in infants]

for q in queries:
    ift, to = q
    frm = belongs[ift]
    belongs[ift] = to


    del gd[frm][bisect_left(gd[frm], (rating[ift], ift))]

    hi_pos = bisect_left(highest, (rating[ift], frm))
    if highest[hi_pos] == (rating[ift], frm):
        del highest[hi_pos]
        if len(gd[frm]):
            insort_left(highest, (gd[frm][-1][0], frm))


    new_pos = bisect_left(gd[to], (rating[ift], ift))
    if len(gd[to]) == 0:
        insort_left(highest, (rating[ift], to))
    elif new_pos == len(gd[to]):
        hi_pos = bisect_left(highest, (gd[to][-1][0], to))
        del highest[hi_pos]
        insort_left(highest, (rating[ift], to))
    insort_left(gd[to], (rating[ift], ift))

    print(highest[0][0])