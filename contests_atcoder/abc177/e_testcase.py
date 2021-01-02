import random

with open("test.txt", "w") as f:
    f.write("")

n = 100000

print(n, file=open("test.txt", "a"))

li = [random.randint(1, n) for _ in range(n)]

print(*li, file=open("test.txt", "a"))