from itertools import zip_longest
Q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(Q)]

def popcnt(x):
    return bin(x).count("1")

for u, v in queries:
    if u > v:
        print("NO")
    elif u == v:
        print("YES")
    else:
        u = bin(u)[::-1]
        v = bin(v)[::-1]
        battle = 0
        for x, y in zip_longest(u, v[:-2]):
            battle += int(x == "1") - int(y == "1")
            if battle < 0:
                print("NO")
                break
        else:
            print("YES")
