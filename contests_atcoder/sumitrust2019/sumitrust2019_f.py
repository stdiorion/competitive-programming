t1, t2 = map(int, input().split())
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

first = (a1 - b1) * t1
second = (a2 - b2) * t2

if first < 0:
    first *= -1
    second *= -1

whole = first + second

if whole == 0:
    print("infinity")
elif whole > 0:
    print(0)
else:
    ans = (first // -whole) * 2 + 1
    if first % -whole == 0:
        ans -= 1
    print(ans)