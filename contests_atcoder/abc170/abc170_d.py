n = int(input())
a = list(map(int, input().split()))

ac = [0] * 1000001
for x in a:
    ac[x] += 1

a.sort()

for x in a:
    if ac[x] <= 0:
        continue
    elif ac[x] > 1:
        ac[x] = 0
        
    i = 2
    while x * i <= a[-1]:
        ac[x * i] = 0
        i += 1

print(sum(ac))