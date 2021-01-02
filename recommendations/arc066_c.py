MOD = 10 ** 9 + 7

n = int(input())
a = list(map(int, input().split()))

list.sort(a, reverse=True)

if n % 2:
    a.append(0)

for i in range(0, n, 2):
    if not(a[i] == a[i + 1] == n - i - 1):
        print(0)
        exit()

print(2 ** (n // 2) % MOD)