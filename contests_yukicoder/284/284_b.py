MOD = 10 ** 9 + 7
sa = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
n = input()

new_n = [9] * len(n)
flag = False
ans1 = 1

for i, d in enumerate(n):
    if d == "0":
        flag = True
        while i > 0:
            i -= 1
            if n[i] == "1":
                if i != 0:
                    new_n[i] = 9
                else:
                    ans1 = 0
            else:
                new_n[i] = int(n[i]) - 1
                break
    else:
        new_n[i] = 9 if flag else int(n[i])

n = new_n

for d in n:
    ans1 *= sa[d]
    ans1 %= MOD

ans2 = 45 * (pow(45, len(n) - 1, MOD) - 1) // 44

if int(n[0]) > 1:
    ans2 *= sa[int(n[0]) - 1] + 1

print((ans1 + ans2) % MOD)