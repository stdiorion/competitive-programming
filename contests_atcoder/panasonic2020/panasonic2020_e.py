from itertools import permutations
import re
a = input()
b = input()
c = input()
s = len(a) + len(b) + len(c)
for x, y, z in permutations((a, b, c), 3):
    for i in range(len(x) + 1):
        for p, q in zip(x[i:], y):
            if p != q and p != "?" and q != "?":
                break
        else:
            for j in range(max(len(y) + 1, len(x) - i + 1)):
                for p, q in zip(y[j:], z):
                    if p != q and p != "?" and q != "?":
                        break
                else:
                    for p, q in zip(x[i + j:], z):
                        if p != q and p != "?" and q != "?":
                            break
                    else:
                        s = min(s, max(len(x), len(y) + i, len(z) + i + j))
print(s)