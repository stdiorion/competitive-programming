from random import randint

n = randint(1, 1000)
q = randint(1, 100)
print(n, q)

a = []

for i in range(n):
    a.append(randint(0, 1000))

print(*a)

for i in range(q):
    if randint(0, 1):
        print(1, randint(1, n), randint(0, 10))
    else:
        x, y = randint(1, n), randint(1, n)
        if x > y: x, y = y, x
        print(2, x, y)