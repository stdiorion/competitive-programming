n = int(input())
ans = [2 * 10 ** 9, 10 ** 9] + list(range(2, n + 1)) + [2 * 10 ** 9]
print(*ans)