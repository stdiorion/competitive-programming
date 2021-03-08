n, m = map(int, input().split())
cond = [tuple(map(int, input().split())) for _ in range(m)]

for ans in range(0, 999):
    ans = str(ans)
    ok = True
    if len(ans) != n:
        continue
    for s, c in cond:
        if ans[s - 1] != str(c):
            ok = False
    
    if ok:
        print(ans)
        exit()
print(-1)