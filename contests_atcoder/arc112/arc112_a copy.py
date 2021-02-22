t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    if (r - l + 1 - l) > 0:
        ans = (r - l + 1) * (r - l + 1 - l) - r * (r - l + 1 - l) // 2
    else:
        ans = 0
    print(ans)