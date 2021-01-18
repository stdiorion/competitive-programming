MOD = 10 ** 9 + 7

def modprod(l):
    ret = 1
    for x in l:
        ret *= x
        ret %= MOD
    return ret

n, k = map(int, input().split())
a = list(map(int, input().split()))

plus = [x for x in a if x > 0]
minus = [x for x in a if x < 0]
zero = a.count(0)

plus.sort()
minus.sort()

ans = 1

if len(a) == k:
    ans = modprod(a)
elif len(plus) + len(minus) < k:
    ans = 0
elif len(plus) + len(minus) == k:
    ans = 0 if len(minus) % 2 else modprod(plus + minus)
else: # len(plus) + len(minus) > k
    if len(plus) == 0:
        if k % 2:
            if zero:
                ans = 0
            else:
                ans = modprod(minus[-k:])
        else:
            ans = modprod(minus[:k])
    else: # len(plus) > 0
        if k % 2:
            k -= 1
            ans = plus.pop()
        pairprod = [plus[-1-2*i] * plus[-2-2*i] for i in range(len(plus) // 2)]
        pairprod += [minus[2*i] * minus[2*i+1] for i in range(len(minus) // 2)]
        pairprod.sort(reverse=True)
        ans *= modprod(pairprod[:k // 2])
        ans %= MOD

print(ans)