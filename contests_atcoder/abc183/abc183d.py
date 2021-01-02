import heapq

n, w = map(int, input().split())


user = [tuple(map(int, input().split())) for _ in range(n)]
user.sort()

usage = []
using = 0

for i in range(n):
    now = user[i][0]

    while len(usage) and usage[0][0] <= now:
        u = heapq.heappop(usage)
        using -= u[1]

    heapq.heappush(usage, user[i][1:])
    using += user[i][2]

    if using > w:
        print("No")
        exit()

print("Yes")