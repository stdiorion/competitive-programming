from collections import Counter
from random import randint, choice

def solve(n, p, s):
    s = [int(x) for x in s]
    a = [0]
    for i, x in enumerate(reversed(s)):
        a.append((a[-1] + x * pow(10, i, p)) % p)

    c = Counter(a)

    ans = 0

    for x in c.values():
        ans += x * (x - 1) // 2

    return ans

def ans(n, p, s):
    ans = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            if int(s[i:j]) % p == 0:
                ans += 1
    return ans

for _ in range(100):
    n = randint(1, 10)
    p = choice([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293])
    s = "".join(str(randint(0, 9)) for _ in range(n))
    ans1 = solve(n, p, s)
    ans2 = ans(n, p, s)

    if ans1 != ans2:
        print(n, p)
        print(s)
        print(ans1, ans2)
        print()