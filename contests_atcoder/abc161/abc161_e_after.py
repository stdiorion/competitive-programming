n, k, c = map(int, input().split())
s = input()

cur = 1
lbound = []

while cur <= n:
    if s[cur-1] == "o":
        lbound.append(cur)
        cur += c + 1
    else:
        cur += 1
    
    if len(lbound) == k:
        break
else:
    exit()

cur = n
rbound = []

while len(rbound) < k:
    if s[cur-1] == "o":
        rbound.append(cur)
        cur -= c + 1
    else:
        cur -= 1

for l, r in zip(lbound, reversed(rbound)):
    if l == r: print(l)