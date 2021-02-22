n, m = map(int, input().split())
a = list(map(int, input().split()))
ans = n - sum(a)
print(ans if ans >= 0 else -1)