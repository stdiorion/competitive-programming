n = int(input())
x = list(map(int, input().split()))

m = 0
e = 0
c = 0

for n in x:
    m += abs(n)
    e += n ** 2
    c = max(c, abs(n))

print(m)
print(e ** 0.5)
print(c)