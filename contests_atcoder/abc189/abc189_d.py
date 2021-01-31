n = int(input())
s = [input() for _ in range(n)]

def solve(k):
    if k == 0: return 1
    elif s[k-1] == "OR": return solve(k-1) + 2 ** k
    else: return solve(k-1)

print(solve(n))