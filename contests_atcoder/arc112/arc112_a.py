t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    ans = 0
    for c in range(l, r - l + 1):
        ans += r - (l + c) + 1
    print(ans)