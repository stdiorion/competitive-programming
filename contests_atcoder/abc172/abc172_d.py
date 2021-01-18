n = int(input())
ans = 0
for i in range(1, n + 1):
    c = n // i
    ans += i * c * (c + 1) // 2
print(ans)