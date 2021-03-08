n, m, c = map(int, input().split())
b = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(n)]

print(sum(int(sum(x * y for x, y in zip(a, b)) > -c) for a in A))