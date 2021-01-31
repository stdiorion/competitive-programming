n, k = map(int, input().split())
a = list(map(int, input().split()))

move = [1]
visited = {1}

for i in range(n):
    if i == k:
        print(move[-1])
        exit()
    elif a[move[-1] - 1] not in visited:
        visited.add(a[move[-1] - 1])
        move.append(a[move[-1] - 1])
    else:
        l = move.index(a[move[-1] - 1])
        loop = move[l:]
        print(loop[(k - l) % len(loop)])
        exit()