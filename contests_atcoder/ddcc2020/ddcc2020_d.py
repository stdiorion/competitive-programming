m = int(input())
dc = [tuple(map(int, input().split())) for _ in range(m)]
print(sum(c for d, c in dc) - 1 + (sum(d * c for d, c in dc) - 1) // 9)