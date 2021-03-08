from random import randint
MOD = 10 ** 9 + 7
sa = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]

def solver(n):
    import sys
    sys.setrecursionlimit(10 ** 7)
    MOD = 10 ** 9 + 7
    sa = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]

    new_n = [9] * len(n)
    flag = False
    dig1 = True

    for i, d in enumerate(n):
        if flag: continue
        if d == "0":
            flag = True
            while i > 0:
                i -= 1
                if n[i] == "1":
                    if i != 0:
                        new_n[i] = 9
                    else:
                        dig1 = False
                else:
                    new_n[i] = int(n[i]) - 1
                    break
        else:
            new_n[i] = int(n[i])

    n = new_n[not dig1:]

    def solve(n):
        if len(n) == 1: return sa[int(n[0])]
        return (int(n[0]) * solve(n[1:]) % MOD + sa[int(n[0]) - 1] * pow(sa[9], len(n) - 1, MOD) % MOD) % MOD

    base = 45 * (pow(45, len(n) - 1, MOD) - 1) // 44

    return ((solve(n) + base) % MOD)

def digit_sum(x, p=10):
    ret = 1
    while x > 0:
        x, d = divmod(x, p)
        ret *= d
    return ret

def answ(n):
    ans = 0
    for N in range(1, int(n) + 1):
        ans += digit_sum(N)
    return ans % MOD

for n in range(1, 10):
    n = str(randint(100000, 200000))
    ans1 = solver(n)
    ans2 = answ(n)
    if ans1 != ans2:
        print(n)
        print(ans1, ans2)