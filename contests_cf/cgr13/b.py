def solve():
    n, u, v = map(int, input().split())
    a = list(map(int, input().split()))

    ans = float("inf")

    for i in range(n):
        if i > 0:
            if abs(a[i - 1] - a[i]) == 0:
                ans = min(ans, 2 * v, v + u)
            elif abs(a[i - 1] - a[i]) == 1:
                ans = min(ans, u)
                if i == n and a[i] == 10 ** 6 and a[i - 1] == 10 ** 6 - 1:
                    ans = min(ans, 3 * v)
                else:
                    ans = min(ans, v)
            else:
                ans = 0
        if i < n - 1:
            if abs(a[i + 1] - a[i]) == 0:
                ans = min(ans, 2 * v, v + u)
            elif abs(a[i + 1] - a[i]) == 1:
                ans = min(ans, u)
                if i == n and a[i] == 1 and a[i + 1] == 2:
                    ans = min(ans, 3 * v)
                else:
                    ans = min(ans, v)
            else:
                ans = 0
    print(ans)


t = int(input())
for _ in range(t): solve()