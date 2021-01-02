h, w = map(int, input().split())

a = []

for _ in range(h):
    a += list(map(int, input().split()))

m = min(a)

ans = 0

for i in a:
    ans += i - m

print(ans)