s = input()
k = int(input())

subst = list(s)

for i in range(2, k + 1):
    for j in range(len(s) - i + 1):
        subst.append(s[j:j + i])

subst = sorted(list(set(subst)))
print(subst[k - 1])