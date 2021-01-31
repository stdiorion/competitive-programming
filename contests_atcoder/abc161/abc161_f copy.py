def div(n):
    lo = []
    hi = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lo.append(i)
            if n // i != i:
                hi.append(n // i)
        i += 1
    return lo + hi[::-1]

for n in range(2, 101):
    print(f"n = {n}")
    n_list = []
    ans_list = []

    for k in range(2, n + 1):
        N = n
        while N > 1:
            if N % k:
                N -= k
            else:
                N //= k
        n_list.append(N)
        if N == 1:
            ans_list.append(k)

    ans_ = len(ans_list)

    print(ans_list)

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

    if ans != ans_:
        print(f"**** Out: {ans} Ans: {ans_} ")