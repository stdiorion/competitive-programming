from sys import stdin
input = stdin.readline

K = int(input())
S = input().rstrip()

if K >= len(S):
    print(S)
else:
    print(S[:K] + "...")