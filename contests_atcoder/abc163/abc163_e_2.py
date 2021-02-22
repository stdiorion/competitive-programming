n = int(input())
a = list(map(int, input().split()))

a_i = [(x, i, i) for i, x in enumerate(a)]
a_i.sort(reverse=True, key=lambda x: x[0])

upper = n
lower = 0

ans = 0

for cnt, (x, i, real_i) in enumerate(a_i):
    del a[real_i]
    rscore = sum(a[real_i:]) + x * (upper - i - 1)
    lscore = sum(a[:real_i]) + x * (i - lower)
    if rscore < lscore:
        ans += x * (i - lower)
        lower += 1
    else:
        ans += x * (upper - i - 1)
        upper -= 1

    for cnt2, (x2, i2, real_i2) in enumerate(a_i):
        if i < i2:
            a_i[cnt2] = (x2, i2, real_i2 - 1)

print(ans)