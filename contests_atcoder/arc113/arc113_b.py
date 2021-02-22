a, b, c = map(int, input().split())
if a % 10 == 0:
    print(0)
elif b % 10 == 0 and c > 10000:
    print(6)
elif b % 10 == 0:
    print(pow(a, pow(b, c), 10))
else:
    print(pow(a, pow(b, c, 100), 10))