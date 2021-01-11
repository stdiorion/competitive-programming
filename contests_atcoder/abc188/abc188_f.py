from bisect import bisect_left, bisect_right
from collections import deque, Counter, defaultdict
from itertools import combinations, permutations
from math import gcd, sin, cos, tan, degrees, radians
import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 10 ** 9 + 7
INF = float("inf")

x, y = map(int, input().split())

scores = defaultdict(int)

def score(n):
    if scores[n] != 0:
        return scores[n]
    ret = INF
    for i in range(70):
        ret = min(ret, abs((n << i) - y) + i)
        if y < (n << i):
            scores[n] = ret
            return ret

if x == y:
    print(0)
elif x > y:
    print(x - y)
else:
    count = 0

    while True:
        if x == y:
            print(count)
            exit()
        if x == 1:
            mul = score(x)
            add = score(x+1)
            choice = min(mul, add)
        else:
            mul = score(x)
            add = score(x+1)
            sub = score(x-1)
            choice = min(mul, add, sub)

        if choice == mul:
            x *= 2
        elif choice == add:
            x += 1
        elif choice == sub:
            x -= 1

        count += 1

exit()
for i in range(100):

    x, y = 1, i

    if x == y:
        print(0)
    elif x > y:
        print(x - y)
    else:
        d = deque()
        d.append(x)

        dist = defaultdict(int)

        while True:
            now = d.popleft()
            if now == y:
                print(f"{dist[now]},", end="")
                break
            if dist[now-1] == 0:
                dist[now-1] = dist[now] + 1
                d.append(now-1)
            if dist[now+1] == 0:
                dist[now+1] = dist[now] + 1
                d.append(now+1)
            if dist[now*2] == 0:
                dist[now*2] = dist[now] + 1
                d.append(now*2)