x, y, a, b = map(int, input().split())

exp = 0

while x * (a - 1) < b:
    x *= a
    if x >= y:
        print(exp)
        exit()
    exp += 1

exp += (y - 1 - x) // b
print(exp)