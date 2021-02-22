n, x = map(int, input().split())
a = list(map(int, input().split()))

print(*[b for b in a if b != x])