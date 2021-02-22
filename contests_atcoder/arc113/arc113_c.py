from collections import defaultdict

s = input()[::-1]

prev = ""
prevpos = 0

charcnt = defaultdict(int)

ans = 0

for i, (x, y) in enumerate(zip(s, s[1:])):
    if x == y:
        if x == prev:
            ans += i - charcnt[x] - prevpos
        else:
            ans += i - charcnt[x]
        prev = x
        prevpos = i + 1
        charcnt = defaultdict(int)
    else:
        charcnt[x] += 1
        if i == 0: charcnt[x] += 1

print(ans)