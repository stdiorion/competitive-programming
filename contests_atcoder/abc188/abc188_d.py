import heapq
import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 10 ** 9 + 7
INF = float("inf")

n, c = map(int, input().split())
services = [tuple(map(int, input().split())) for _ in range(n)]

timeline = []

for service in services:
    heapq.heappush(timeline, (service[0], service[2]))
    heapq.heappush(timeline, (service[1]+1, -service[2]))

first_trans = heapq.heappop(timeline)
prev_time = first_trans[0]
daily_payment = first_trans[1]
total_payment = 0

while timeline:
    transaction = heapq.heappop(timeline)
    total_payment += (transaction[0] - prev_time) * min(daily_payment, c)
    prev_time = transaction[0]
    daily_payment += transaction[1]

print(total_payment)