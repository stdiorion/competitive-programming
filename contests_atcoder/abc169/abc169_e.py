n = int(input())
X = [tuple(map(int, input().split())) for _ in range(n)]

a = []
b = []

for x in X:
    a.append(x[0])
    b.append(x[1])

a.sort()
b.sort()

if n % 2:
    print(b[(n-1)//2] - a[(n-1)//2] + 1)
else:
    print(b[n//2] + b[n//2-1] - a[n//2] - a[n//2-1] + 1)