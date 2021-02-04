n, m, k = map(int, input().split())
a = list(map(int, input().split()))

streak = 1
prev = -1

for x in a:
    if x - 1 == prev:
        streak += 1
        if streak == m:
            print(-1)
            exit()
    else:
        streak = 1
    prev = x

cdp = [0] * (n + m + 1)
xdp = [0] * (n + m + 1)

scdp = 0
sxdp = 0

for i in range(n, 0, -1):
    if i - 1 in a:
        cdp[i - 1] = 0
        xdp[i - 1] = 1
    else:
        cdp[i - 1] = scdp / m + 1
        xdp[i - 1] = sxdp / m
    scdp = scdp + cdp[i - 1] - cdp[i + m - 1]
    sxdp = sxdp + xdp[i - 1] - xdp[i + m - 1]

if xdp[0] == 1:
    ans = -1
else:
    ans = cdp[0] / (1 - xdp[0])
print(ans)