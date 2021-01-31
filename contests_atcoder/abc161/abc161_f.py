n = int(input())

def div(n):
    lo = []
    hi = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            lo.append(i)
            if n // i != i: hi.append(n // i)
    return lo + hi[::-1]

k_list = div(n) + div(n-1)

k_set = set(k_list)
k_set.discard(1)

ans = len(k_set)

for k in k_set:
    N = n
    while N > 1:
        if N % k:
            N %= k
            if N > 1: break
        else:
            N //= k
    
    if N != 1:
        ans -= 1

print(ans)