from random import randint as ri

for t in range(100):
    n, m, k = ri(1, 5), ri(1, 5), ri(1, 300)
    a = [ri(1, 100) for _ in range(n)]
    b = [ri(1, 100) for _ in range(m)]

    A = a[:]

    ans_ = 0
    for i in range(n + 1):
        for j in range(m + 1):
            if sum(a[:i]) + sum(b[:j]) <= k:
                ans_ = max(ans_, i + j)

    time_a = sum(a)
    bi = 0
    time_b = 0

    ans = 0

    for i in range(n + 1):
        while time_a + time_b <= k and bi < len(b):
            ans = max(ans, n - i + bi)
            time_b += b[bi]
            bi += 1
        if bi == len(b):
            ans = max(ans, n - i + bi)
            break
        if i < n:
            time_a -= a.pop()

    if ans != ans_:
        print(n, m, k)
        print(*A)
        print(*b)
        print(ans, ans_)