MOD = 998244353
r, c, n = map(int, input().split())

dp = [[0] * (1 << c) for _ in range(r + 1)]
dp[0][0] = 1

for row in range(r):
    for bit_prev in range(1 << c):
        bit_prev <<= 1
        for bit in range(1 << c):
            bit <<= 1
            count = 0
            for i in range(c + 1):
                if ((bit_prev >> i) & 1 + (bit_prev >> i + 1) & 1 + (bit >> i) & 1 + (bit >> i + 1) & 1) & 1:
                    count += 1
            bit >>= 1
            dp[row + 1][bit] += count

print(sum(dp[-1]))