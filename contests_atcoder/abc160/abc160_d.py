from collections import deque
n, x, y = map(int, input().split())
x -= 1
y -= 1

dist_count = [0] * n

for i in range(n):
    d = deque()
    d.append((i, 0))
    visited = [False] * n
    visited[i] = True

    while d:
        now, dist = d.popleft()

        dist_count[dist] += 1

        if now - 1 >= 0 and not visited[now - 1]:
            d.append((now - 1, dist + 1))
            visited[now - 1] = True
        
        if now + 1 < n and not visited[now + 1]:
            d.append((now + 1, dist + 1))
            visited[now + 1] = True
        
        if now == x and not visited[y]:
            d.append((y, dist + 1))
            visited[y] = True
        
        if now == y and not visited[x]:
            d.append((x, dist + 1))
            visited[x] = True

dist_count = [x // 2 for x in dist_count]
print(*dist_count[1:], sep="\n")