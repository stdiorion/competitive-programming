def sgn(x):
    return (x > 0) - (x < 0)

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a = [a[0]] * 2 + a + [a[-1]] * 2

    it = []
    ita = it.append

    chg = 0

    for i in range(2, n + 2):
        ita(a[i-1] < a[i] > a[i+1] or a[i-1] > a[i] < a[i+1])
        if chg == 0 and it[-1]: chg = 1
        if chg < 3 and i > 2 and it[-1] and it[-2] and it[-3]: chg = 3
        if chg < 2 and i > 4 and not it[-1] and it[-2] and it[-3] and not it[-4]:
            chg = 1 + (a[i-2] <= a[i] <= a[i+1] or a[i-4] <= a[i-3] <= a[i-1] or a[i-2] >= a[i] >= a[i+1] or a[i-4] >= a[i-3] >= a[i-1])
    
    ans = sum(it) - chg
    print(ans)