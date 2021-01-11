def digitsum(num, p=10):
    dsum = 0
    while num > 0:
        num, d = divmod(num, p)
        dsum += d
    return dsum

n, a, b = map(int, input().split())

ans = 0

for i in range(1, n + 1):
    if a <= digitsum(i) <= b:
        ans += i

print(ans)