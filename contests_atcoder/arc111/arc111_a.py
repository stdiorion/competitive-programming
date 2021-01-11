from bisect import bisect_left, bisect_right
from collections import deque, Counter
from itertools import combinations, permutations
from math import gcd, sin, cos, tan, degrees, radians
import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 10 ** 9 + 7
INF = float("inf")

n, m = map(int, input().split())

ans = pow(10, n, m ** 2) // m
print(ans)

# for i in range(1, n):
#     print(((10 ** i) // m))
    # if ((10 ** i) // m) % m != 0 and ((10 ** i) // m) % m in anslog:
    #     print("loop!!")
    
    # anslog.add(((10 ** i) // m) % m)


# def cycle_len(k):
#     rem = 1
#     rem_log = []
#     while True:
#         rem %= k
#         if rem == 0:
#             return 0 # 有限小数の場合は0を返す
#         if rem in rem_log:
#             return len(rem_log[rem_log.index(rem):])
#         rem_log.append(rem)
#         rem *= 10

# nonzero_appears = False
# cycle = cycle_len(m)

# if cycle == 0:
#     for i in range(1, n):
#         if (10 ** i) // m % m == 0:
#             if nonzero_appears:
#                 print(0)
#                 exit()
#         else:
#             nonzero_appears = True
#     else:
#         print((10 ** n) // m % m)
# else:
#     print((10 ** cycle))