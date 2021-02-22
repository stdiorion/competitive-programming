from random import randint

def solve(x, m):
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
            return 0
        else:
            return 1
    else:
        if not okay(d + 1):
            return 0
        else:
            return meguru_bisect(m, d + 1) - d

def stupi(x, m):
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
    
    ans = set()

    for i in range(d + 1, m + 2):
        if okay(i):
            ans.add(base(x, i))
    
    return len(ans)


for _ in range(10000):
    x = str(randint(1, 10000))
    m = randint(1, 100)

    ans1 = solve(x, m)
    ans2 = stupi(x, m)
    if ans1 != ans2:
        print(x, m)
        print(ans1, ans2)