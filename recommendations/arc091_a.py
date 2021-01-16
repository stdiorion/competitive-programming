n, m = map(int, input().split())

if n > m:
    n, m = m, n

if n == 1:
    if m == 1:
        print(1)
    else:
        print(m - 2)
else:
    print((n - 2) * (m - 2))