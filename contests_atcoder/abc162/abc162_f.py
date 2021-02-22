from itertools import accumulate
INF = float("inf")
n = int(input())
a = list(map(int, input().split()))

if n % 2:
    # odd
    offset0 = [0] + list(accumulate(a[:-1:2]))
    offset1 = [0] + list(accumulate(a[1::2]))
    offset2 = [0] + list(accumulate(a[2::2]))

    ans = -INF
    base_i = []
    base_j = []

    for i in range(n // 2 + 1):
        base_i.append((offset0[i] - offset1[i] + offset2[n // 2], i))
    for j in range(n // 2 + 1):
        base_j.append((offset1[j] - offset2[j], j))

    base_i.sort(reverse=True, key=lambda x: x[0])
    base_j.sort(reverse=True, key=lambda x: x[0])
    
    for k in range(n // 2 + 1):
        for l in range(k + 1):
            if base_i[l][1] <= base_j[k - l][1]:
                ans = max(ans, base_i[l][0] + base_j[k - l][0])
        if ans != -INF:
            break
    print(ans)

else:
    # even
    front = [0] + list(accumulate(a[::2]))
    back = [0] + list(accumulate(a[::-2]))
    ans = -INF
    for i in range(n // 2 + 1):
        ans = max(ans, front[i] + back[n // 2 - i])
    print(ans)