def solve():
    n = int(input())
    s = list(map(int, input().split()))
    on = [0] * n

    ans = 0

    for i, x in enumerate(s):
        ans += max(0, x - on[i] - 1)
        on[i] += max(0, x - on[i] - 1)
        for j in range(2, min(n - i, x + 1)):
            on[i + j] += 1
        on[i] -= x - 1
        if i < n - 1 and on[i] > 0:
            on[i + 1] += on[i]
    
    print(ans)

t = int(input())
for _ in range(t): solve()