t = int(input())
N = [int(input()) for _ in range(t)]

for n in N:
    ans = "9"
    for i in range(n - 1):
        ans += str((i + 8) % 10)
    print(ans)