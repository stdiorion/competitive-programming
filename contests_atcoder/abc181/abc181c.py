from itertools import combinations

n = int(input())

points = [tuple(map(int, input().split())) for _ in range(n)]

for t in combinations(points, 3):
    if (t[0][0] - t[1][0]) * (t[0][1] - t[2][1]) == (t[0][1] - t[1][1]) * (t[0][0] - t[2][0]):
        print("Yes")
        exit()

print("No")