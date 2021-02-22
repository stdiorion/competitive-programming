from random import randint

def stupid(a, b, c):
    return pow(a, pow(b, c), 10)

def solve(a, b, c):
    if a % 10 == 0:
        return 0
    else:
        return pow(a, pow(b, c, 10000), 10)

for _ in range(1000):
    a = randint(1, 100)
    b = randint(1, 100)
    c = randint(1, 100)

    ans1 = stupid(a, b, c)
    ans2 = solve(a, b, c)
    if ans1 != ans2:
        print(a, b, c)
        print(ans1, ans2)