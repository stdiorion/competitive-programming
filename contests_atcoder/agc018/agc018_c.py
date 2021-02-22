import sys
input = sys.stdin.readline
from operator import itemgetter

x, y, z = map(int, input().split())
coins = [tuple(map(int, input().split())) for _ in range(x + y + z)]


def solve(value, x, y, z):
    value.sort(reverse=True, key=itemgetter(0, 2))

    res = sum(a for abc, bc, a, b, c in value[:x])

    value = value[x:]

    value.sort(reverse=True, key=itemgetter(1, 3))

    res += sum(b for abc, bc, a, b, c in value[:y])
    res += sum(c for abc, bc, a, b, c in value[y:])

    return res

value1 = [(a - b - c, b - c, a, b, c) for a, b, c in coins]
value2 = [(b - c - a, c - a, b, c, a) for a, b, c in coins]
value3 = [(c - a - b, a - b, c, a, b) for a, b, c in coins]

ans = max(solve(value1, x, y, z), solve(value2, y, z, x), solve(value3, z, x, y))
print(ans)