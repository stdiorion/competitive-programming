n = int(input())
s = input()

ans = 0

for p in range(1000):
    pin = str(p).zfill(3)
    idx = 0
    for x in s:
        if x == pin[idx]:
            idx += 1
            if idx == 3:
                ans += 1
                break

print(ans)