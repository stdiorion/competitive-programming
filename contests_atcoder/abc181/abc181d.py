from itertools import permutations

s_raw = list(input().rstrip())
s = []

dig_cnt = [0] * 10

for dig in s_raw:
    if dig_cnt[int(dig)] >= 3:
        continue
    dig_cnt[int(dig)] += 1
    s.append(dig)

if len(s) >= 3:
    for k in permutations(s, 3):
        num = int("".join(k))
        if num % 8 == 0:
            print("Yes")
            exit()
elif len(s) == 2:
    if int("".join(s)) % 8 == 0 or int("".join(reversed(s))) % 8 == 0:
        print("Yes")
        exit()
elif s == ["8"]:
    print("Yes")
    exit()


print("No")