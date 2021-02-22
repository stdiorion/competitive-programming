n = input()
k = int(input())


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


print(solve(n, k))