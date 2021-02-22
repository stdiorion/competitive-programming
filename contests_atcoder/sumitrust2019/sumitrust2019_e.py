MOD = 10 ** 9 + 7
n = int(input())
a = list(map(int, input().split()))

remain = [0] * 110000
remain[0] = 3

ans = 1

for x in a:
    ans *= remain[x]
    ans %= MOD
    remain[x] -= 1
    remain[x + 1] += 1

print(ans)