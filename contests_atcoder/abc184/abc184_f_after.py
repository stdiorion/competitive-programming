n, t = map(int, input().split())
a = list(map(int, input().split()))

a_lower = a[:20]
a_upper = a[20:]

t_lo = []
t_up = []

for i in range(1 << len(a_lower)):
    needed_time = 0
    for j in range(len(a_lower)):
        if (i >> j) % 2:
            needed_time += a_lower[j]
    t_lo.append(needed_time)

for i in range(1 << len(a_upper)):
    needed_time = 0
    for j in range(len(a_upper)):
        if (i >> j) % 2:
            needed_time += a_upper[j]
    t_up.append(needed_time)

t_lo.sort()
t_up.sort(reverse=True)

i = 0
ans = 0

for basetime in t_lo:
    while basetime + t_up[i] > t:
        i += 1
        if i == len(t_up):
            break
    else:
        ans = max(ans, basetime + t_up[i])
        continue
    break

print(ans)