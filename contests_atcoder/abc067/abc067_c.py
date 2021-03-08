n = int(input())
a = list(map(int, input().split()))
snuke = sum(a[1:])
arai = a[0]

ans = abs(snuke - arai)

for x in a[1:-1]:
    snuke -= x
    arai += x
    ans = min(ans, abs(snuke - arai))

print(ans)