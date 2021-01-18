n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

time_a = sum(a)
bi = 0
time_b = 0

ans = 0

for i in range(n + 1):
    while time_a + time_b <= k and bi < len(b):
        ans = max(ans, n - i + bi)
        time_b += b[bi]
        bi += 1
    if time_a + time_b <= k and bi == len(b):
        ans = max(ans, n - i + bi)
        break
    if i < n:
        time_a -= a.pop()

print(ans)