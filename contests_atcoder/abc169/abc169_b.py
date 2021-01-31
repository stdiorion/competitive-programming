n = int(input())
a = list(map(int, input().split()))

ans = 1

if 0 in a:
    print(0)
    exit()
    
for x in a:
    ans *= x
    if ans > 10 ** 18:
        print(-1)
        exit()

print(ans)