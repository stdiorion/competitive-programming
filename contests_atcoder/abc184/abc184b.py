from sys import stdin
input = stdin.readline

N, X = map(int, input().split())
S = input()

for char in S:
    if char == "o":
        X += 1
    elif char == "x":
        X = max(X - 1, 0)

print(X)