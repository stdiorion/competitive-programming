n = int(input()) - 1

ans = [["A" * 2 ** (i-1) + "B" * 2 ** (i-1)] for i in range(1, 9)]

for i in range(1, 8):
    for line in ans[i-1]:
        ans[i].append(line+line)
        ans[i].append(line+line.translate(str.maketrans('AB', 'BA')))

print(len(ans[n]))
print(*ans[n], sep="\n")