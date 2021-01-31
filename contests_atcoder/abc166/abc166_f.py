n, a, b, c = map(int, input().split())
s = [input() for _ in range(n)] + ["end"]

num = {"A": a, "B": b, "C": c}

ans = []

for i in range(n):
    if num[s[i][0]] == num[s[i][1]] == 0:
        print("No")
        exit()
    elif num[s[i][0]] == 0:
        choice = s[i][0]
        reduce = s[i][1]
    elif num[s[i][1]] == 0:
        choice = s[i][1]
        reduce = s[i][0]
    elif s[i][0] in s[i + 1]:
        choice = s[i][0]
        reduce = s[i][1]
    else:
        choice = s[i][1]
        reduce = s[i][0]
    ans.append(choice)
    num[choice] += 1
    num[reduce] -= 1

print("Yes")
print(*ans, sep="\n")