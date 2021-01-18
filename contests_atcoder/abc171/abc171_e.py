n = int(input())
a = list(map(int, input().split()))

xor = a[0]
for x in a[1:]:
    xor ^= x

ans = print(*[xor ^ x for x in a])