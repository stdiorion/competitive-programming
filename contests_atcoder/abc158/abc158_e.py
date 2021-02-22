from collections import Counter
n, p = map(int, input().split())
s = [int(x) for x in input()]

if p == 2:
    ans = 0
    for i, x in enumerate(s, start=1):
        if x % 2 == 0:
            ans += i
    print(ans)

elif p == 5:
    ans = 0
    for i, x in enumerate(s, start=1):
        if x % 5 == 0:
            ans += i
    print(ans)

else:
    a = [0]
    for i, x in enumerate(reversed(s)):
        a.append((a[-1] + x * pow(10, i, p)) % p)

    c = Counter(a)

    ans = 0

    for x in c.values():
        ans += x * (x - 1) // 2

    print(ans)