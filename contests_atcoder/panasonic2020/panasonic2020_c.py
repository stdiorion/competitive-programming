a, b, c = map(int, input().split())
print("Yes" if 4 * a * b < (max(0, c - a - b)) ** 2 else "No")