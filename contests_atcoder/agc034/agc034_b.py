s = input().replace("BC", "R")

charge = 0
ans = 0

for x in s:
    if x == "A":
        charge += 1
    elif x == "R":
        ans += charge
    else:
        charge = 0

print(ans)