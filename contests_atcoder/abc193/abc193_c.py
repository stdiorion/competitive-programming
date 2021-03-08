n = int(input())
exp = set()

for a in range(2, int(n ** .5) + 1):
    b = a
    while a * b <= n:
        a *= b
        exp.add(a)

print(n - len(exp))