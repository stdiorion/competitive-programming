from math import sqrt
from decimal import *

n = int(input())

#print(n + 1 - int((-1 + sqrt(9 + 8 * n)) // 2))
print(n + 1 - (-1 + Decimal(9 + 8 * n).sqrt()) // 2)

exit()

scrap = (-1 + sqrt(9 + 8 * n)) // 2 # float // int なので float になる
print(scrap)

print(n + 1 - scrap)      # int - float なので float にキャストして演算する → 15桁ほどで桁落ち
print(int(n + 1 - scrap))
print(n + 1 - int(scrap)) # int - int なので int のまま演算する
