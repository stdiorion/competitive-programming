from decimal import Decimal as d

n = int(input())
ans = 0
for i in range(1, n):
    ans += 1 / d(i)
print(ans * n)