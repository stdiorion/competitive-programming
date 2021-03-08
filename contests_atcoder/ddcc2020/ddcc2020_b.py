n = int(input())
a = list(map(int, input().split()))
sa = sum(a)

f = [0]
ans = 10 ** 20

for x in a:
    f.append(f[-1] + 2 * x)
    if f[-1] == sa:
        ans = 0
        break
    elif f[-1] > sa:
        ans = f[-1] - sa
        if len(f) > 1:
            ans = min(ans, sa - f[-2])
        break

print(ans)