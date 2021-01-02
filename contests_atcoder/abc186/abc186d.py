n = int(input())
a = list(map(int, input().split()))

a.sort()

ans = 0

for i, num in enumerate(a):
    ans += ((-len(a) + 1) + 2 * i) * num

print(ans)