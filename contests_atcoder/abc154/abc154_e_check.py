from random import randint

def stupid(n, k):
    n = int(n)
    count = 0

    for i in range(1, n + 1):
        I = str(i)
        if len(I) - I.count("0") == k:
            count += 1
    return count

def solve(n, k):
    ans = 0
    
    while n[0] == "0":
        n = n[1:]
        if len(n) == 0:
            return 0

    if k == 1:
        ans += int(n[0])
        ans += (len(n) - 1) * 9
    elif k == 2:
        # 1文字目をそのまま使う
        if len(n) >= 2:
            ans += solve(n[1:], 1)
        # 1文字目を減らして使う
        if len(n) >= 2:
            ans += (int(n[0]) - 1) * (len(n) - 1) * 9
        # 1文字目を0にする
        if len(n) >= 3:
            ans += (len(n) - 1) * (len(n) - 2) // 2 * 81
    else:
        if len(n) >= 3:
            ans += solve(n[1:], 2)
        if len(n) >= 3:
            ans += (int(n[0]) - 1) * (len(n) - 1) * (len(n) - 2) // 2 * 81
        if len(n) >= 4:
            ans += (len(n) - 1) * (len(n) - 2) * (len(n) - 3) // 6 * 9 ** 3
    return ans

for _ in range(100):
    n = str(randint(1, 1000))
    k = randint(1, 3)
    ans1 = solve(n, k)
    ans2 = stupid(n, k)
    if ans1 != ans2:
        print(n)
        print(k)
        print(ans1, ans2)
        print()