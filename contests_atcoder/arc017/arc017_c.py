from bisect import bisect_left, bisect_right
n, x = map(int, input().split())
w = [int(input()) for _ in range(n)]

pt1 = w[:16]
pt2 = w[16:]

w1 = []

for bit in range(1 << len(pt1)):
    weight = 0
    for i in range(len(pt1)):
        if (bit >> i) & 1:
            weight += pt1[i]
    w1.append(weight)

if not len(pt2):
    print(w1.count(x))
    exit()

w2 = []

for bit in range(1 << len(pt2)):
    weight = 0
    for i in range(len(pt2)):
        if (bit >> i) & 1:
            weight += pt2[i]
    w2.append(weight)


ans = 0

w1.sort()
w2.sort()
i2 = 0

for weight1 in w1:
    ans += bisect_right(w2, x - weight1) - bisect_left(w2, x - weight1)

print(ans)