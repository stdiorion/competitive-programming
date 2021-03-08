import sys
sys.setrecursionlimit(10 ** 7)
n = input()
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

print((solve(n) + base) % MOD)