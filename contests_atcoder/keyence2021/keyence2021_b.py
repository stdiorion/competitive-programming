from collections import Counter
import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 10 ** 9 + 7
INF = float("inf")

n, k = map(int, input().split())
a = list(map(int, input().split()))

c = Counter(a)

now = INF

ans = 0

for i in range(n + 1):
    if c[i] >= now:
        continue
    
    if i > 0:
        ans += max((now - c[i]) * i, 0)

    now = min(now, c[i], k)

print(ans)