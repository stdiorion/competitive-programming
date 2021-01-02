from sys import stdin
from functools import reduce
input = stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
query = [list(map(int, input().split())) for i in range(Q)]

for q in query:
    if q[0] == 1:
        A[q[1] - 1] ^= q[2]
    if q[0] == 2:
        print(reduce(lambda i, j: i ^ j, A[q[1] - 1 : q[2]]))