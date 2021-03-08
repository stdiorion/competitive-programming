n, m = map(int, input().split())
shops = [tuple(map(int, input().split())) for _ in range(n)]
shops.sort(key=lambda x: x[0])
ans = 0
for a, b in shops:
    if m <= b:
        ans += a * m
        break
    else:
        ans += a * b
        m -= b

print(ans)