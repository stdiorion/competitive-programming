s = input().rstrip()

letters = set(list(s))

ans = len(s)

for l in letters:
    frg = s.split(l)
    ans = min(ans, max([len(x) for x in frg]))

print(ans)