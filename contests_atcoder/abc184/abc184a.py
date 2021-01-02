from sys import stdin
input = stdin.readline


a, b = map(int, input().split())
c, d = map(int, input().split())

print(a * d - b * c)