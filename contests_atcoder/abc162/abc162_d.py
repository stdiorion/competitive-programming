n = int(input())
s = input()

ans = s.count("R") * s.count("G") * s.count("B")

for i in range(1, 2020):
    for j in range(4000):
        i1 = j
        i2 = j + i
        i3 = j + i + i
        if i3 >= n:
            break
        if s[i1] != s[i2] != s[i3] != s[i1]:
            ans -= 1
    
print(ans)