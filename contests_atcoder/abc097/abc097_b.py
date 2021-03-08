x = int(input())
expo = [1]
for b in range(2, int(x ** .5) + 1):
    a = b
    while a * b <= x:
        a *= b
        expo.append(a)

print(max(expo))