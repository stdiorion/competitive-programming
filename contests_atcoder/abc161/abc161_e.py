from random import randint

n, k, c = map(int, input().split())
s = input()

cur = 0
workday = 0
worked_left = set()

while cur < n:
    if s[cur] == "o":
        workday += 1
        worked_left.add(cur + 1)
        cur += c + 1
    else:
        cur += 1

    if workday == k:
        break

else:
    exit()

cur = n - 1
workday = 0
worked_right = set()

while cur >= 0:
    if s[cur] == "o":
        workday += 1
        worked_right.add(cur + 1)
        cur -= c + 1
    else:
        cur -= 1

    if workday == k:
        break

ans = worked_left & worked_right


for i in range(10):
    cur = 0
    workday = 0
    worked_another = set()

    while cur < n:
        if s[cur] == "o":
            if randint(0, 2): 
                workday += 1
                worked_another.add(cur + 1)
                cur += c + 1
            else:
                cur += 1
        else:
            cur += 1

        if workday == k:
            ans &= worked_another
            break

print(*sorted(ans), sep="\n")