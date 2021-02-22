s = input()
k = int(input())

cand = []
for length in range(1, 6):
    for i in range(len(s) - length + 1):
        cand.append(s[i:i + length])

cand = list(set(cand))

print(sorted(cand)[k - 1])