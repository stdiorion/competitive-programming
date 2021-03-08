INF = float("inf")
def solve():
    x, y, p, q = map(int, input().split())

    if 2 * (x + y) == p + q:
        if x + y <= p:
            print("infinity")
        else:
            print(max(x, p))
        return

    ans = INF
    t = x
    for i in range(100000):
        if t % (p + q) >= p:
            ans = min(ans, t)
            break
        t += x + x + y + y

    t = p
    for i in range(100000):
        if x <= t % (x + x + y + y) < x + y:
            ans = min(ans, t)
            break
        t += p + q
    
    print(ans)

for _ in range(int(input())):
    solve()