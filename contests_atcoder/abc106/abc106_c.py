s = input()
k = int(input())

one = 0
char = s[0]
for x in s:
    if x == "1":
        one += 1
    else:
        char = x
        break

if one >= k:
    print(1)
else:
    print(char)