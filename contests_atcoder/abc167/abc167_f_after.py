n = int(input())
plus = []
minus = []
for i in range(n):
    s = input()
    left_cnt = s.count("(")
    right_cnt = s.count(")")
    if left_cnt >= right_cnt:
        plus.append((s, right_cnt))
    else:
        minus.append((s[::-1], left_cnt))

plus.sort(key=lambda x: x[1])
minus.sort(key=lambda x: x[1])

hp = 0

for x, y in plus:
    for l in x:
        hp += 1 if l == "(" else -1
        if hp < 0:
            print("No")
            exit()
hm = 0

for x, y in minus:
    for l in x:
        hm += 1 if l == ")" else -1
        if hm < 0:
            print("No")
            exit()

if hp - hm:
    print("No")
else:
    print("Yes")