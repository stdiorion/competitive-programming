n = int(input())
if n == 1:
    print(101)
    exit()

a = sum(map(int, input().split()))
ans = 0
for i in range(101):
    if (a + i) % n == 0:
        ans += 1
print(ans)