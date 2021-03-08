def popcnt(x):
    return bin(x).count("1")

def solve(u, v):
    from itertools import zip_longest
    if u > v:
        return 0
    elif u == v:
        return 1
    else:
        u = bin(u)[2:][::-1]
        v = bin(v)[2:][::-1]
        battle = 0
        for x, y in zip_longest(u, v):
            battle += int(x == "1") - int(y == "1")
            if battle < 0:
                return 0
                break
        else:
            return 1

def resolve(u, v):
    from collections import deque
    d = deque([u])
    while d:
        now = d.popleft()
        if now == v:
            return 1
        for i in range(1, now + 1):
            if now + i <= v and i & now == i:
                d.append(now + i)
    return 0

for u in range(1, 100):
    for v in range(1, 100):
        ans1 = solve(u, v)
        ans2 = resolve(u, v)
        if ans1 != ans2:
            print(u, v, ans1, ans2)