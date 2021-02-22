s = input()

mountains = []
prev = 0
for i in range(len(s) - 1):
    if s[i:i + 2] == "><":
        mountains.append(s[prev:i + 1])
        prev = i + 1
mountains.append(s[prev:])

ans = 0

for m in mountains:
    lt = m.count("<")
    gt = m.count(">")
    if lt > gt: lt, gt = gt, lt
    ans += (1 + gt) * gt // 2 + (1 + lt - 1) * (lt - 1) // 2

print(ans)