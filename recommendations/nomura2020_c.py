n = int(input())
leaves = list(map(int, input().split()))

capacity = [0]

for i in range(n + 1):
    if (i != n and leaves[i] > capacity[i]) or (i == n and leaves[i] > capacity[i] + 1):
        print(-1)
        exit()
    capacity[i] -= leaves[i]
    capacity.append(1 + capacity[i] * 2)

leavesum = [0] * n + [leaves[n] - 1]

for i in reversed(range(n)):
    leavesum[i] = min(leaves[i] + capacity[i], leaves[i] + leavesum[i + 1])

ans = n + 1 + sum(leavesum)

print(ans)