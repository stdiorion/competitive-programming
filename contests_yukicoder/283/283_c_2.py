v, d = map(int, input().split())
e = [[x == "1" for x in input()] for _ in range(v)]

def power(a, b):
    c = [[False] * v for _ in range(v)]
    for i in range(v):
        for j in range(v):
            for k in range(v):
                if a[i][k] & b[k][j]:
                    c[i][j] = True
                    break
    return c

digits = len(bin(d)[2:])

ans = [[True if i == j else False for j in range(v)] for i in range(v)]

for i in range(digits):
    if d & 1:
        ans = power(ans, e)
    e = power(e, e)
    d >>= 1

for row in ans:
    for x in row:
        if x == False:
            print("No")
            exit()

print("Yes")