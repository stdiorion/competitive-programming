from sys import stdin
from operator import mul
from functools import reduce
input = stdin.readline

L = int(input())

// https://note.nkmk.me/python-math-factorial-permutations-combinations/
def combinations_count(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom

print(combinations_count(L - 1, 11))