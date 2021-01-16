import sys
input = sys.stdin.buffer.readline
n, Q = map(int, input().split())
c = tuple(map(int, input().split()))

queries = [tuple(map(int, input().split() + [i])) for i in range(Q)]

BIT = [0] * (n + 1)

def bitsum(i):
    r = 0
    while i >= 1:
        r += BIT[i]
        i -= i & -i
    return r

def bitadd(i, x, n):
    while i <= n:
        BIT[i] += x
        i += i & -i

queries.sort(key=lambda x: x[0])

p_next = [-1] * (n + 1)
c_now = [-1] * (n + 1)

for i, x in enumerate(reversed(c)):
    p_next[n - i] = c_now[x]
    c_now[x] = n - i

for pos in c_now:
    if 1 <= pos <= n:
        bitadd(pos, 1, n)

l = 1

ans = [[] for _ in range(Q)]

for q in queries:
    left, right, id = q
    for i in range(l, left):
        if p_next[i] != -1:
            bitadd(p_next[i], 1, n)
    l = left
    ans[id] = bitsum(right) - bitsum(left - 1)

print(*ans, sep="\n")