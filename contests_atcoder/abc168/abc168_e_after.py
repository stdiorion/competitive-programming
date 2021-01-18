from collections import defaultdict
from fractions import Fraction
import sys
input = sys.stdin.buffer.readline
MOD = 10 ** 9 + 7
 
n = int(input())

dic = defaultdict(lambda: [0, 0])
zero = 0
a_zero = 0
b_zero = 0

for _ in range(n):
    a, b = map(int, input().split())

    if a == b == 0:
        zero += 1
    elif a == 0:
        a_zero += 1
    elif b == 0:
        b_zero += 1
    else:
        if a * b > 0:
            key = Fraction(a, b)
            dic[key][0] += 1
        else:
            key = Fraction(-b, a)
            dic[key][1] += 1

# 仲の悪いペアからどちらかのグループを選んでそこから取り出す場合の数をかけていく
ans = pow(2, a_zero, MOD) + pow(2, b_zero, MOD) - 1

for (n1, n2) in dic.values():
    ans *= pow(2, n1, MOD) + pow(2, n2, MOD) - 1
    ans %= MOD

# クーラーボックスが空の場合
ans -= 1

# 孤立するやつ
ans += zero
ans %= MOD

print(ans)