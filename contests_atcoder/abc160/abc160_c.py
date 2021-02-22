k, n = map(int, input().split())
a = list(map(int, input().split()))
a += [a[0] + k]
a = [y - x for x, y in zip(a, a[1:])]
print(k - max(a))