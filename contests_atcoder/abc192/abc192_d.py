x = input()
m = int(input())

d = 0
for y in x:
    d = max(d, int(y))

def base(x, n):
    res = 0
    for i, y in enumerate(x[::-1]):
        res += int(y) * n ** i
    return res

def okay(n):
    return base(x, n) <= m

def meguru_bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if okay(mid):
            ok = mid
        else:
            ng = mid
    return ok

if len(x) == 1:
    if int(x) > m:
        print(0)
    else:
        print(1)
else:
    if not okay(d + 1):
        print(0)
    else:
        print(meguru_bisect(m + 1, d + 1) - d)