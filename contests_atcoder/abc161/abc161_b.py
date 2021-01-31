n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort(reverse=True)

if a[m-1] * 4 * m < sum(a): print("No")
else: print("Yes")