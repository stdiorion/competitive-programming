from collections import defaultdict
import numpy as np

r, c, k = map(int, input().split())
items = np.zeros((r, c), np.int32)

for _ in range(k):
    y, x, v = map(int, input().split())
    items[y - 1, x - 1] = v

dp = np.zeros((r, c, 4), np.int64)

for y in range(r):
    for x in range(c):
        dp[y, x, 0] = max(dp[y - 1, x]) if y != 0 else 0
        dp[y, x, 1] = max(dp[y - 1, x]) + items[y, x] if y != 0 else 0
        
        dp[y, x, 0] = max(dp[y, x, 0], dp[y, x - 1, 0]) if x != 0 else dp[y, x, 0]
        if x != 0:
            for k in range(3):
                dp[y, x, k + 1] = max(dp[y, x - 1, k] + items[y, x], dp[y, x - 1, k + 1], dp[y, x, k + 1])
        else:
            dp[y, x, 1] = dp[y, x, 0] + items[y, x]

#print(*dp, sep="\n")
print(max(dp[-1, -1]))