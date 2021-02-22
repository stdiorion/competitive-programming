from itertools import accumulate
n, k = map(int, input().split())
p = list([int(x) + 1 for x in input().split()])

p = [0] + list(accumulate(p))

ans = 0
for i in range(n - k + 1):
    ans = max(ans, p[i + k] - p[i])

print(ans / 2)