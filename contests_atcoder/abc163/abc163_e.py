n = int(input())
a = list(map(int, input().split()))

a_i = [(x, i) for i, x in enumerate(a)]
a_i.sort(reverse=True)

upper = n - 1
lower = 0

ans = 0

for x, i in a_i:
    rdist = abs(upper - i)
    ldist = abs(lower - i)
    if rdist < ldist:
        ans += x * abs(lower - i)
        lower += 1
    elif rdist > ldist:
        ans += x * abs(upper - i)
        upper -= 1
    else:
        ans += x * abs(upper - i)
        upper -= 1

print(ans)