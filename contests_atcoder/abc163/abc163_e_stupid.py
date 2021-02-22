from itertools import permutations
n = int(input())
a = list(map(int, input().split()))
a_i = [(x, i) for i, x in enumerate(a)]

ans = 0

for perm in permutations(a_i, n):
    score = 0
    for i, (x, i_be) in enumerate(perm):
        score += x * abs(i - i_be)
    if ans < score:
        ans = score
        ans_perm = perm

print(ans)