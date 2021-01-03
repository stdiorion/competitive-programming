from bisect import bisect_left, bisect_right
from collections import deque, Counter
from itertools import combinations, permutations
from math import gcd, sin, cos, tan, degrees, radians
import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 10 ** 9 + 7
INF = float("inf")

a, b = map(int, input().split())

def sdig(n):
    return n // 100 + (n % 100) // 10 + n % 10

print(max(sdig(a), sdig(b)))