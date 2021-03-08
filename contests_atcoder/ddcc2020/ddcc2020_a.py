x, y = map(int, input().split())
if x == y == 1:
    print(1000000)
else:
    print(max(0, 100000 * (4 - x)) + max(0, 100000 * (4 - y)))