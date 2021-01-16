n = int(input())
s = input()

i1 = 0
i2 = n - 1

ans = 0

while i1 < i2:
    if s[i1] == "W" and s[i2] == "R":
        i1 += 1
        i2 -= 1
        ans += 1
    if s[i1] == "R":
        i1 += 1
    if s[i2] == "W":
        i2 -= 1

print(ans)