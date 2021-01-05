from bisect import bisect_left, bisect_right
from collections import deque, Counter
from itertools import combinations, permutations
from math import gcd, sin, cos, tan, degrees, radians
import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 10 ** 9 + 7
INF = float("inf")

n, d, a = map(int, input().split())
monsters = [tuple(map(int, input().split())) for _ in range(n)]

monsters.sort()

now = 0
ans = 0
bomb = deque()

for m in monsters:
    x = m[0]
    attack_count = -(-m[1] // a)

    while len(bomb) and bomb[0][0] < x:
        b = bomb.popleft()
        now -= b[1]

    if attack_count > now:
        ans += attack_count - now
        bomb.append((x + 2 * d, attack_count - now))
        now = attack_count

print(ans)