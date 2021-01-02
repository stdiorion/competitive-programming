from itertools import combinations
import math

N = int(input())
sardines_pos = []
sardines_neg = []
sardines_zero = 0
a_zero = 0
b_zero = 0
discord = []

for i in range(N):
    a, b = map(int, input().split())

    if a == 0 and b == 0:
        sardines_zero += 1
    elif a == 0:
        a_zero += 1
    elif b == 0:
        b_zero += 1
    else:
        c = a / b

        if c > 0:
            sardines_pos.append((c, a, b))
        else:
            sardines_neg.append((c, a, b))


sardines_pos.sort()
sardines_neg.sort()

i_pos = 0
i_neg = 0

while i_pos < len(sardines_pos) and i_neg < len(sardines_neg):
    if sardines_pos[i_pos][2] * sardines_neg[i_neg][2] + sardines_pos[i_pos][1] * sardines_neg[i_neg][1] > 0:
        i_neg += 1
    elif sardines_pos[i_pos][2] * sardines_neg[i_neg][2] + sardines_pos[i_pos][1] * sardines_neg[i_neg][1] < 0:
        i_pos += 1
    else:
        cnt_pos = 0
        cnt_neg = 0
        for i in range(i_pos, len(sardines_pos)):
            if sardines_pos[i][0] == sardines_pos[i_pos][0]:
                cnt_pos += 1
            else:
                break
        for i in range(i_neg, len(sardines_neg)):
            if sardines_neg[i][0] == sardines_neg[i_neg][0]:
                cnt_neg += 1
            else:
                break
        discord.append([cnt_pos, cnt_neg])
        i_pos += cnt_pos
        i_neg += cnt_neg

def choice(n):
    return(2 ** n - 1)

ans = choice(N)

if sardines_zero > 0:
    discord.append([sardines_zero])
    ans += sardines_zero

if a_zero > 0 and b_zero > 0:
    discord.append([a_zero, b_zero])

if len(discord):
    for i in range(1, len(discord) + 1):
        for ds in combinations(discord, i):
            ds = sum(ds, [])
            ds_sum = 0
            ds_prod = 1
            for d in ds:
                ds_sum += d
                ds_prod *= choice(d)
            ans += ds_prod * (choice(N - ds_sum) + 1) * (-1) ** i

ans %= 1000000007

print(ans)