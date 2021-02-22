x = int(input())
ans = 0
for i in range(1, 10000):
    if 100 * i <= x <= 105 * i:
        ans |= 1
print(ans)