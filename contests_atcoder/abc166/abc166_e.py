n = int(input())
a = list(map(int, input().split()))

bottom = [0] * n
top = [0] * n

for i, x in enumerate(a):
    if i + x < n:
        bottom[i + x] += 1
    if i - x >= 0:
        top[i - x] += 1

print(sum(u * v for u, v in zip(bottom, top)))