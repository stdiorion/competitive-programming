n = int(input())
a = list(map(int, input().split()))

k_max = 0
g_max = 0

for k in range(2, max(a) + 1):
    gcdness = 0
    for elem in a:
        if elem % k == 0:
            gcdness += 1
    
    if gcdness >= g_max:
        g_max = gcdness
        k_max = k

print(k_max)