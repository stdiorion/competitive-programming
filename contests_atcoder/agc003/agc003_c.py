n = int(input())
a = [int(input()) for _ in range(n)]

b = sorted(a)
print(len(set(a[::2])^set(b[::2]))//2)

