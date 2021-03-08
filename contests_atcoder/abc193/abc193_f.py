n = int(input())
c = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if c[i][j] != "?": continue

        neighbor = []
        if i > 0: neighbor.append(c[i-1][j])
        if j > 0: neighbor.append(c[i][j-1])
        if i < n - 1: neighbor.append(c[i+1][j])
        if j < n - 1: neighbor.append(c[i][j+1])
        
        if neighbor.count("B") >= len(neighbor) // 2:
            c[i][j] = "W"
        elif neighbor.count("W") >= len(neighbor) // 2:
            c[i][j] = "B"
        else:
            score = max(10 * neighbor.count("B") - neighbor.count("?"), 10 * neighbor.count("W") - neighbor.count("?"))