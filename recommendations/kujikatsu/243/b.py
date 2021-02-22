n = int(input())
w = list(map(int, input().split()))
ans = float("inf")
for t in range(1, n + 1):
    ans = min(abs(sum(w[:t]) - sum(w[t:])), ans)
print(ans)