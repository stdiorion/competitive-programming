from itertools import accumulate,chain,combinations,groupby,permutations,product
from collections import deque,Counter
from bisect import bisect_left,bisect_right
from math import gcd,sqrt,sin,cos,tan,degrees,radians
from fractions import Fraction
from decimal import Decimal
import sys
input = lambda: sys.stdin.readline().rstrip()
#from sys import setrecursionlimit
#setrecursionlimit(10**7)
MOD=10**9+7
INF=float('inf')

h, w = map(int, input().split())
ch, cw = map(lambda x: int(x) - 1, input().split())
dh, dw = map(lambda x: int(x) - 1, input().split())
field = [list(input()) for _ in range(h)]

warp_needed = [[INF] * w for _ in range(h)]

d = deque()
d.append((ch, cw))
warp_needed[ch][cw] = 0

d_afterwarp = deque()

def walk_from(p):
    return [(p[0] - 1, p[1]), (p[0], p[1] - 1), (p[0] + 1, p[1]), (p[0], p[1] + 1)]

def warp_from(p):
    ret = []
    for i in range(-2, 3):
        for j in range(-2, 3):
            if abs(i) + abs(j) > 1:
                ret.append((p[0] + i, p[1] + j))
    return ret

warp_count = 0

while True:
    if d:
        now = d.popleft()

        for dst in walk_from(now):
            if 0 <= dst[0] < h and 0 <= dst[1] < w and field[dst[0]][dst[1]] != "#" and warp_needed[dst[0]][dst[1]] > warp_count:
                warp_needed[dst[0]][dst[1]] = warp_count
                d.append(dst)

        for dst in warp_from(now):
            if 0 <= dst[0] < h and 0 <= dst[1] < w and field[dst[0]][dst[1]] != "#" and warp_needed[dst[0]][dst[1]] > warp_count + 1:
                warp_needed[dst[0]][dst[1]] = warp_count + 1
                d_afterwarp.append(dst)
    
    elif d_afterwarp:
        d = d_afterwarp
        d_afterwarp = deque()
        warp_count += 1
    
    else:
        break

print(warp_needed[dh][dw] if warp_needed[dh][dw] != INF else -1)