n, k = map(int, input().split())

snuke = set(range(1, n + 1))

for _ in range(k):
    d = int(input())
    a = list(map(int, input().split()))
    for x in a:
        snuke.discard(x)

print(len(snuke))