from bisect import bisect_left, bisect_right
from collections import deque, Counter
from itertools import combinations, permutations
from math import gcd, sin, cos, tan, degrees, radians
import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 10 ** 9 + 7
INF = float("inf")

h, n = map(int, input().split())
spell = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[INF] * (h + 1) for _ in range(n)]

for i in range(n):
    for j in range(h + 1):
        if i > 0:
            dp[i][j] = min(dp[i][j], dp[i-1][j])
        if j >= spell[i][0]:
            dp[i][j] = min(dp[i][j], dp[i][j-spell[i][0]] + spell[i][1])
        elif j == 0:
            dp[i][j] = 0
        else:
            dp[i][j] = min(dp[i][j], spell[i][1])

print(dp[-1][-1])
