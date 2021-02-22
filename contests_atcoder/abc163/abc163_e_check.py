from itertools import permutations
from random import randint


def solver(n, a):
    a_i = [(x, i) for i, x in enumerate(a)]

    ans = 0

    for perm in permutations(a_i, n):
        score = 0
        for i, (x, i_be) in enumerate(perm):
            score += x * abs(i - i_be)
        if ans < score:
            ans = score
            ans_perm = perm

    return ans

def delve2(n, a):
    a_i = [(x, i, i) for i, x in enumerate(a)]
    a_i.sort(reverse=True)

    upper = n
    lower = 0

    ans = 0

    for cnt, (x, i, real_i) in enumerate(a_i):
        del a[real_i]
        rscore = sum(a[real_i:]) + x * (upper - i - 1)
        lscore = sum(a[:real_i]) + x * (i - lower)
        if rscore < lscore:
            ans += x * (i - lower)
            lower += 1
        else:
            ans += x * (upper - i - 1)
            upper -= 1

        for cnt2, (x2, i2, real_i2) in enumerate(a_i):
            if i < i2:
                a_i[cnt2] = (x2, i2, real_i2 - 1)
    
    return ans

for i in range(10000):
    n = randint(2, 8)
    a = [randint(1, 5) for _ in range(n)]
    ans = solver(n, a[:])
    ans2 = delve2(n, a[:])
    if ans != ans2:
        print(n)
        print(*a)
        print(ans, ans2)
        exit()