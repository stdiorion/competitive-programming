s = input()
n = len(s)
f = s[:n // 2]
l = s[n // 2 + 1:]
if s == s[::-1] and f == f[::-1] and l == l[::-1]:
    print("Yes")
else:
    print("No")