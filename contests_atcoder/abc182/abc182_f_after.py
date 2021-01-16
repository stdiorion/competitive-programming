from collections import defaultdict
n, x = map(int, input().split())
a = list(map(int, input().split())) + [float("inf")]

memo = defaultdict(int)
def solve(yen, i):
    if memo[(yen, i)]:
        return memo[(yen, i)]
    remain = yen % a[i]
    if remain:
        if a[i] + yen < a[i+1]:
            memo[(yen, i)] += solve(remain - a[i], i - 1)
        if a[i] - yen < a[i+1]:
            memo[(yen, i)] += solve(remain, i - 1)
        return memo[(yen, i)]
    else:
        return 1

print(solve(x, n - 1))