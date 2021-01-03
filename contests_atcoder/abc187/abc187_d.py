from bisect import bisect_left, bisect_right
from collections import deque, Counter
from itertools import combinations, permutations
from math import gcd, sin, cos, tan, degrees, radians
import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 10 ** 9 + 7
INF = float("inf")

n = int(input())
cities = [list(map(int, input().split())) for _ in range(n)]

aoki_sum = 0
gain = []

for city in cities:
    aoki = city[0]
    tak = city[1]
    gain.append(aoki * 2 + tak)
    aoki_sum += aoki

gain.sort(reverse=True)

rep = 0

for i, g in enumerate(gain):
    rep += g
    if rep > aoki_sum:
        print(i + 1)
        break