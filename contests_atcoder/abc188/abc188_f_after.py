from collections import defaultdict

x, y = map(int, input().split())

memo = defaultdict(lambda: -1)

def score(n):
    if memo[n] != -1:
        return memo[n]
    
    if n <= x:
        memo[n] = x - n  
    elif n % 2 == 0:
        memo[n] = min(score(n // 2) + 1, n - x)
    else:
        memo[n] = min(score(n + 1) + 1, score(n - 1) + 1)
    return memo[n]

print(score(y))