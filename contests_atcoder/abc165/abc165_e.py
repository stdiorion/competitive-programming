n, m = map(int, input().split())
if n % 2:
    n -= n % 2
    print(*[str(1 + i) + " " + str(n - i) for i in range(m)], sep="\n")
else:
    k = n // 2
    lower = [str(1 + i) + " " + str(k - i) for i in range(k // 2)]
    upper = [str(k + 1 + i) + " " + str(n - 1 - i) for i in range(k // 2)]
    ans = lower + upper
    print(*ans[:m], sep="\n")