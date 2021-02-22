n, k = map(int, input().split())

def g1(x):
    return int("".join(sorted(str(x), reverse=True)))

def g2(x):
    return int("".join(sorted(str(x))))

ans = n
for i in range(k):
    ans = g1(ans) - g2(ans)

print(ans)