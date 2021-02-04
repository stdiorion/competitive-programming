from itertools import combinations_with_replacement
n, m, q = map(int, input().split())
pairs = [tuple(map(int, input().split())) for _ in range(q)]
print(max(sum(p for i, j, c, p in pairs if a[j - 1] - a[i - 1] == c) for a in combinations_with_replacement(range(1, m + 1), n)))