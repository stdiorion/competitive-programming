from collections import Counter

n = int(input())
a = list(map(int, input().split()))
Q = int(input())
queries = [list(map(int, input().split())) for _ in range(Q)]

ans = sum(a)
A = Counter(a)

for q in queries:
    ans += (q[1] - q[0]) * A[q[0]]
    A[q[1]] += A[q[0]]
    A[q[0]] = 0
    print(ans)