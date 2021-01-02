s = input()

for i in range(len(s) // 2):
    if s[i] != s[-i-1] and s[i] != "*" and s[-i-1] != "*":
        print("NO")
        exit()

print("YES")