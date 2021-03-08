n = int(input())
x = list(map(int, input().split()))

p = int(sum(x) / n + 0.5)

print(sum((k-p)**2 for k in x))