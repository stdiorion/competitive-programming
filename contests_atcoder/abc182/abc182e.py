import heapq as hq

h, w, n, m = map(int, input().split())

lights = []

for _ in range(n):
    hq.heappush(lights, tuple(map(int, input().split()))

