n = int(input())
A = list(map(int, input().split()))

A_ = sorted(list(set(A)))

ans = 0

for b in A_:
    cnt = 0
    max_cnt = 0
    for a in A:
        if a < b:
            if max_cnt < cnt: max_cnt = cnt
            cnt = 0
        else:
            cnt += 1
    if max_cnt < cnt: max_cnt = cnt
    ans = max(ans, b * max_cnt)

print(ans)