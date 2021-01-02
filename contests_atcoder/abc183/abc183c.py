from itertools import permutations

n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]

order = list(permutations(range(1, n)))

ans = 0

for o in order:
    time_spent = 0
    prev = 0
    for i in o:
        time_spent += t[prev][i]
        prev = i
    time_spent += t[i][0]
    if time_spent == k:
        ans += 1

print(ans)