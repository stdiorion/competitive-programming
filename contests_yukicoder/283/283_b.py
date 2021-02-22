v, d = map(int, input().split())

def out(matrix):
    for row in matrix:
        print(*row, sep="")

if d == 1:
    ans = [[1] * v for _ in range(v)]
    out(ans)
else:
    ans = [[1] * v]
    for _ in range(v - 1):
        ans.append([1] + [0] * (v - 1))
    out(ans)