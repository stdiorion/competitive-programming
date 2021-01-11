n, k = map(int, input().split())
s = input()

s *= 2

def match(two):
    if two[0] == two[1]:
        return two[0]
    if two == "RS" or two == "SR":
        return "R"
    if two == "SP" or two == "PS":
        return "S"
    if two == "PR" or two == "RP":
        return "P"

for i in range(k, 0, -1):
    s_new = ""
    for pos in range(n):
        s_new += match(s[2*pos:2*pos+2])
    s = s_new * 2

print(s[0])