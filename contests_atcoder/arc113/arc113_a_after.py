k = int(input())

div = [[] for _ in range(k + 1)]
for d in range(1, k + 1):
    for i in range(d, k + 1, d):
        div[i].append(d)

count = 0

for i in range(1, k + 1):
    for a in div[i]:
        count += len(div[a])

print(count)