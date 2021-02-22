from random import randint

print(2000, 10**8)
for _ in range(2000):
    print("".join(str(randint(0, 1)) for _ in range(2000)))