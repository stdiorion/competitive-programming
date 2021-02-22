from random import randint

h, w = randint(2, 10), randint(2, 10)
print(h, w)

for i in range(h):
    row = ""
    for j in range(w):
        row += "." if randint(0, 5) else "#"
    print(row)
print()