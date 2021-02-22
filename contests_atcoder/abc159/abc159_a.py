n, m = map(int, input().split())
ansn = 0
if n:
    ansn += n * (n - 1) // 2
ansm = 0
if m:
    ansm = m * (m - 1) // 2
print(ansn + ansm)