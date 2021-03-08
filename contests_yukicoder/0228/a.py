a, b, c, d = map(int, input().split())

c -= a
d -= b
c = abs(c)
d = abs(d)

def movable(u, v):
    return u == 0 or v == 0 or u + v <= 3

if movable(c, d):
    print(1)
else:
    print(2) 