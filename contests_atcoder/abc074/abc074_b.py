n = int(input())
k = int(input())
x = list(map(int, input().split()))
print(2 * sum(min(v, k - v) for v in x))