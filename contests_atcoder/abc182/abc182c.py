n = list(input().rstrip())

d = [0, 0, 0]

for dig in n:
    dig = int(dig) % 3
    d[dig] += 1

s = (d[1] + 2 * d[2]) % 3

if s == 0:
    print(0)
elif s == 1:
    if d[1] > 0 and d != [0, 1, 0]:
        print(1)
    elif d[2] > 1 and d != [0, 0, 2]:
        print(2)
    else:
        print(-1)
else:
    if d[2] > 0 and d != [0, 0, 1]:
        print(1)
    elif d[1] > 1 and d != [0, 2, 0]:
        print(2)
    else:
        print(-1)