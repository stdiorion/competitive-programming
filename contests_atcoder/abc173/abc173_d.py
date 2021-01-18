from bisect import bisect_left, bisect_right
from collections import deque, Counter
from itertools import combinations, permutations
from math import gcd, sin, cos, tan, degrees, radians
import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 10 ** 9 + 7
INF = float("inf")

n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

ans = -a[0]

for i in range(n):
    ans += a[i // 2]

print(ans)