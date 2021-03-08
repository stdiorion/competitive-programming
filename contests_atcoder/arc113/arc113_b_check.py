from random import randint

def stupid(a, b, c):
    return pow(a, pow(b, c), 10)

def solve(a, b, c):
    if a % 10 == 0:
        return 0
    else:
        return pow(a, pow(b, c, 10000), 10)

def solve2(a, b, c):
    b %= 4

    if (b == 2):
        if (c == 1): b = 2
        else: b = 0
    elif (c & 1): b %= 4
    else: b = (b % 4) * (b % 4) % 4

    if (b == 0): b = 4

    a %= 10
    res = 1
    for i in range(b): res = res * a % 10

    return res

for _ in range(1000):
    a = randint(1, 100)
    b = randint(1, 100)
    c = randint(1, 100)

    ans1 = solve2(a, b, c)
    ans2 = stupid(a, b, c)
    if ans1 != ans2:
        print(a, b, c)
        print(ans1, ans2)