from collections import defaultdict
MOD = 998244353
r, c, n = map(int, input().split())

bit_prev = defaultdict(int)
bit_prev[(0, 0)] = 1

for row in range(r + 1):
    bit_prev_new = defaultdict(int)
    for pbit, vcount in bit_prev:
        pbit <<= 1
        for bit in range(1 << c):
            bit <<= 1
            vcount_new = vcount
            for i in range(c + 1):
                if ((pbit >> i) & 1 + (pbit >> i + 1) & 1 + (bit >> i) & 1 + (bit >> i + 1) & 1) & 1:
                    vcount_new += 1
                elif (pbit >> i) & 1 != (pbit >> i + 1) & 1 != (bit >> i) & 1 != (bit >> i + 1) & 1:
                    break
            else:
                bit >>= 1
                pbit >>= 1
                bit_prev_new[(bit, vcount_new)] += bit_prev[(pbit, vcount)]
            if row == r:
                break
    bit_prev = bit_prev_new.copy()
ans = sum(bit_prev[(pbit, vcount)] for pbit, vcount in bit_prev if vcount == n)
print(ans)