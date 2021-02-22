from itertools import accumulate
INF = float("inf")
h, w, k = map(int, input().split())
field = [[0] + list(accumulate(map(int, input()))) for _ in range(h)]
ans = INF
for bit in range(1 << h - 1):
    bit <<= 1
    division = bin(bit).count("1")
    prev = 0
    for j in range(1, w + 1):
        count = 0
        for i in range(h):
            if (bit >> i) & 1:
                # divide
                count = field[i][j] - field[i][prev]
            else:
                # not divide
                count += field[i][j] - field[i][prev]
            if count > k:
                division += 1 if prev < j - 1 else INF
                prev = j - 1
                break
    ans = min(ans, division)
print(ans)