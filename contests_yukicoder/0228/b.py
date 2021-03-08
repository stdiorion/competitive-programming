from math import cos, sin
n, w = map(int, input().split())
sushi = [tuple(map(int, input().split())) for _ in range(n)]

def solve(t, sushi):
    for x, y, r, v, a in sushi:
        