h, w = map(int, input().split())
print((h * w + 1) // 2 if min(h, w) > 1 else 1)