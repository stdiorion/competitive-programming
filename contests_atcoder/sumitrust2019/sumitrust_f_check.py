from random import randint

def solve(t1, t2, a1, a2, b1, b2):
    first = (a1 - b1) * t1
    second = (a2 - b2) * t2

    if first < 0:
        first *= -1
        second *= -1

    whole = first + second

    if whole == 0:
        return "infinity"
    elif whole > 0:
        return 0
    else:
        ans = (first // -whole) * 2 + 1
        return ans

def ans(t1, t2, a1, a2, b1, b2):
    first = (a1 - b1) * t1
    second = (a2 - b2) * t2

    come = 0

    while True:
        if come 

for _ in range(100):
    t1, t2 = randint(1, 100), randint(1, 100)
    a1, a2 = randint(1, 100), randint(1, 100)
    b1, b2 = randint(1, 100), randint(1, 100)

    if a1 == b1 or a2 == b2:
        continue

    ans1 = solve(t1, t2, a1, a2, b1, b2)
    ans2 = ans(t1, t2, a1, a2, b1, b2)

    if ans1 != ans2:
        print(t1, t2)
        print(a1, a2)
        print(b1, b2)
        print(f"Out: {ans1} Correct: {ans2} ")